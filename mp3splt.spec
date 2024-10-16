Name:		mp3splt
Summary:	Command line utility to split mp3 and ogg files
Version:	2.6.2
Release:	1
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Group:		Sound
URL:		https://mp3splt.sourceforge.net/
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(flac)
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
%autosetup -p1
%configure \
	--enable-oggsplt_symlink \
	--enable-flacsplt_symlink \
	--disable-rpath

%build
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_mandir}/man1/mp3splt.*
%{_mandir}/man1/oggsplt.*
%{_mandir}/man1/flacsplt.*
