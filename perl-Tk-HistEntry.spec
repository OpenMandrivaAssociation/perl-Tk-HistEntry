%define upstream_name    Tk-HistEntry
%define upstream_version 0.43

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    An entry widget with history capability
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Tk)
BuildRequires: x11-server-xvfb

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
xvfb-run %make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


