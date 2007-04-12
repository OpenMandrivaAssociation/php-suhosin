%define modname suhosin
%define soname %{modname}.so
%define inifile Z99_%{modname}.ini

Summary:	Suhosin extension module for PHP
Name:		php-%{modname}
Version:	0.9.18
Release:	%mkrel 4
Group:		Development/PHP
License:	PHP License
URL:		http://www.hardened-php.net/suhosin/
Source0:	%{modname}-%{version}.tgz
Source1:	%{modname}-%{version}.tgz.sig
Patch0:		suhosin-0.9.18-noservervar.patch
BuildRequires:	php-devel >= 3:5.2.0
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Suhosin is an advanced protection system for PHP installations. It was designed
to protect servers and users from known and unknown flaws in PHP applications
and the PHP core. Suhosin is binary compatible to normal PHP installation,
which means it is compatible to 3rd party binary extension like ZendOptimizer.

%prep

%setup -q -n %{modname}-%{version}
%patch0 -p1 -b .noservervar
[ "../package.xml" != "/" ] && mv ../package.xml .

%build

phpize

%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so %{modname}.so

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m0755 %{soname} %{buildroot}%{_libdir}/php/extensions/
install -m0644 suhosin.ini %{buildroot}%{_sysconfdir}/php.d/%{inifile}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS package.xml tests Changelog
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


