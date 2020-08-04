Central Nahuatl: `apertium-nhn`
===============================================================================

This is an Apertium monolingual language package for nhn. What
you can use this language package for:

* Morphological analysis of nhn
* Morphological generation of nhn
* Part-of-speech tagging of nhn

Requirements
-------------------------------------------------------------------------------

You will need the following software installed:

* lttoolbox (>= 3.3.0)
* apertium (>= 3.3.0)
* vislcg3 (>= 0.9.9.10297)
* hfst (>= 3.8.2)

If this does not make any sense, we recommend you look at: www.apertium.org.

Compiling
-------------------------------------------------------------------------------

Given the requirements being installed, you should be able to just run:

```bash
$ ./configure
$ make
```

You can use `./autogen.sh` instead of `./configure` if you're compiling
from source.

If you're doing development, you don't have to install the data, you
can use it directly from this directory.

If you are installing this language package as a prerequisite for an
Apertium translation pair, then do (typically as root / with sudo):

```bash
$ make install
```

You can use a `--prefix` with `./configure` to install as a non-root user,
but make sure to use the same prefix when installing the translation
pair and any other language packages.

Testing
-------------------------------------------------------------------------------

If you are in the source directory after running make, the following
commands should work:

```console
$ echo "TODO: test sentence" | apertium -d . nhn-morph
TODO: test analysis result

$ echo "TODO: test sentence" | apertium -d . nhn-tagger
TODO: test tagger result
```

Files and data
-------------------------------------------------------------------------------

* [`apertium-nhn.nhn.lexc`](apertium-nhn.nhn.lexc) - Morphotactic dictionary
* [`apertium-nhn.nhn.twol`](apertium-nhn.nhn.twol) - Morphophonological rules
* [`apertium-nhn.nhn.rlx`](apertium-nhn.nhn.rlx) - Constraint Grammar disambiguation rules
* [`apertium-nhn.post-nhn.dix`](apertium-nhn.post-nhn.dix) - Post-generator
* [`nhn.prob`](nhn.prob) - Tagger model
* [`modes.xml`](modes.xml) - Translation modes

For more information
-------------------------------------------------------------------------------

* http://wiki.apertium.org/wiki/Installation
* http://wiki.apertium.org/wiki/apertium-nhn
* http://wiki.apertium.org/wiki/Using_an_lttoolbox_dictionary

Help and support
-------------------------------------------------------------------------------

If you need help using this language pair or data, you can contact:

* Mailing list: apertium-stuff@lists.sourceforge.net
* IRC: `#apertium` on irc.freenode.net (irc://irc.freenode.net/#apertium)

See also the file [`AUTHORS`](AUTHORS), included in this distribution.
