Name:    gpgme
Version: 1.0.2
Release: 2%{?dist_tag}
Summary: GnuPG Made Easy - high level crypto API
License: LGPL
Group:   Applications/System
URL:     http://www.gnupg.org/related_software/gpgme/
Source0: ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-1.0.2.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-1.0.2.tar.bz2.sig
Patch0:  %{name}-1.0.2-macro.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gnupg >= 1.2.2
BuildRequires: gnupg2 >= 1.9.6
BuildRequires: pth-devel
BuildRequires: libgpg-error-devel >= 0.5

Requires: gnupg >= 1.2.2
Requires: gnupg2 >= 1.9.6

Obsoletes: cryptplug <= 0.3.16-2

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package devel
Summary:  Static libraries and header files from GPGME, GnuPG Made Easy
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libgpg-error-devel
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
%description    devel
Static libraries and header files from GPGME, GnuPG Made Easy.


%prep
%setup -q
%patch0 -p0


%build
%configure \
  --program-prefix="%{?_program_prefix}" \
  --enable-static

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT{%{_infodir}/dir,%{_libdir}/*.la}


%check || :
make check


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%post devel
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :

%postun devel
if [ $1 -eq 0 ] ; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :
fi


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING* ChangeLog NEWS README* THANKS TODO VERSION
%{_libdir}/libgpgme*.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/gpgme-config
%{_includedir}/gpgme.h
%{_libdir}/libgpgme*.a
%{_libdir}/libgpgme*.so
%{_datadir}/aclocal/gpgme.m4
%{_infodir}/gpgme.info*


%changelog
* Fri Mar 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0.2-2
- Fix FC4 build.

* Tue Feb  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:1.0.2-1
- LGPL used here, and made summary more explicit.
- Remove dirmngr dependency (gpgsm interfaces with it).
- Obsolete cryptplug as gpgme >= 0.4.5 provides what we used cryptplug for.

* Thu Jan 06 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0:1.0.2-0.fdr.1
- 1.0.2

* Thu Oct 21 2004 Rex Dieter <rexdieter at sf.net> 0:1.0.0-0.fdr.1
- 1.0.0
- Requires: dirmngr

* Tue Oct 19 2004 Rex Dieter <rexdieter at sf.net> 0:0.4.7-0.fdr.1
- 0.4.7

* Sun May  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.3
- Require %%{_bindir}/gpgsm instead of newpg.
- Cosmetic spec file improvements.

* Thu Oct 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.2
- Update description.

* Tue Oct  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.1
- Update to 0.4.3.

* Fri Aug 15 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.2-0.fdr.1
- Update to 0.4.2.
- make check in the %%check section.

* Thu Jul 10 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.1-0.fdr.1
- Update to 0.4.1.
- Make -devel cooperate with --excludedocs.

* Sat Apr 19 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.0-0.fdr.2
- BuildRequire pth-devel, fix missing epoch in -devel Requires (#169).
- Save .spec in UTF-8.

* Sat Mar 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.0-0.fdr.1
- Update to current Fedora guidelines.
- Exclude %%{_libdir}/*.la.

* Tue Feb 12 2003 Warren Togami <warren@togami.com> 0.4.0-1.fedora.3
- info/dir temporary workaround

* Sat Feb  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.4.0-1.fedora.1
- First Fedora release.
