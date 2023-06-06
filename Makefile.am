###############################################################################
## Makefile for apertium-nhi
###############################################################################

LANG1=nhi
BASENAME=apertium-$(LANG1)
VAR1=SEP

TARGETS_COMMON =			\
	$(LANG1).automorf.hfst		\
	$(LANG1).automorf.bin		\
	$(LANG1).automorf.att.gz	\
	$(LANG1).autogen.hfst		\
	$(LANG1).autophon.hfst		\
	$(LANG1).autophon_$(VAR1).hfst		\
	$(LANG1)-$(LANG1)_$(VAR1).autoconv.hfst \
	$(LANG1).autogen.bin		\
	$(LANG1).autogen.att.gz		\
	$(LANG1).autoseg.hfst		\
	$(LANG1).autoseg.bin		\
	$(LANG1).prob		\
	$(LANG1).rlx.bin

TARGETS_INTERMEDIATE = $(LANG1).mor.hfst $(LANG1).seg.hfst $(LANG1).gen.hfst $(LANG1).phon.hfst

# This include defines goals for install-modes, .deps/.d and .mode files:
@ap_include@

###############################################################################

# nimahtlapaltzin:<s_sg1>mahtlapal<n><dim>
.deps/nhi.mor.hfst: .deps/nhi.gen.hfst .deps/nhi.mor.twol.hfst
	hfst-compose-intersect -1 .deps/nhi.gen.hfst -2 .deps/nhi.mor.twol.hfst | hfst-minimise | hfst-invert -o $@

# amatl<n><dim><pl>:ama>tzi>tzin
.deps/nhi.gen.hfst: .deps/nhi.RL.lexc.hfst .deps/nhi.twol.hfst
	hfst-compose-intersect -1 .deps/nhi.RL.lexc.hfst -2 .deps/nhi.twol.hfst | hfst-minimise  -o $@

.deps/nhi.twol.hfst: apertium-nhi.nhi.twol
	hfst-twolc $< -o $@

# <px2sg>metztli<n><pl>:m{o}>metz>huan
.deps/nhi.lexc.hfst: apertium-nhi.nhi.lexc .deps/.d
	hfst-lexc -A --Werror $< -o $@

.deps/nhi.RL.lexc: apertium-nhi.nhi.lexc .deps/.d
	cat $< | grep -v "Dir/LR" > $@

.deps/nhi.RL.lexc.hfst: .deps/nhi.RL.lexc .deps/.d
	hfst-lexc -A --Werror $< -o $@

.deps/nhi.mor.twol.hfst: apertium-nhi.nhi.mor.twol
	hfst-twolc apertium-nhi.nhi.mor.twol -o .deps/nhi.mor.twol.hfst

# notipehuan:no>tipe>huan
.deps/nhi.seg.hfst: .deps/nhi.mor.hfst .deps/nhi.gen.hfst
	hfst-compose -F -1 .deps/nhi.mor.hfst -2 .deps/nhi.gen.hfst -o .deps/nhi.seg.hfst 

.deps/nhi.phon.hfst: apertium-nhi.nhi.phon
	hfst-lexc apertium-nhi.nhi.phon -o $@

.deps/nhi.phon_$(VAR1).hfst: apertium-nhi.nhi_$(VAR1).phon
	hfst-lexc apertium-nhi.nhi_$(VAR1).phon -o $@

.deps/nhi.spellrelax.hfst: apertium-nhi.nhi.spellrelax 
	hfst-regexp2fst -S -o $@ < $<

.deps/nhi-nhi_$(VAR1).phon.hfst: .deps/nhi.phon.hfst .deps/nhi.phon_$(VAR1).hfst
	hfst-invert .deps/nhi.phon_$(VAR1).hfst | hfst-compose -F -1 .deps/nhi.phon.hfst -2 - -o $@

$(LANG1)-$(LANG1)_$(VAR1).autoconv.hfst: .deps/nhi-nhi_$(VAR1).phon.hfst
	hfst-fst2fst -w $< -o $@

$(LANG1).autophon.hfst: .deps/nhi.phon.hfst
	hfst-fst2fst -w $< -o $@

$(LANG1).autophon_$(VAR1).hfst: .deps/nhi.phon_$(VAR1).hfst
	hfst-fst2fst -w $< -o $@

$(LANG1).automorf.hfst: .deps/nhi.mor.hfst .deps/nhi.spellrelax.hfst
	hfst-invert $< |  hfst-compose -F -1 - -2 .deps/nhi.spellrelax.hfst  | hfst-invert | hfst-fst2fst -w -o $@

$(LANG1).autogen.hfst: .deps/nhi.gen.hfst
	hfst-compose-intersect -1 .deps/nhi.gen.hfst -2 .deps/nhi.mor.twol.hfst | hfst-fst2fst -w -o $@

$(LANG1).autoseg.hfst: .deps/nhi.seg.hfst 
	hfst-fst2fst -w $< -o $@

$(LANG1).rlx.bin: apertium-nhi.nhi.rlx
	cg-comp $< $@

$(LANG1).autogen.att.gz: .deps/$(LANG1).gen.hfst
	hfst-compose-intersect -1 .deps/nhi.gen.hfst -2 .deps/nhi.mor.twol.hfst | hfst-eliminate-flags  | hfst-fst2txt | gzip -9 -c > $@ 

$(LANG1).automorf.att.gz: .deps/$(LANG1).mor.hfst .deps/nhi.spellrelax.hfst
	hfst-invert $< |  hfst-compose -F -1 - -2 .deps/nhi.spellrelax.hfst  | hfst-eliminate-flags | hfst-invert | hfst-fst2txt | gzip -9 -c > $@

$(LANG1).autoseg.att.gz: .deps/$(LANG1).seg.hfst
	hfst-fst2txt $< | gzip -9 -c > $@

$(LANG1).autogen.bin: $(LANG1).autogen.att.gz .deps/.d
	zcat < $< > .deps/$(LANG1).autogen.att
	lt-comp lr .deps/$(LANG1).autogen.att $@

$(LANG1).automorf.bin: $(LANG1).automorf.att.gz .deps/.d
	zcat < $< > .deps/$(LANG1).automorf.att
	lt-comp lr .deps/$(LANG1).automorf.att $@

$(LANG1).autoseg.bin: $(LANG1).autoseg.att.gz .deps/.d
	zcat < $< > .deps/$(LANG1).autoseg.att
	lt-comp lr .deps/$(LANG1).autoseg.att $@

$(LANG1).prob: $(BASENAME).$(LANG1).tagged $(LANG1).rlx.bin
	cat $< | cg-proc $(LANG1).rlx.bin | apertium-tagger -s 0 -u 2 $@ /dev/stdin

###############################################################################
## Distribution
###############################################################################

EXTRA_DIST=$(BASENAME).$(LANG1).lexc		\
		$(BASENAME).$(LANG1).twol	\
		$(BASENAME).$(LANG1).phon \
		$(BASENAME).$(LANG1).spellrelax \
		$(BASENAME).$(LANG1).rlx	\
		modes.xml

###############################################################################
## Installation stuff
###############################################################################
#
#   apertium_nhi_dir: This is where the compiled binaries go
#   apertium_nhi_srcdir: This is where the source files go

apertium_nhidir=$(prefix)/share/apertium/$(BASENAME)/
apertium_nhi_srcdir=$(prefix)/share/apertium/$(BASENAME)/

EXTRA_TARGETS=

if HAVE_HFSTOSPELL
EXTRA_TARGETS += $(LANG1).zhfst
endif # HAVE_HFSTOSPELL

apertium_nhi_DATA=$(TARGETS_COMMON) $(EXTRA_TARGETS) 

pkgconfigdir = $(prefix)/share/pkgconfig
pkgconfig_DATA = $(BASENAME).pc

noinst_DATA=modes/$(LANG1)-morph.mode

install-data-local: install-modes
	$(INSTALL_DATA) $(BASENAME).$(LANG1).lexc $(DESTDIR)$(apertium_nhi_srcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG1).twol $(DESTDIR)$(apertium_nhi_srcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG1).rlx $(DESTDIR)$(apertium_nhi_srcdir)


###############################################################################
## Cleanup
###############################################################################

CLEANFILES = $(TARGETS_COMMON) $(TARGETS_INTERMEDIATE)
clean-local:
	-rm -rf .deps modes

###############################################################################

test: all
	apertium-regtest test
