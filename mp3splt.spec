%define name mp3splt
%define version 2.1
%define sversion 2.0
%define release 1mdk

Name: %{name}
Summary: Command line utility to split mp3 and ogg files
Version: %{version}
Release: %{release}
Source: %{name}-%{sversion}-src.tar.bz2
Group: Sound
URL: http://mp3splt.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: oggvorbis-devel mad-devel autoconf2.5
License: GPL

%description
Mp3Splt is a command line utility to split mp3 (VBR supported) and ogg files
selecting a begin and an end time position, without decoding.

It's very useful to split large mp3/ogg to make smaller files or to split
entire albums to obtain original tracks. If you want to split an album, you can
select split points and filenames manually or you can get them automatically
from CDDB (internet or a local file) or from .cue files. Supports also
automatic silence split, that can be used also to adjust cddb/cue splitpoints.

Otherwise if you have a file created either with Mp3Wrap or AlbumWrap you can
extract tracks just in few seconds.
%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}-%{sversion}

%build

%configure2_5x
%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README
%{_bindir}/*
%{_mandir}/man1/mp3splt.1.bz2
