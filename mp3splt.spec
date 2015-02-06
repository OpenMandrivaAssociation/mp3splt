%define	name	mp3splt
%define	version	2.4.1
%define release	3

Name:		%{name}
Summary:	Command line utility to split mp3 and ogg files
Version:	%{version}
Release:	%{release}
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Group:		Sound
URL:		http://mp3splt.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	oggvorbis-devel
BuildRequires:	mad-devel
BuildRequires:	libmp3splt-devel
License:	GPLv2+

%description
Mp3Splt is a command line utility to split MP3 (VBR supported) and Ogg Vorbis
files between a beginning and an end time position, without decoding.

It's very useful to split large mp3/ogg to make smaller files or to split
entire albums to obtain original tracks. If you want to split an album, you can
select split points and filenames manually or you can get them automatically
from CDDB (internet or a local file) or from .cue files. Supports also
automatic silence split, that can be used also to adjust cddb/cue splitpoints.

Otherwise if you have a file created either with Mp3Wrap or AlbumWrap you can
extract tracks just in few seconds.

%prep
%setup -q

%build
%configure2_5x \
	--enable-oggsplt_symlink \
	--disable-rpath
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_mandir}/man1/mp3splt.*
%{_mandir}/man1/oggsplt.*


%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-2mdv2012.0
+ Revision: 773004
- relink against libpcre.so.1

* Thu Nov 24 2011 Andrey Bondrov <abondrov@mandriva.org> 2.4.1-1
+ Revision: 733211
- New version 2.4.1

* Thu Aug 18 2011 Andrey Bondrov <abondrov@mandriva.org> 2.4-1
+ Revision: 695193
- New version 2.4

* Sun Mar 06 2011 Jani Välimaa <wally@mandriva.org> 2.3a-1
+ Revision: 642247
- new version 2.3a

* Fri Mar 04 2011 Jani Välimaa <wally@mandriva.org> 2.3-1
+ Revision: 641582
- new version 2.3

* Fri Oct 01 2010 Jani Välimaa <wally@mandriva.org> 2.2.9-1mdv2011.0
+ Revision: 582293
- new version 2.2.9

* Fri Aug 27 2010 Jani Välimaa <wally@mandriva.org> 2.2.8-1mdv2011.0
+ Revision: 573593
- new version 2.2.8
- drop unneeded patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.1c-3mdv2009.0
+ Revision: 252945
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2.1c-1mdv2008.1
+ Revision: 136608
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 17 2007 Adam Williamson <awilliamson@mandriva.org> 2.1c-1mdv2008.0
+ Revision: 52981
- add patch0 (fix build with GCC 4)
- spec clean
- new release 2.1c
- Import mp3splt


* Thu Nov  4 2004 Pascal Terjan <pterjan@mandrake.org> 2.1-1mdk
- New release 2.1

* Tue Apr 04 2004 Pascal Terjan <pterjan@mandrake.org> 2.0e-1mdk
- 2.0e

* Thu Mar 11 2004 Pascal Terjan <pterjan@mandrake.org> 2.0d-1mdk
- 2.0d

* Fri Jan 10 2004 Pascal Terjan <pterjan@mandrake.org> 2.0-1mdk
- 2.0

* Thu Nov 13 2003 Pascal Terjan <CMoi@tuxfamily.org> 1.9-2mdk
- fix typo in summary

* Thu Nov 06 2003 Pascal Terjan <CMoi@tuxfamily.org> 1.9-1mdk
- new in contribs
