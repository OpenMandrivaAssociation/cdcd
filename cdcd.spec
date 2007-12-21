%define	name	cdcd
%define	version	0.6.6
%define	release	%mkrel 3

Summary:	Command line based cd player with cddb support
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	libcdaudio-devel ncurses-devel readline-devel
URL:		http://libcdaudio.sourceforge.net/

%description
cdcd takes a different approach from conventional console
(or X) based CD players, in that it doesn't keep with the
display-oriented paradigm. Conventional computer-based CD players
resemble traditional physical CD players.  This is fine, if your
user interface consists of 10 buttons. However, computers have
keyboards, so why not use them?  Besides, it's certainly a waste 
of a console or an xterm to have a traditional CD player
open anyway.

%prep
%setup  -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post 
%_install_info %{name}.info

%postun 
%_remove_install_info %{name}.info

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*

