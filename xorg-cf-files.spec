Summary:	X.org cf files
Summary(pl):	Pliki cf z X.org
Name:		xorg-cf-files
Version:	1.0.1
Release:	0.2
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/util/%{name}-X11R7.0-%{version}.tar.bz2
# Source0-md5:	f2dd453c37386293fb207431b4a073dd
Patch0:		%{name}-projectroot.patch
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
%setup -q -n %{name}-X11R7.0-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
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
%doc COPYING ChangeLog README
%{_libdir}/X11/config
