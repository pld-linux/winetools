Summary:	WineTools is a menu driven installer for installing Windows programs under Linux.
Name:		winetools
Version:	2.1.2
Release:	0.jo.4
License:	GPL
Group:		Applications/Emulators
Source0:	http://ds80-237-203-29.dedicated.hosteurope.de/wt/%{name}-%(echo %{version} | tr -d .)jo.tar.gz
# Source0-md5:	3ce523e4c52c0b9e31fc961b1be93c06
Patch0:		%{name}-paths.patch
Patch1:		%{name}-mktemp.patch
URL:		http://www.von-thadden.de/Joachim/WineTools/
Requires:	gettext
Requires:	wget
Requires:	wine
Requires:	perl-base
Requires:	bash
Requires:	mktemp
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WineTools is a menu driven installer for installing about 90 Windows
programs under the x86 (Athlon or Intel PC) processor architecture
with the Linux operating system using Wine. This software lets you
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
by me (Joachim von Thadden). It is licensed under the GPL.

%prep
%setup -q -n %{name}-%(echo %{version} | tr -d .)jo
mv wt%(echo %{version} | tr -d .)jo wt2
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install Xdialog $RPM_BUILD_ROOT%{_bindir}
install wt2 $RPM_BUILD_ROOT%{_bindir}
install findwine $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -a scripts icon doc $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a *.ini *.cfg config.* findwine chopctrl.pl $RPM_BUILD_ROOT%{_datadir}/%{name}
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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/winetools
