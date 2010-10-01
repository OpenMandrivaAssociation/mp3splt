%define	name	mp3splt
%define	version	2.2.9
%define	release	%mkrel 1

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
