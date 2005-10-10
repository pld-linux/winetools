%define		_suffix	jo
%define		_shortver	%(echo %{version} | tr -d .)
Summary:	WineTools - a menu driven installer for installing Windows programs under Linux
Summary(pl):	WineTools - oparty na menu instalator do windowsowych programów pod Linuksem
Name:		winetools
Version:	2.1.2
Release:	0.%{_suffix}.11
License:	GPL
Group:		Applications/Emulators
Source0:	http://ds80-237-203-29.dedicated.hosteurope.de/wt/%{name}-%{_shortver}%{_suffix}.tar.gz
# Source0-md5:	3ce523e4c52c0b9e31fc961b1be93c06
Patch0:		%{name}-paths.patch
Patch1:		%{name}-mktemp.patch
URL:		http://www.von-thadden.de/Joachim/WineTools/
BuildRequires:	gettext-devel
BuildRequires:	sed >= 4.0
Requires:	bash
Requires:	gettext
Requires:	mktemp
Requires:	perl-base
Requires:	wget
Requires:	wine
Requires:	wine-programs
Requires:	Xdialog
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WineTools is a menu driven installer for installing about 90 Windows
programs under the x86 (Athlon or Intel PC) processor architecture
with the Linux operating system using WINE. This software lets you
install the following Windows software:
- DCOM98
- IE6
- Windows Core Fonts
- Windows System Software
- Office & Office Viewer
- Adobe Photoshop 7, Illustrator 9
- many other programs

It also sets up your .wine directory in the correct way, downloads the
files to install from the web (only the free and shareware ones for
sure), installs Windows fonts and lets you uninstall and configure
your software. And it does much more than Sidenet, although it uses a
part of the configuration for IE6 (thanks for that!).

WineTools was initially written by Frank Hendriksen and was extended
by Joachim von Thadden. It is licensed under the GPL.

%description -l pl
WineTools to oparty na menu instalator do instalowania oko³o 90
windowsowych programów na komputerach z procesorem x86 (Athlon lub
Intel PC) z systemem operacyjnym Linux przy u¿yciu WINE. Ten program
pozwala zainstalowaæ nastêpuj±ce oprogramowanie dla Windows:
- DCOM98
- IE6
- podstawowe fonty Windows
- oprogramowanie systemowe Windows
- Office i Office Viewer
- Adobe Photoshop 7, Illustrator 9
- wiele innych programów.

Konfiguruje tak¿e w poprawny sposób katalog .wine, ¶ci±ga pliki do
instalacji z sieci (oczywi¶cie tylko darmowe i shareware), instaluje
fonty z Windows oraz pozwala odinstalowaæ i skonfigurowaæ
oprogramowanie. Robi to w du¿ej mierze tak jak Sidenet, ale u¿ywa
czê¶ci konfiguracji dla IE6 (za co nale¿± siê podziêkowania).

WineTools zosta³ pocz±tkowo napisany przez Franka Hendriksena i zosta³
rozszerzony przez Joachima von Thaddena. Jest licencjonowany na GPL.

%prep
%setup -q -n %{name}-%{_shortver}%{_suffix}
mv wt%{_shortver}%{_suffix} wt2
%patch0 -p1

sed -i -e '
	s,\. findwine,. %{_datadir}/%{name}/findwine,
' $(find scripts -type f)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install wt2 $RPM_BUILD_ROOT%{_bindir}
install findwine $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -a scripts icon doc $RPM_BUILD_ROOT%{_datadir}/%{name}
install *.ini *.cfg config.* *.reg findwine chopctrl.pl $RPM_BUILD_ROOT%{_datadir}/%{name}
install iebatch.txt wineinit.tar.gz $RPM_BUILD_ROOT%{_datadir}/%{name}
install gettext.sh $RPM_BUILD_ROOT%{_datadir}/%{name}

cd po
for i in $(ls *.po | cut -f1 -d.); do
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES
	msgfmt $i.po -o $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES/wt2.mo
done
cd ..

%find_lang wt2

%clean
rm -rf $RPM_BUILD_ROOT

%files -f wt2.lang
%defattr(644,root,root,755)
%doc INSTALL.txt LICENSE.txt doc/*
%attr(755,root,root) %{_bindir}/wt2

%dir %{_datadir}/winetools
%{_datadir}/winetools/doc
%{_datadir}/winetools/icon

%{_datadir}/winetools/PowBallDX.cfg
%{_datadir}/winetools/config.%{_shortver}
%{_datadir}/winetools/config.empty
%{_datadir}/winetools/lauge-prefs.ini
%{_datadir}/winetools/bde.reg
%{_datadir}/winetools/ie6.reg
%{_datadir}/winetools/iebatch.txt
%{_datadir}/winetools/wineinit.tar.gz

%{_datadir}/winetools/gettext.sh
%{_datadir}/winetools/findwine
%attr(755,root,root) %{_datadir}/winetools/chopctrl.pl

%dir %{_datadir}/winetools/scripts
%attr(755,root,root) %{_datadir}/winetools/scripts/*
