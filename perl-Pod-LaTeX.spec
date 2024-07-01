#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Pod-LaTeX
Version  : 0.61
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/T/TJ/TJENNESS/Pod-LaTeX-0.61.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TJ/TJENNESS/Pod-LaTeX-0.61.tar.gz
Summary  : 'Convert Pod data to formatted Latex'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Pod-LaTeX-bin = %{version}-%{release}
Requires: perl-Pod-LaTeX-man = %{version}-%{release}
Requires: perl-Pod-LaTeX-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Pod::Find)
BuildRequires : perl(Pod::ParseUtils)
BuildRequires : perl(Pod::Parser)
BuildRequires : perl(Pod::Select)

%description
Pod::LaTeX - convert Pod to latex using Pod::Parser
This is version 0.60 of Pod::LaTeX. This module can be used to
convert pod data to latex. It uses the standard Pod::Parser module.
A pod2latex replacement command is provided. This can be installed over
the pod2latex command distributed with perl.

%package bin
Summary: bin components for the perl-Pod-LaTeX package.
Group: Binaries

%description bin
bin components for the perl-Pod-LaTeX package.


%package dev
Summary: dev components for the perl-Pod-LaTeX package.
Group: Development
Requires: perl-Pod-LaTeX-bin = %{version}-%{release}
Provides: perl-Pod-LaTeX-devel = %{version}-%{release}
Requires: perl-Pod-LaTeX = %{version}-%{release}

%description dev
dev components for the perl-Pod-LaTeX package.


%package man
Summary: man components for the perl-Pod-LaTeX package.
Group: Default

%description man
man components for the perl-Pod-LaTeX package.


%package perl
Summary: perl components for the perl-Pod-LaTeX package.
Group: Default
Requires: perl-Pod-LaTeX = %{version}-%{release}

%description perl
perl components for the perl-Pod-LaTeX package.


%prep
%setup -q -n Pod-LaTeX-0.61
cd %{_builddir}/Pod-LaTeX-0.61

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pod2latex

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Pod::LaTeX.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pod2latex.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
