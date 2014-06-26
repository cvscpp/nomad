%define _prefix /usr

Name: nomad
Version: 3.6.1
Release: 1
Summary: NOMAD (Nonsmooth Optimization by Mesh Adaptive Direct Search)
License: LGPL
Group: science
Source: %{name}-%{version}.tar.gz
URL: https://www.gerad.ca/nomad/
Packager: Miroslav Shaltev <miroslav.shaltev@aei.mpg.de>
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: gcc-c++, autoconf, automake, doxygen, graphviz
#Requires: 
Prefix: %{_prefix}

%description
NOMAD (Nonsmooth Optimization by Mesh Adaptive Direct Search)

%prep
%setup -q

%build
./autogen.sh
%configure
make
%makeinstall

%clean
#[ ${RPM_BUILD_ROOT} != "/" ] && rm -Rf ${RPM_BUILD_ROOT}
#rm -Rf ${RPM_BUILD_DIR}/%{name}-%{version}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%{_includedir}/*
%{_libdir}/*
