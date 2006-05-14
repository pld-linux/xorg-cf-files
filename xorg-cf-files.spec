Summary:	X.org cf files
Summary(pl):	Pliki cf z X.org
Name:		xorg-cf-files
Version:	1.0.1
Release:	0.3
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
# Source0-md5:	e3107572a02a344b5f5da57a1eb95732
Patch0:		%{name}-projectroot.patch
Patch1:		%{name}-lib64.patch
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
%setup -q -n %{name}-%{version}
%patch0 -p1
%if "%{_lib}" == "lib64"
%patch1 -p1
%endif

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
