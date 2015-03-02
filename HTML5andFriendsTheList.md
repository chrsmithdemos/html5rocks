# HTML5 and Friends, The List #
## A big big bulleted list of new features. ##

It's a common need to get a big list of all the stuff we think of when we think **new and shiny** these days. This list is for that.

Many things beyond just HTML5 the spec are included, for comprehensiveness.

### javascript APIs ###
  * Web Storage (localStorage, sessionStorage)
  * Web SQL Database
  * IndexedDB
  * app Cache
  * postMessage
  * Notifications
  * Geolocation
  * Dedicated Workers
  * Shared Workers
  * File/FileReader API
  * Drag and Drop
  * Web Sockets
  * History pushState
  * hashchange event
  * MessagePorts
  * CORS (cross origin resource sharing)
  * touch events
  * ECMAScript 5
    * getters, setters
    * array extras
  * canvas 2d
  * canvas 3d (webgl)
  * server-sent events (eventsource)
  * UndoManager
  * selectors api

### markup ###
  * audio tag
  * video tag
    * timed track (subtitles)
  * ruby tag
  * new semantic tags
    * section, nav, article, aside, hgroup, header, footer, address, figure, figcaption, time, code, var, samp, kbd, output
  * new behavior/application tags
    * progress, meter, details/summary, command, menu, keygen
  * webforms
    * new input types
      * telephone, search, url, e-mail, date, time, month, week, number, range, color
    * input autofocus, placeholder
    * form validation
    * multiple file upload
  * SVG
    * inline SVG
    * SMIL animation
  * MathML
  * aria roles and states
  * ping attribute
  * magic iframe
  * sandbox iframe
  * contenteditable
  * microdata, RDFa
  * link relations
    * alternate, archives, author, bookmark, external, help, icon, license, nofollow, noreferrer, pingback, prefetch, search, sidebar, tag, index, up, first, last, next, prev
  * data-attributes and dataset
  * classList API
  * link prefetching
  * device element (camera and microphone continuous input)
  * speech attribute
  * p2p connections
  * XHTML polyglot
  * standardized HTML5 parser




### style ###
  * css transitions
  * animations
  * 2d transforms
  * 3d transforms
  * Rounded Corners
  * text columns
  * web fonts, woff
  * Gradients
  * css3 selectors
  * flex box model
  * box shadows
  * pointer events
  * multiple backgrounds
  * background-[size|origin|clip]

### style, continued ###
  * reflections
  * overflow: ellipsis
  * Text Stroke
  * box-mask-image
  * CSS styling of new HTML5 input types


### other ###
  * O3D api for webgl
  * GPU acceleration of HTML, Canvas, SVG, and CSS3 Animations/Transitions/Transforms
  * getElementsByClassName
  * innerHTML, outerHTML, insertAdjacentHTML
  * script defer/async
  * audio data API




## Things Flash can do that HTML5 cannot ##

or at least what other people think.. (my thoughts in parens)

  * camera & microphone access (yeah. but, see work [is doing](ericisson.md)(https://labs.ericsson.com/blog/beyond-html5-conversational-voice-and-video-implemented-webkit-gtk) on this front)
  * audio processing (in works in audio data api (mozilla and webkit have two separate specs for this))
  * video/audio streaming (works, depending on codec. see fluomotion. not well documented: h264 streaming isnt possible in non-safari)
  * P2P (developing in device spec)
  * video with alpha channel ([workaround](canvas.md)(http://jakearchibald.com/scratch/alphavid/) from jake archibald)
  * sockets (websockets are widely deployed now)
  * flash media server (whats the value of it that we need?)
  * good IDE (yup, it's true. though most professional flash work is done in AS predominantly so the IDE is pretty moot)
  * better image/video compression (dubious but i dont know), usually smaller file size,
  * DRM (yup...... maybe. token-y expiration-y somethingsomething might be close)

original list was taken from [post](this.md)(http://www.kontain.com/fi/entries/99941/an-open-letter-to-the-html5-community/)