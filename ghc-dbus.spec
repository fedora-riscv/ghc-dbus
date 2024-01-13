# generated by cabal-rpm-2.1.2
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name dbus
%global pkgver %{pkg_name}-%{version}

# requires network
%ifnarch riscv64
%bcond_with tests
%endif

Name:           ghc-%{pkg_name}
Version:        1.2.29
Release:        %autorelease -e 0.rv64
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
%autopatch -p1
# End cabal-rpm setup


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
%autochangelog
