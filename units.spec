Summary:	A utility for converting amounts from one unit to another

Name:		units
Version:	2.11
Release:	5
Source0:	ftp://ftp.gnu.org:21/pub/gnu/units/%{name}-%{version}.tar.gz
Url:		http://www.gnu.org/software/units/units.html
License:	GPLv2
Group:		Office
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel

%description
The â€˜units' program converts quantities expressed in various scales to
their equivalents in other scales. The â€˜units' program can handle
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
%makeinstall_std

%files
%{_bindir}/units*
%{_datadir}/units*
%{_infodir}/*
%{_mandir}/man1/units.1*



