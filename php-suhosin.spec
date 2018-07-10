%define modname suhosin
%define soname %{modname}.so
%define inifile Z98_%{modname}.ini

Summary:	Suhosin extension module for PHP
Name:		php-%{modname}
Version:	0.9.38
Epoch:		1
Release:	2
Group:		Development/PHP
License:	PHP License
Url:		http://www.hardened-php.net/suhosin/
Source0:	http://download.suhosin.org/%{modname}-%{version}.tar.gz
Source1:	http://download.suhosin.org/%{modname}-%{version}.tar.gz.sig
BuildRequires:	php-devel >= 3:5.2.0

%description
Suhosin is an advanced protection system for PHP installations. It was designed
to protect servers and users from known and unknown flaws in PHP applications
and the PHP core. Suhosin is binary compatible to normal PHP installation,
which means it is compatible to 3rd party binary extension like ZendOptimizer.

%prep
%setup -qn suhosin-%{version}
%apply_patches

%build
%serverbuild

phpize
%configure2_5x \
	--with-libdir=%{_lib} \
	--with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so %{modname}.so

%install
install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m0755 %{soname} %{buildroot}%{_libdir}/php/extensions/
install -m0644 suhosin.ini %{buildroot}%{_sysconfdir}/php.d/%{inifile}

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%files 
%doc CREDITS tests Changelog
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}

