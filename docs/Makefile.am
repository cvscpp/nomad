if HAVE_DOXYGEN
directory = $(top_srcdir)/docs

$(directory)/html: doxyfile.stamp

doxyfile.stamp:
	$(DOXYGEN) Doxyfile
	echo Timestamp > doxyfile.stamp

CLEANFILES = doxyfile.stamp

docsdir = $(datadir)/docs/@PACKAGE@/html
docs_DATA = $(directory)/html/*.html \
	$(directory)/html/*.png \
	$(directory)/html/*.css \
	$(directory)/html/*.jpg \
	$(directory)/html/*.m* \
	$(directory)/html/*.js

sdocsdir = $(datadir)/docs/@PACKAGE@/html/search
sdocs_DATA = $(directory)/html/search/*.html \
	$(directory)/html/search/*.png \
	$(directory)/html/search/*.css \
	$(directory)/html/search/*.js


all-local: doxyfile.stamp
clean-local:
	rm -rf $(top_srcdir)/docs/html
endif