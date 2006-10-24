# TODO:
# - icon and some desktop file
%define		_suffix	jo
%define		_rel 3
Summary:	WineTools - a menu driven installer for installing Windows programs under Linux
Summary(pl):	WineTools - oparty na menu instalator do windowsowych programów pod Linuksem
Name:		winetools
Version:	0.9
Release:	1.%{_suffix}.%{_rel}
Epoch:		1
License:	GPL
Group:		Applications/Emulators
Source0:	http://ds80-237-203-29.dedicated.hosteurope.de/wt/%{name}-%{version}%{_suffix}-III.tar.gz
# Source0-md5:	e15874cabdd48342e7de5a1823ee3c98
Patch0:		%{name}-paths.patch
URL:		http://www.von-thadden.de/Joachim/WineTools/
BuildRequires:	gettext-devel
BuildRequires:	sed >= 4.0
Requires:	Xdialog
Requires:	bash
Requires:	gettext
Requires:	mktemp
Requires:	perl-base
Requires:	wget
Requires:	wine >= 1:0.9
Requires:	wine-programs >= 1:0.9
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_winetoolsdir	%{_datadir}/%{name}

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
%setup -q -n %{name}-%{version}%{_suffix}-III
mv wt%{version}%{_suffix} wt2
mv gettext.sh.dummy gettext.sh
%patch0 -p1

%{__sed} -i -e 's#\. findwine#. %{_winetoolsdir}/findwine#' scripts/*
mv po/{de_DE@euro,de}.po

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_winetoolsdir}/3rdParty}

install wt2 $RPM_BUILD_ROOT%{_bindir}
install findwine $RPM_BUILD_ROOT%{_winetoolsdir}

cp -a scripts icon doc $RPM_BUILD_ROOT%{_winetoolsdir}
install *.reg findwine chopctrl.pl $RPM_BUILD_ROOT%{_winetoolsdir}
install 3rdParty/*.{cfg,reg,txt} $RPM_BUILD_ROOT%{_winetoolsdir}/3rdParty
install gettext.sh $RPM_BUILD_ROOT%{_winetoolsdir}

for i in po/*.po; do
	locale=${i#po/}
	locale=${locale%.po}
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$locale/LC_MESSAGES
	msgfmt po/$locale.po -o $RPM_BUILD_ROOT%{_datadir}/locale/$locale/LC_MESSAGES/wt2.mo
done

%find_lang wt2

%clean
rm -rf $RPM_BUILD_ROOT

%files -f wt2.lang
%defattr(644,root,root,755)
%doc INSTALL.txt LICENSE.txt doc/*
%attr(755,root,root) %{_bindir}/wt2

%dir %{_winetoolsdir}
%{_winetoolsdir}/doc
%{_winetoolsdir}/icon
%{_winetoolsdir}/gettext.sh
%{_winetoolsdir}/findwine
%{_winetoolsdir}/wt-config.reg
%attr(755,root,root) %{_winetoolsdir}/chopctrl.pl
%dir %{_winetoolsdir}/3rdParty
%{_winetoolsdir}/3rdParty/PowBallDX.cfg
%{_winetoolsdir}/3rdParty/bde.reg
%{_winetoolsdir}/3rdParty/futurepinball.reg
%{_winetoolsdir}/3rdParty/ie6.reg
%{_winetoolsdir}/3rdParty/iebatch.txt
%{_winetoolsdir}/3rdParty/steaminstall.reg
%{_winetoolsdir}/3rdParty/typograf.reg

%dir %{_winetoolsdir}/scripts
%attr(755,root,root) %{_winetoolsdir}/scripts/*
