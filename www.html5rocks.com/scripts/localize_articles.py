#!/usr/bin/python2.4
# Copyright 2011 Google Inc. All Rights Reserved.
# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Generates HTML from Django, and Django from HTML for localization."""

from __future__ import with_statement

__author__ = ('mkwst@google.com (Mike West)')

import optparse
import os
import re

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


class Article(object):
  """Represents an article, and maps back and forth between Django and HTML.

  Attributes:
    DJANGO_ROOT: The root directory in which Django templates are found.
    HTML_ROOT: The root directory in which HTML files are found .
    django_: The absolute path to a specific Django template.
    html_: The absolute path to a specific HTML file.
  """
  DJANGO_ROOT = os.path.abspath(os.path.join(ROOT_DIR, '..', 'content'))
  HTML_ROOT = os.path.abspath(os.path.join(ROOT_DIR, '..', '_to_localize'))

  UNTRANSLATABLE_LABEL = r'<!--DO_NOT_TRANSLATE_BLOCK>'
  UNTRANSLATABLE_END_LABEL = r'</DO_NOT_TRANSLATE_BLOCK-->'

  CONTENT_LABEL = """
<!--CONTENT_BLOCK ***********************************************************-->
"""
  CONTENT_LABEL_END = """
<!--/END_CONTENT_BLOCK ******************************************************-->
"""

  def __init__(self, django=None, html=None):
    """Creates an Article object.

    Args:
      django: The path to a Django file (optional)
      html: The path to an HTML file (optional)
    """
    self.django_ = os.path.abspath(django) if django else ''
    self.html_ = os.path.abspath(html) if html else ''
    self._NormalizePaths()

  def _NormalizePaths(self):
    """Ensures that both the Django and HTML paths exist and are absolute."""

    if not self.django_:
      self.django_ = re.sub(r'^%s' % Article.HTML_ROOT,
                            Article.DJANGO_ROOT,
                            self.html_)
    if not self.html_:
      self.html_ = re.sub(r'^%s' % Article.DJANGO_ROOT,
                          Article.HTML_ROOT,
                          self.django_)
    self.html_ = os.path.abspath(self.html_)
    self.django_ = os.path.abspath(self.django_)

  def GenerateHTML(self):
    """Generates a localizable HTML file from a Django template.

    This function will also create the HTML file's directory if it doesn't
    already exist.
    """
    try:
      os.makedirs(os.path.dirname(self.html_))
    except os.error:
      pass
    print '* Generating `%s`' % self.html_
    with open(self.html_, 'w') as outfile:
      with open(self.django_, 'r') as infile:
        in_content = False
        for line in infile:
          (line, in_content) = self._HtmlizeLine(line, in_content)
          outfile.write(line)

  def _HtmlizeLine(self, line, in_content):
    """Given a line of a Django template, returns the corresponding HTML line

    * Replaces Django tags with comments in the form:
        <!--DO_NOT_TRANSLATE_BLOCK-->{DJANGO_TAG}<!--/DO_NOT_TRANSLATE_BLOCK-->

    * Replaces script/style/pre tags with comments in the form:
        <TAG_GOES_HERE><!--DO_NOT_TRANSLATE_BLOCK-->
        ...
        <!--/DO_NOT_TRANSLATE_BLOCK--></TAG_GOES_HERE>
    """

    UNESCAPED_DJANGO = r'(?P<tag>{%.+?%})'
    ESCAPED_DJANGO = r'%s\g<tag>%s' % (Article.UNTRANSLATABLE_LABEL,
                                       Article.UNTRANSLATABLE_END_LABEL,)

    UNESCAPED_UNTRANSLATABLE = r'(?P<tag><(?:pre|script|style)[^>]*?>)'
    ESCAPED_UNTRANSLATABLE = r'\g<tag>%s' % Article.UNTRANSLATABLE_LABEL

    UNESCAPED_UNTRANSLATABLE_END = r'(?P<tag></(?:pre|script|style)[^>]*?>)'
    ESCAPED_UNTRANSLATABLE_END = r'%s\g<tag>' % Article.UNTRANSLATABLE_END_LABEL

    UNESCAPED_CONTENT = r'{% block content %}'
    UNESCAPED_CONTENT_END = r'{% endblock %}'

    # Preprocess Django tags
    line = re.sub(UNESCAPED_DJANGO, ESCAPED_DJANGO, line)
    # Preprocess script/pre/style blocks
    line = re.sub(UNESCAPED_UNTRANSLATABLE, ESCAPED_UNTRANSLATABLE, line)
    line = re.sub(UNESCAPED_UNTRANSLATABLE_END,
                  ESCAPED_UNTRANSLATABLE_END,
                  line)
    # Preprocess content block
    if not in_content and re.search(UNESCAPED_CONTENT, line):
      line = Article.CONTENT_LABEL
      in_content = True
    if in_content and re.search(UNESCAPED_CONTENT_END, line):
      line = Article.CONTENT_LABEL_END
      in_content = False
    return (line, in_content)

  def GenerateDjango(self):
    """Generates a Django template from a localized HTML file.

    Implemented trivially by stripping comments in the form:
    `<!--DJANGO>...</DJANGO-->`. This function will also create the Django
    template's directory if it doesn't already exist.
    """
    try:
      os.makedirs(os.path.dirname(self.django_))
    except os.error:
      pass
    with open(self.html_, 'r') as infile:
      with open(self.django_, 'w') as outfile:
        for line in infile:
          # Preprocess Django tags
          line = re.sub(Article.ESCAPED_DJANGO, Article.UNESCAPED_DJANGO, line)
          # Preprocess script blocks
          line = line.replace(Article.ESCAPED_SCRIPT, Article.UNESCAPED_SCRIPT)
          line = line.replace(Article.ESCAPED_SCRIPT_END,
                              Article.UNESCAPED_SCRIPT_END)
          # Preprocess style blocks
          line = line.replace(Article.ESCAPED_STYLE, Article.UNESCAPED_STYLE)
          line = line.replace(Article.ESCAPED_STYLE_END,
                              Article.UNESCAPED_STYLE_END)
          outfile.write(line)


  def __str__(self):
    """String representation of an Article."""

    return ('Article:\n'
            '- HTML Path:   `%s`\n'
            '- Django Path: `%s`\n') % (self.html_, self.django_)


class Localizer(object):
  """Implements the HTML5Rocks article localization workflow.

  Given a root directory, Localizer looks for article files (defined as pretty
  much anything living directly under an `en` directory (which is very fragile
  and assumes we'll never have articles written first in languages other than
  English (which is probably accurate, but not something we should hard-code)))
  and converts the Django templates into HTML files that can be
  passed into a translation system (by commenting out all the Django bits).

  Localizer also goes in the other direction, converting localized HTML files
  into Django-template counterparts that can be rendered as part of HTML5Rocks.

  Attributes:
    root_: The root directory from which Localizer scans
    articles_: A list of Article objects found during a scan.
  """

  def __init__(self, root):
    """Constructs a Localizer object.

    Args:
      root: The root directory from which Localizer should scan.
    """
    self.root_ = root
    self.articles_ = []

  def Scan(self):
    """Scans the root directory for articles.

    Populates `self.articles_` with a list of Article objects.

    Returns:
        list of Article objects
    """
    self.articles_ = []
    for root, _, files in os.walk(Article.DJANGO_ROOT):
      for name in files:
        if not name == '.DS_Store' and re.search(r'\/en$', root):
          self.articles_.append(Article(django=os.path.join(root,
                                                            name)))
    return self.articles_

  def Htmlize(self):
    """Generates localizable HTML from Django templates."""

    print ('Generating Localizable HTML\n'
           '===========================\n')
    for article in self.articles_:
      article.GenerateHTML()

  def Djangoize(self):
    """Generates Django templates from localized HTML."""

    # TODO(mkwst): I should implement this function. :)
    print 'Not finished (read: started) yet. Come back later.'


def main():
  parser = optparse.OptionParser()
  parser.add_option('--generate_html', dest='generate_html',
                    default=False, action='store_true',
                    help='Generate HTML from Django templated articles.')
  parser.add_option('--generate_django', dest='generate_django',
                    default=False, action='store_true',
                    help=('Generate Django templates from localized '
                          'HTML articles.'))

  options = parser.parse_args()[0]
  if not options.generate_html or options.generate_django:
    parser.error('You must specify either `--generate_html`'
                 'or `--generate_django`.')

  l10n = Localizer(Article.DJANGO_ROOT)
  l10n.Scan()
  if options.generate_html:
    l10n.Htmlize()
  if options.generate_django:
    l10n.Djangoize()

if __name__ == '__main__':
  main()