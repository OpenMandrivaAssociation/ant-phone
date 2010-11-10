%define name	ant-phone
%define version	0.2.1
%define release %mkrel 1

Name: 	 	%{name}
Summary:	Desktop ISDN telephony application
Version: 	%{version}
Release: 	%{release}

Source:		http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:		ant-phone-0.2.1-linking.patch
URL:		http://www.nongnu.org/ant-phone/
License:	GPLv2
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig
BuildRequires:  gettext
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gtk+2-devel
BuildRequires:	libsndfile-devel
BuildRequires:	alsa-lib-devel
Requires:	desktop-common-data

%description
ANT is a desktop ISDN telephony application written for GNU/Linux. It supports
OSS (Open Sound System) and I4L (ISDN4Linux).  It directly interfaces OSS and
ISDN devices, so there is no need to install extra software or hardware like
PBX (Private Branch Exchange) or telephony cards, if you've got direct access
to an audio capable ISDN card (teles or HiSax chip-set, e.g. AVM Fritz Card)
and a full duplex sound card or two sound devices.

%prep
%setup -q
%patch0 -p0 -b .linking

%build
%configure2_5x --disable-rpath
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=ANT-phone
Comment=ISDN Telephone
Exec=%{name}
Icon=communications_phone_section
Terminal=false
Type=Application
Categories=GNOME;GTK;X-MandrivaLinux-Office-Communications-Phone;Network;Telephony;
EOF

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_datadir}/applications/mandriva-%{name}.desktop
