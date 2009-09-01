%define name	ant-phone
%define version	0.1.13
%define release %mkrel 2

Name: 	 	%{name}
Summary:	Desktop ISDN telephony application
Version: 	%{version}
Release: 	%{release}

Source:		http://www.antcom.de/ant-phone/download/%{name}-%{version}.tar.bz2
URL:		http://www.antcom.de/
License:	GPL
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig
BuildRequires:  gettext
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gtk+2-devel
BuildRequires:	libsndfile-devel

%description
ANT is a desktop ISDN telephony application written for GNU/Linux. It supports
OSS (Open Sound System) and I4L (ISDN4Linux).  It directly interfaces OSS and
ISDN devices, so there is no need to install extra software or hardware like
PBX (Private Branch Exchange) or telephony cards, if you've got direct access
to an audio capable ISDN card (teles or HiSax chipset, e.g. AVM Fritz Card)
and a full duplex soundcard or two sound devices.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=ANT-phone
Comment=ISDN Telephone
Exec=%{_bindir}/%{name}
Icon=communications_phone_section
Terminal=false
Type=Application
Categories=GNOME;GTK;X-MandrivaLinux-Office-Communications-Phone;Network;Telephony;
EOF

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS README AUTHORS ChangeLog TODO COPYING
%{_bindir}/%name
%{_mandir}/man1/%name.1.*
%{_datadir}/applications/mandriva-%{name}.desktop

