**audiolib.js** - https://github.com/jussi-kalliokoski/audiolib.js
> - normalizing library between the Mozilla Audio Data API and the Webkit Web Audio API
> - has effects, synthesis, envelopes, recording and exporting

**XAudioJS** - https://github.com/grantgalitz/XAudioJS
> - shim for basic audio handling between the two apis
> - grant just ported GameBoyColor to HTML5 and uses the audio apis in his port:
> > https://github.com/grantgalitz/GameBoy-Online

**dynamicaudio.js** - https://github.com/bfirsh/dynamicaudio.js/

> - Mozilla Audio Data API polyfill via flash.
> - also an author of a nintendo emulator: http://benfirshman.com/projects/jsnes/

**audionode** - https://github.com/corbanbrook/audionode.js
> - polyfill of the Webkit Web Audio API using the moz audio data api.
> - done back in july so it may not still be compatible.
> - corban is one of the guys on the mozilla audio/webgl demo team

**audiodata** - https://github.com/notmasteryet/audiodata
> - abstraction layer for mozilla audio data api

**Music.js** - http://www.gregjopa.com/2011/05/calculate-note-frequencies-in-javascript-with-music-js/
> - note and chord synthesis for both FF and WebKit APIs
and then also..


https://beatdetektor.svn.sourceforge.net/svnroot/beatdetektor/trunk/core/js/beatdetektor.js detects beats... and uses...

https://github.com/corbanbrook/dsp.js for its DSP action, and can work with both APIs