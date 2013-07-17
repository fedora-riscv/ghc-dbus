# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name dbus

Name:           ghc-%{pkg_name}
Version:        0.10.4
Release:        2%{?dist}
Summary:        Haskell client library for the D-Bus IPC system

License:        GPLv3+
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz

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
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the development files for the Haskell %{pkg_name} library.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc license.txt


%files devel -f %{name}-devel.files
%doc examples


%changelog
* Wed Jul 17 2013 Dan Callaghan <dcallagh@redhat.com> - 0.10.4-2
- update for new guidelines (cabal-rpm 0.8.2)

* Mon May 13 2013 Dan Callaghan <dcallagh@redhat.com> - 0.10.4-1
- initial version
