Summary:	A utility for converting amounts from one unit to another
Name:		units
Version:	1.88
Release:	6
Source0:	ftp://ftp.gnu.org/pub/gnu/units/%{name}-%{version}.tar.gz
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
%makeinstall

%files
%defattr(-,root,root)
%{_bindir}/units
%{_datadir}/units.dat
%{_infodir}/*
%{_mandir}/man1/units.1*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.88-3mdv2011.0
+ Revision: 670746
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.88-2mdv2011.0
+ Revision: 608110
- rebuild

* Tue Mar 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.88-1mdv2010.1
+ Revision: 517168
- fix license to GPLv2
- use %%configure2_5x
- update to 1.88

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.87-5mdv2010.0
+ Revision: 427480
- rebuild

* Wed Feb 25 2009 Thierry Vignaud <tv@mandriva.org> 1.87-4mdv2009.1
+ Revision: 344816
- rebuild for new libreadline

* Wed Feb 25 2009 Thierry Vignaud <tv@mandriva.org> 1.87-3mdv2009.1
+ Revision: 344798
- rebuild for new libreadline

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.87-2mdv2009.0
+ Revision: 225900
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 12 2007 Emmanuel Andry <eandry@mandriva.org> 1.87-1mdv2008.1
+ Revision: 118766
- New version


* Wed Mar 14 2007 Claudio Matsuoka <claudio@mandriva.com> 1.86-2mdv2007.1
+ Revision: 143815
- Fixed description to match actual package features (closes: #26243)

* Thu Jan 18 2007 Gustavo De Nardin <gustavodn@mandriva.com> 1.86-1mdv2007.1
+ Revision: 110471
- new version 1.86
- removed DESTDIR patch, made unnecessary by upstream changes
- removed unneeded and old gpm-devel from BuildRequires

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.85-2mdk
- Rebuild

* Wed Jun 01 2005 Götz Waschk <waschk@mandriva.org> 1.85-1mdk
- drop patches 2,3
- New release 1.85

* Thu Jan 20 2005 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.80-4mdk
- rebuild for new readline
- fix summary-ended-with-dot

* Wed Jun 30 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.80-3mdk
- fix buildrequires
- P3 from fedora:
	o fix parsecs #96982
- cosmetics

