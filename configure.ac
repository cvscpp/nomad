AC_INIT(nomad, 3.6.1, miroslav.shaltev@shaltev.de)
AC_PREREQ([2.69])
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
AC_CONFIG_FILES([Makefile src/Makefile nomad.pc nomadmpi.pc])
AC_OUTPUT
