Step-by-step guide for third-party developers to contribute to html5rocks.com. Before you draft the article, read the [writing tips](http://code.google.com/p/html5rocks/wiki/WritingTips).

# Before you start #

HTML5Rocks runs on Google App Engine (Python). Before you check out the code, download
the [App Engine Python SDK](http://code.google.com/appengine/downloads.html#Google_App_Engine_SDK_for_Python). The SDK is not required, but highly recommended. You'll want to run a local development server and preview your changes before submitting a tutorial, sample, or patch.

Our code repository is Git. If you do not have it, [download and install it](http://git-scm.com/download).

# Getting the code #

The entirety of HTML5Rocks ([www](http://www.html5rocks.com/), [studio](http://studio.html5rocks.com/), [slides](http://slides.html5rocks.com/), [playground](http://playground.html5rocks.com/), [updates](http://updates.html5rocks.com/)) is located here.

Each sub-domain points to a separate [Google App Engine](http://code.google.com/appengine/downloads.html) (Python) application with a corresponding sub-directory in the src tree:

| **Sub-domain** | **App ID** | **src** |
|:---------------|:-----------|:--------|
| www.html5rocks.com | http://html5rocks.appspot.com | [/www.html5rocks.com](http://code.google.com/p/html5rocks/source/browse/#git%2Fwww.html5rocks.com) |
| studio.html5rocks.com | http://html5playbook.appspot.com | [/studio.html5rocks.com](http://code.google.com/p/html5rocks/source/browse/#git%2Fstudio.html5rocks.com) |
| slides.html5rocks.com | http://html5slides.appspot.com | [/slides.html5rocks.com](http://code.google.com/p/html5rocks/source/browse/#git%2Fslides.html5rocks.com) |
| playground.html5rocks.com | http://html5playground.appspot.com | [/playground.html5rocks.com](http://code.google.com/p/html5rocks/source/browse/#git%2Fplayground.html5rocks.com) |
| updates.html5rocks.com | http://updaterocker.appspot.com | [/updates.html5rocks.com](http://code.google.com/p/html5rocks/source/browse/#git%2Fupdates.html5rocks.com) |

To checkout the src, run the following command:
```
git clone https://code.google.com/p/html5rocks/
```

# Contributing: submitting patches and tutorials #

## Submitting a code patch, studio/playground sample ##

### Contributor License Agreements ###

This section only applies if you are submitting a patch for us. The CLA mentioned below does not apply if you are giving us a brand new article or tutorial.

We'd love to accept your code patches! However, before we can take them, we have to jump a couple of legal hurdles.

Please fill out either the individual or corporate Contributor License Agreement.


  * If you are an individual writing original source code and you're sure you own the intellectual property, then you'll need to sign an [individual CLA](http://code.google.com/legal/individual-cla-v1.0.html).
  * If you work for a company that wants to allow you to contribute your work to HTML5Rocks.com, then you'll need to sign a [corporate CLA](http://code.google.com/legal/corporate-cla-v1.0.html).

Follow either of the two links above to access the appropriate CLA and instructions for how to sign and return it. Once we receive it, we'll add you to the official list of contributors and be able to accept your patches.

  1. Sign the contributors license agreement above.
  1. Decide which code you want to submit. A submission should be a set of changes that addresses one issue in the [HTML5Rocks issue tracker](http://code.google.com/p/html5rocks/issues/list). Please don't mix more than one logical change per submittal, because it makes the history hard to follow. If you want to make a change (e.g. add a sample or feature) that doesn't have a corresponding issue in the issue tracker, please create one.
  1. **Submitting**: When you are ready to submit, attach a diff of your patch (by running ` git diff /path/to/file `) to the issue.

## Writing a tutorial / case study ##

  * Our articles and case studies are licensed under Creative Commons Attribution 3.0 License. Be sure you are OK with that.
  * If one doesn't already exist, [Create a new issue](http://code.google.com/p/html5rocks/issues/entry) in the issue tracker so others can follow/comment on progress.

Now choose your adventure:

### Semi-automated process ###

The main project folder contains a script, ` www.html5rocks.com/scripts/generate_tutorial.py ` to automate the creation of new tutorials/case studies.  It does this by:

  1. Creating the directory and file you pass in via the command line. The article's templates is taken from ` www.html5rocks.com/content/tutorials/tutorial.html.template `.
  1. Prompting you for various information (article title, name, tags, etc.)
  1. Adding your article to the ` /tutorials/index.html `

To create a new tutorial run:
```
  cd www.html5rocks.com/
  python scripts/generate_tutorial.py --output /file/filesystem/index.html
```

where the ` --output ` parameter is of the form: ` /<api_name>/<tutorial_name>/index.html `

To create a new case study  run:
```
  cd www.html5rocks.com/scripts
  python generate_tutorial.py --output /casestudies/company_articlename.html
```

To create a mobile article:
```
  cd www.html5rocks.com/scripts
  python generate_tutorial.py --output /mobile/articlename.html
```

If you have an existing .txt file containing article content (or a Google Doc exported to .txt), the script can take an ` --input ` parameter that will populate the empty article with your content:

```
  cd www.html5rocks.com/scripts
  python generate_tutorial.py --output /casestudies/company_articlename.html --input ~/path/to/content.txt
```

**Note**: You'll need to still clean up the generated HTML in ` company_articlename.html `.

This script tries to mimic the manual process (below) but isn't perfect. Some HTML clean up/formatting will be necessary. For example, you still need to replace the ` ___COMPAT_TEST___ ` in your generated article with an appropriate Modernizr (or raw JS) test that makes sense for your article, add a summary description in `/tutorials/index.html', and other other loose ends.

If you are a new author, add yourself to ` www.html5rocks.com/profiles.yaml `. We'll also need a ` .png ` photo of you for the [profiles page](http://html5rocks.com/profiles).

### Manual process ###

  1. If you are a new author, add yourself to ` www.html5rocks.com/profiles.yaml `. We'll also need a ` .png ` photo of you for the [profiles page](http://html5rocks.com/profiles).
  1. Add a new directory for your tutorial/case study. Both are located in http://code.google.com/p/html5rocks/source/browse/#git%2Fwww.html5rocks.com%2Fcontent%2Ftutorials` <api_name>/<tutorial_name> ` and are hosted under the live site at http://www.html5rocks.com/tutorials/.  Please use good judgement when naming a new directory/tutorial.  HTML files will automatically be parsed by the templating system, which is Django based. See [Django template tags and filters](http://docs.djangoproject.com/en/1.0/ref/templates/builtins/) for more information.
  1. If you're writing a case study, add your article under ` /content/tutorials/casestudies/ ` instead. The naming convention is ` company_articlename.html `.
  1. Copy ` www.html5rocks.com/content/tutorials/tutorial.html.template ` to your directory and replace its holder variable ` ___COMPAT_TEST___ ` your our feature detect. Also remove the html comment at the top, otherwise you'll get parsing errors.
  1. Add your article to the [/tutorials.yaml](http://code.google.com/p/html5rocks/source/browse/www.html5rocks.com/tutorials.yaml) file.

Modify a previous entry to match the details of your tutorial. When possible, try to use existent tags. If you're writing a case study, be sure to tag the article with the ` type:casestudy ` tag.

## Writing/Augmenting a feature page ##

  1. URL like ` http://www.html5rocks.com/features/offline ` uses a file in [content/features/offline.html](http://code.google.com/p/html5rocks/source/browse/www.html5rocks.com/content/features/offline.html)
  1. New files should be created using what's in ` feature_empty.html ` of that same directory. It has a useful markup skeleton that'll save you time.

**Submitting**: When you are ready to submit, attach a diff of your patch (by running ` git diff /path/to/file `) to the issue.

## i18n ##

A few things to note about internationalization:

  1. All templates need to include the ` i18n ` library by adding ` {% include 'i18n' %} ` as early as possible.
  1. UI strings must be wrapped with ` {% blocktrans %} ` or ` {% trans ... %} ` tags.  These are well explained in http://docs.djangoproject.com/en/1.2/topics/i18n/.
  1. Articles live one subdirectory deeper to encode their locale, in http://code.google.com/p/html5rocks/source/browse/www.html5rocks.com/content/tutorials/3d/css/en/index.html?r=v4 for example.
  1. Similarly, all case studies live in http://code.google.com/p/html5rocks/source/browse/www.html5rocks.com/content/tutorials/casestudies/en