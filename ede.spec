# TODO: CFLAGS, .so files in /usr/share
Summary:	Equinox Desktop Environment
Name:		ede
Version:	2.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/ede/%{name}-%{version}.tar.gz
# Source0-md5:	8b9820c84929d66e6258e223737c27c6
Patch0:		%{name}-ksh.patch
Patch1:		%{name}-dontbuildpekwm.patch
URL:		http://www.equinox-project.org/
BuildRequires:	asciidoc
BuildRequires:	edelib-devel
BuildRequires:	jam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xdgconfdir	/etc/xdg
%define		_xdgdatadir	%{_datadir}/desktop-directories

%description
EDE is small and fast desktop environment that uses
http://www.fltk.org.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
%configure
jam -q -dx

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT jam -q -dx install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/manual
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/ede
%{_datadir}/dbus-1/services/org.equinoxproject.Launch.service
%{_datadir}/ede/*
%{_datadir}/xsessions/ede.desktop
%{_desktopdir}/*.desktop
%{_iconsdir}/*
%{_xdgconfdir}/ede/*.conf
%{_xdgconfdir}/menus/ede-applications.menu
%{_xdgdatadir}/*.directory
