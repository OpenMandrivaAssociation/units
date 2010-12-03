%define	name	units
%define version 1.88
%define release %mkrel 2

Summary:	A utility for converting amounts from one unit to another
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.gnu.org/pub/gnu/units/%{name}-%{version}.tar.gz
Url:		http://www.gnu.org/software/units/units.html
License:	GPLv2
Group:		Office
BuildRequires:	ncurses-devel readline-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The ‘units' program converts quantities expressed in various scales to
their equivalents in other scales. The ‘units' program can handle
multiplicative scale changes as well as nonlinear conversions such as
Fahrenheit to Celsius. Temperature and other nonlinear conversions
are handled using a functional notation.

%prep
%setup -q

%build
%configure2_5x
%make
make check

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/units
%{_datadir}/units.dat
%{_infodir}/*
%{_mandir}/man1/units.1*
