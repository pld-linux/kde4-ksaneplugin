%define		_state		stable
%define		orgname		ksaneplugin
%define		qtver		4.8.1

Summary:	K Desktop Environment - SANE plugin
Summary(pl.UTF-8):	K Desktop Environment - Wtyczka SANE
Name:		kde4-ksaneplugin
Version:	4.9.0
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	491207674049fc69b2b15a1a99beb8a9
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libksane-devel >= %{version}
Obsoletes:	kde4-kdegraphics-ksane < 4.6.99
Obsoletes:	ksaneplugin <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ksane is a KDE application that enables easy scanning using SANE
libraries.

%description -l pl.UTF-8
Ksane to aplikacja KDE umożliwiająca łatwe skanowanie przy użyciu
bibliotek SANE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/ksaneplugin.so
%{_datadir}/kde4/services/ksane_scan_service.desktop
