all : install

SDIR = $(HOME)/.reccon

install :
	@if test ! -d $(SDIR) ; then \
  		mkdir $(SDIR) ; \
   	fi ; \
   	cp reccon.py $(SDIR) ; \
   	cp reccon /usr/bin

remove :
	rm $(SDIR) -r ; \
	rm /usr/bin/reccon
