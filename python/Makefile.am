# Name of the cpp source file
BUILT_SOURCES = nomad_wrap.cxx
# Name of the swig source file
SWIG_SOURCES = nomad.i
# Python source files that will be install in prefix/lib/name_of_your_python_interpreter/site-packages/name_of_your_project
pkgpython_PYTHON = nomad.py
pkgpyexec_LTLIBRARIES = _nomad.la
_nomad_la_SOURCES = nomad_wrap.cxx $(SWIG_SOURCES)
_nomad_la_CPPFLAGS = $(AX_SWIG_PYTHON_CPPFLAGS) -I$(top_srcdir)/src -I/usr/include/python@PYTHON_VERSION@ -lpython@PYTHON_VERSION@
_nomad_la_LDFLAGS = -module

nomad_wrap.cxx: $(SWIG_SOURCES)
	$(SWIG) $(AX_SWIG_PYTHON_OPT) -I$(top_srcdir)/src -I/usr/include/python@PYTHON_VERSION@ -o $@ $<
