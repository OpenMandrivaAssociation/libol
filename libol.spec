%define major	0
%define libname	%mklibname ol %{major}

Summary:	Nonblocking I/O and OO library
Name:		libol
Version:	0.3.18
Release:	7
License:	GPL
Group:		System/Libraries
URL:		https://www.balabit.hu/downloads/libol/0.3/
Source:     http://www.balabit.hu/downloads/libol/0.3/%{name}-%{version}.tar.bz2

%description
Nonblocking I/O and OO library. It is needed to build syslog-ng,
the new generation syslog.

%package -n	%{libname}
Group:		Development/Other
Summary:	Nonblocking I/O and OO library. This package contains the libraries

%description -n	%{libname}
Nonblocking I/O and OO library. It is needed to build syslog-ng,
the new generation syslog.

%package -n	%{libname}-devel
Group:		Development/Other
Summary:	Nonblocking I/O and OO library. Devel files
Requires:	%{libname} = %{version}-%{release}
Provides:	libol-devel = %{version}-%{release}

%description -n	%{libname}-devel
Nonblockin I/O and OO library. It is needed to build syslog-ng,
the new generation syslog.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall
rm -f %{buildroot}%{_bindir}/make_class

%files -n %{libname}
%{_libdir}/*so.%{major}*

%files -n %{libname}-devel
%{_bindir}/*
%{_includedir}/libol/
%{_libdir}/*.a
%{_libdir}/libol.so

%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.18-5mdv2011.0
+ Revision: 620168
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3.18-4mdv2010.0
+ Revision: 429817
- rebuild

* Sat Jul 26 2008 Thierry Vignaud <tv@mandriva.org> 0.3.18-3mdv2009.0
+ Revision: 250309
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.3.18-1mdv2008.1
+ Revision: 136557
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.18-1mdv2007.1
+ Revision: 142379
- new version

* Wed Jul 13 2005 Herton Ronaldo Krzesinski <herton@mandriva.com> 0.3.16-2mdk
- Fix some things pointed out by rpmlint.

* Sat Jul 09 2005 Herton Ronaldo Krzesinski <herton@mandriva.com> 0.3.16-1mdk
- New upstream version: 0.3.16.

* Thu Sep 23 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.14-2mdk
- get rid of scsh dependency by dropping %%{_bindir}/make_class

* Tue Sep 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.14-1mdk
- 0.3.14
- cleanups

