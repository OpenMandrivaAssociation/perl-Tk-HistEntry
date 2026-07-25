%define upstream_name    Tk-HistEntry
%define upstream_version 0.46

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	An entry widget with history capability
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/eserte/tk-histentry
Source0:	https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Tk-HistEntry-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Tk)
BuildRequires:	x11-server-xvfb

BuildArch:	noarch

%description
'Tk::HistEntry' defines entry widgets with history capabilities. The
widgets come in two flavours:

* 'HistEntry' (in package 'Tk::HistEntry::Browse') - with associated
  browse entry

* 'SimpleHistEntry' (in package 'Tk::HistEntry::Simple') - plain widget
  without browse entry

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
xvfb-run %make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.430.0-2mdv2011.0
+ Revision: 658895
- rebuild for updated spec-helper

* Tue May 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-1mdv2011.0
+ Revision: 545248
- import perl-Tk-HistEntry


* Tue May 18 2010 cpan2dist 0.43-1mdv
- initial mdv release, generated with cpan2dist
