# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name dbus

%bcond_with tests

# no useful debuginfo for Haskell packages without C sources
%global debug_package %{nil}

Name:           ghc-%{pkg_name}
Version:        0.10.7
Release:        3%{?dist}
Summary:        Haskell client library for the D-Bus IPC system

License:        GPLv3+
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-libxml-sax-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-xml-types-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-chell-devel
BuildRequires:  ghc-chell-quickcheck-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-process-devel
%endif
# End cabal-rpm deps

%description
D-Bus is a simple, message-based protocol for inter-process communication,
which allows applications to interact with other parts of the machine and the
user's session using remote procedure calls.

This library is an implementation of the D-Bus protocol in Haskell. It can be
used to add D-Bus support to Haskell applications, without the awkward
interfaces common to foreign bindings.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%check
%if %{with tests}
%cabal test
%endif


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc license.txt


%files devel -f %{name}-devel.files
%doc examples


%changelog
* Tue Jun 10 2014 Jens Petersen <petersen@redhat.com> - 0.10.7-3
- update to cblrpm-0.8.11

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Dan Callaghan <dcallagh@redhat.com> - 0.10.7-1
- upstream release 0.10.7

* Thu Feb 20 2014 Dan Callaghan <dcallagh@redhat.com> - 0.10.6-2
- rebuilt for updated ghc-libxml-sax

* Wed Feb 19 2014 Dan Callaghan <dcallagh@redhat.com> - 0.10.6-1
- upstream release 0.10.6 (again no effective changes, just more relaxing of 
  version requirements)

* Mon Feb 03 2014 Dan Callaghan <dcallagh@redhat.com> - 0.10.5-1
- upstream release 0.10.5 (no effective changes, upstream just relaxed the 
  version requirement for cereal)

* Wed Jul 17 2013 Dan Callaghan <dcallagh@redhat.com> - 0.10.4-2
- update for new guidelines (cabal-rpm 0.8.2)

* Mon May 13 2013 Dan Callaghan <dcallagh@redhat.com> - 0.10.4-1
- initial version
