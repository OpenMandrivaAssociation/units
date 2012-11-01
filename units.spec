Summary:	A utility for converting amounts from one unit to another
Name:		units
Version:	2.01
Release:	1
Source0:	ftp://ftp.gnu.org/pub/gnu/units/%{name}-%{version}.tar.gz
Url:		http://www.gnu.org/software/units/units.html
License:	GPLv2
Group:		Office
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel

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

%check
make check

%install
%makeinstall_std

%files
%dir %{_datadir}/units
%{_bindir}/units
%{_datadir}/units/*.units
%{_infodir}/*
%{_mandir}/man1/units.1*
