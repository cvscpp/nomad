AC_INIT(nomad, 3.6.1, miroslav.shaltev@shaltev.de)
AC_PREREQ([2.67])
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_AWK
AC_PROG_CXX
AC_PROG_INSTALL
AC_PROG_MAKE_SET
AC_PROG_RANLIB

AM_MISSING_PROG(ACLOCAL, aclocal, $missing_dir)
AM_MISSING_PROG(AUTOMAKE, automake, $missing_dir)


AM_INIT_AUTOMAKE

AC_CHECK_LIB([m], [sin])
AC_CHECK_HEADERS([limits.h stdlib.h unistd.h])

# Checks for library functions.
AC_FUNC_ERROR_AT_LINE
AC_CHECK_FUNCS([floor pow sqrt])

AC_CHECK_PROGS([DOXYGEN],[doxygen])

if test "x$DOXYGEN" = "xtrue"; then
	AC_MSG_WARN([Doxygen not found - continuing without Doxygen support])
fi

AC_CHECK_PROGS([DOT],[dot])

if test "x$DOT" = "xtrue"; then
	AC_MSG_WARN([dot not found - install graphviz for more fancier documentation])
fi


AM_CONDITIONAL([HAVE_DOXYGEN],[test -n "$DOXYGEN"])
AM_COND_IF([HAVE_DOXYGEN], [AC_CONFIG_FILES([docs/Doxyfile])])


NOMAD_ENABLE_MPI
MPI_ENABLE_VAL="`eval test x$mpi = xtrue && echo "ENABLED"||echo "DISABLED"`"
AM_CONDITIONAL([MPI_ENABLED],[test "$MPI_ENABLE_VAL" = "ENABLED"])


AC_PROG_CXX
AC_LANG_PUSH([C++])
if test "x$mpi" = "xtrue"; then
  LX_FIND_MPI([mpi=true],[mpi=false])
fi
NOMAD_ENABLE_MODULE([MPI],[mpi])

AC_PROG_CPP
AC_CONFIG_FILES([Makefile src/Makefile docs/Makefile nomad.pc nomadmpi.pc])
AC_OUTPUT
