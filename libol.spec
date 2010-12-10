%define	name	libol
%define	version	0.3.18
%define	release	%mkrel 5

%define major	0
%define libname	%mklibname ol %{major}

Summary:	Nonblocking I/O and OO library
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.balabit.hu/downloads/libol/0.3/
Source:     http://www.balabit.hu/downloads/libol/0.3/%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Nonblocking I/O and OO library. It is needed to build syslog-ng,
the new generation syslog.

%package -n	%{libname}
Group:		Development/Other
License:	GPL
Summary:	Nonblocking I/O and OO library. This package contains the libraries

%description -n	%{libname}
Nonblocking I/O and OO library. It is needed to build syslog-ng,
the new generation syslog.

%package -n	%{libname}-devel
Group:		Development/Other
License:	GPL
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
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}%{_bindir}/make_class

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*so.*

%files -n %{libname}-devel
%defattr (-,root,root)
%{_bindir}/*
%{_includedir}/libol/
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/libol.so


