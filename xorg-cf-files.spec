Summary:	X.org cf files
Summary(pl):	Pliki cf z X.org
Name:		xorg-cf-files
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/util/%{name}-%{version}.tar.bz2
# Source0-md5:	1bdd3af74a693fb9c8b6c1927c978fee
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org cf files.

%description -l pl
Pliki cf z X.org.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_libdir}/X11/config
