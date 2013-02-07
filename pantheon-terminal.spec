Summary:	Pantheon Terminal Emulator
Name:		pantheon-terminal
Version:	0.1
Release:	0.1
License:	GPL v3
Group:		X11/Applications
Source0:	https://launchpad.net/pantheon-terminal/0.x/0.1/+download/%{name}-%{version}.tar.gz
# Source0-md5:	868c63b826ab7e03236297e15e6c2aa8
URL:		https://launchpad.net/pantheon-terminal
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	granite-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libnotify-devel
BuildRequires:	pkgconfig
BuildRequires:	vala >= 0.10.0
BuildRequires:	vala-libgee0.6
BuildRequires:	vte-devel
Requires:	desktop-file-utils
Requires:	glib2 >= 1:2.26.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pantheon Terminal (referred to simply as "Terminal" when installed) is
a super lightweight, beautiful, and simple terminal. It's designed to
be setup with sane defaults and little to no configuration. It's just
a terminal, nothing more, nothing less.

%prep
%setup -qc

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%glib_compile_schemas

%postun
%update_desktop_database
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/pantheon-terminal
%{_desktopdir}/pantheon-terminal.desktop
%{_datadir}/glib-2.0/schemas/org.elementary.pantheon-terminal.gschema.xml
