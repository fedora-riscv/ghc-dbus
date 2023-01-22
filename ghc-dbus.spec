# generated by cabal-rpm-2.1.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name dbus
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        1.2.27
Release:        1%{?dist}
Summary:        A client library for the D-Bus IPC system

License:        Apache-2.0
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources
Patch0:         dbus-disable-test_ListenUnix_InvalidBind.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-th-lift-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-types-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cereal-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-lens-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-th-lift-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-xml-conduit-prof
BuildRequires:  ghc-xml-types-prof
%endif
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif
# End cabal-rpm deps
%if %{with tests}
BuildRequires:  dbus-daemon
%endif

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
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup
%patch0 -p1 -b .orig


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%check
%if %{with tests}
%cabal_test
%endif


%files -f %{name}.files
# Begin cabal-rpm files:
%license license.txt
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc examples


%if %{with haddock}
%files doc -f %{name}-doc.files
%license license.txt
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sun Jan 22 2023 Jens Petersen <petersen@redhat.com> - 1.2.27-1
- https://hackage.haskell.org/package/dbus-1.2.27/changelog
- refresh to cabal-rpm-2.1.0 with SPDX migration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Jens Petersen <petersen@redhat.com> - 1.2.17-3
- disable test_ListenUnix_InvalidBind (failing with ghc-8.10.7 in mock)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug  5 2021 Jens Petersen <petersen@redhat.com> - 1.2.17-1
- update to 1.2.17

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jens Petersen <petersen@redhat.com> - 1.2.16-1
- update to 1.2.16

* Sun Jun 07 2020 Jens Petersen <petersen@redhat.com> - 1.2.15.1-1
- update to 1.2.15.1

* Thu Feb 20 2020 Jens Petersen <petersen@redhat.com> - 1.2.7-3
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 1.2.7-1
- update to 1.2.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar  5 2019 Jens Petersen <petersen@redhat.com> - 1.1.1-1
- update to 1.0.1

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.10.15-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.10.15-1
- update to 0.10.15

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.10.14-1
- update to 0.10.14

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 0.10.12-3
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.10.12-1
- Update to 0.10.12 (#1299445)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.10.10-3
- Rebuild (aarch64 vector hashes)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 01 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.10.10-1
- Update to 0.10.10 (#1181481)

* Tue Jan 27 2015 Jens Petersen <petersen@fedoraproject.org> - 0.10.8-2
- cblrpm refresh

* Fri Aug 22 2014 Dan Callaghan <dcallagh@redhat.com> - 0.10.8-1
- upstream release 0.10.8 (just test fixes and dependency relaxations)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

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
