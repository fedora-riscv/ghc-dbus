# https://fedoraproject.org/wiki/Packaging:Haskell
# https://fedoraproject.org/wiki/PackagingDrafts/Haskell

%global pkg_name dbus

%global common_summary A client library for the D-Bus IPC system

%global common_description D-Bus is a simple, message-based protocol for inter-process \
communication, which allows applications to interact with other parts of \
the machine and the user's session using remote procedure calls. \
\
This library is an implementation of the D-Bus protocol in Haskell. It \
can be used to add D-Bus support to Haskell applications, without the \
awkward interfaces common to foreign bindings.

Name:           ghc-%{pkg_name}
Version:        0.10.4
Release:        1%{?dist}
Summary:        %{common_summary}

License:        GPLv3+
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros

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

%description
%{common_description}

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%ghc_devel_package

%ghc_devel_description

%ghc_devel_post_postun

%ghc_files license.txt
%doc examples

%changelog
* Mon May 13 2013 Dan Callaghan <dcallagh@redhat.com> - 0.10.4-1
- initial version
