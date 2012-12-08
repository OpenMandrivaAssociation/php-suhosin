%define modname suhosin
%define soname %{modname}.so
%define inifile Z98_%{modname}.ini

Summary:	Suhosin extension module for PHP
Name:		php-%{modname}
Version:	0.9.34
Release:	%mkrel 0.0.git716a292.1
Group:		Development/PHP
License:	PHP License
URL:		http://www.hardened-php.net/suhosin/
#Source0:	http://download.suhosin.org/%{modname}-%{version}.tgz
#Source1:	http://download.suhosin.org/%{modname}-%{version}.tgz.sig
Source0:	stefanesser-suhosin-716a292.tar.gz
BuildRequires:	php-devel >= 3:5.2.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Suhosin is an advanced protection system for PHP installations. It was designed
to protect servers and users from known and unknown flaws in PHP applications
and the PHP core. Suhosin is binary compatible to normal PHP installation,
which means it is compatible to 3rd party binary extension like ZendOptimizer.

%prep

#%%setup -q -n %{modname}-%{version}
%setup -q -n stefanesser-suhosin-716a292

%build
%serverbuild

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

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS tests Changelog
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


%changelog
* Wed May 02 2012 Oden Eriksson <oeriksson@mandriva.com> 0.9.34-0.0.git716a292.1mdv2012.0
+ Revision: 795011
- 0.9.34 (git snapshot)
- rebuild for php-5.4.x

* Thu Jan 19 2012 Oden Eriksson <oeriksson@mandriva.com> 0.9.33-1
+ Revision: 762691
- 0.9.33 (stack buffer overflow fix (with non FORTIFY_SOURCE compilations))
- drop the fix for CVE-2011-2483 as crypt was removed from the source

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 0.9.32.1-11
+ Revision: 761122
- rebuild

* Mon Nov 28 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.32.1-10
+ Revision: 734905
- P0: security fix for CVE-2011-2483, upgrade to crypt-blowfish-1.2

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.32.1-9
+ Revision: 696374
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.32.1-8
+ Revision: 695319
- rebuilt for php-5.3.7

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.32.1-7
+ Revision: 667734
- mass rebuild

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.32.1-6
+ Revision: 646558
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.32.1-5mdv2011.0
+ Revision: 629746
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.32.1-4mdv2011.0
+ Revision: 628052
- ensure it's built without automake1.7

* Tue Nov 23 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.32.1-3mdv2011.0
+ Revision: 600184
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.32.1-2mdv2011.0
+ Revision: 588723
- rebuild

* Tue Jul 27 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.32.1-1mdv2011.0
+ Revision: 561822
- 0.9.32.1

* Wed Apr 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.31-1mdv2010.1
+ Revision: 532632
- 0.9.31

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.29-7mdv2010.1
+ Revision: 514662
- rebuilt for php-5.3.2

* Mon Feb 22 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.29-6mdv2010.1
+ Revision: 509471
- rebuild
- rebuild

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.29-4mdv2010.1
+ Revision: 485265
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.29-3mdv2010.1
+ Revision: 468092
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.29-2mdv2010.0
+ Revision: 451222
- rebuild

* Sun Aug 16 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.29-1mdv2010.0
+ Revision: 416884
- 0.9.29

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.28-1mdv2010.0
+ Revision: 416496
- 0.9.28

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 0.9.27-7mdv2010.0
+ Revision: 397609
- Rebuild

* Wed May 13 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.27-6mdv2010.0
+ Revision: 375364
- rebuilt against php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.27-5mdv2009.1
+ Revision: 346639
- rebuilt for php-5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.27-4mdv2009.1
+ Revision: 341514
- rebuilt against php-5.2.9RC2

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.27-3mdv2009.1
+ Revision: 321953
- rebuild

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.27-2mdv2009.1
+ Revision: 310224
- rebuilt against php-5.2.7

* Mon Aug 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.27-1mdv2009.0
+ Revision: 275952
- 0.9.27

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.25-1mdv2009.0
+ Revision: 272556
- 0.9.25

* Tue Jul 15 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.24-2mdv2009.0
+ Revision: 235882
- rebuild

* Sun May 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.24-1mdv2009.0
+ Revision: 208745
- 0.9.24

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.23-4mdv2009.0
+ Revision: 200068
- rebuilt against php-5.2.6

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.23-3mdv2008.1
+ Revision: 161931
- rebuild

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.23-2mdv2008.1
+ Revision: 161930
- rebuild

* Tue Jan 15 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.23-1mdv2008.1
+ Revision: 153299
- 0.9.23

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 03 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.22-1mdv2008.1
+ Revision: 114474
- 0.9.22

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.20-7mdv2008.1
+ Revision: 107577
- restart apache if needed

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.20-6mdv2008.0
+ Revision: 77462
- rebuilt against php-5.2.4

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.20-5mdv2008.0
+ Revision: 64306
- use the new %%serverbuild macro

* Thu Jun 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.20-4mdv2008.0
+ Revision: 42296
- fix #31403

* Thu Jun 14 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.20-3mdv2008.0
+ Revision: 39389
- use distro conditional -fstack-protector

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.20-2mdv2008.0
+ Revision: 33784
- rebuilt against new upstream version (5.2.3)

* Mon May 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.20-1mdv2008.0
+ Revision: 29169
- 0.9.20

* Mon May 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.19-1mdv2008.0
+ Revision: 24076
- rebuilt against php-5.2.2 final

* Wed May 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.19-0mdv2008.0
+ Revision: 20474
- 0.9.19
- drop upstream patches; P0


* Sun Mar 11 2007 Olivier Blin <oblin@mandriva.com> 0.9.18-4mdv2007.1
+ Revision: 141144
- fix crash when register_server_variables is not defined (fix Maniadrive for example)

* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.18-3mdv2007.1
+ Revision: 134221
- rebuild

* Tue Mar 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.18-2mdv2007.1
+ Revision: 133887
- rebuild
- 0.9.18
- use the provided suhosin.ini file (thanks sesser)

* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.16-3mdv2007.1
+ Revision: 117538
- rebuilt against new upstream version (5.2.1)

* Mon Dec 18 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.16-2mdv2007.1
+ Revision: 98530
- fix deps (it does not requires pdo)

* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.16-1mdv2007.1
+ Revision: 92245
- 0.9.16

* Thu Nov 23 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.14-1mdv2007.1
+ Revision: 86751
- 0.9.14

* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.12-7mdv2007.1
+ Revision: 85480
- reworked the suhosin.ini file

* Fri Nov 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.12-6mdv2007.1
+ Revision: 85222
- rebuilt due to faulty/missing hdlists, try #6
- rebuilt due to faulty/missing hdlists, try #5
- rebuilt due to faulty/missing hdlists
- rebuilt due to faulty/missing hdlists
- rebuilt due to faulty/missing hdlists
- 0.9.12
- added some documentation in the ini file

* Thu Nov 09 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.11-1mdv2007.1
+ Revision: 79254
- 0.9.11

* Wed Nov 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.10-3mdv2007.0
+ Revision: 78320
- fix deps

* Tue Nov 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.10-2mdv2007.1
+ Revision: 77398
- rebuilt for php-5.2.0

* Tue Oct 31 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.10-1mdv2007.1
+ Revision: 74290
- 0.9.10
- Import php-suhosin

* Wed Oct 18 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-1mdv2007.1
- initial Mandriva package (looked at opensuse)

