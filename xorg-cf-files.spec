Summary:	X.org cf files
Summary(pl.UTF-8):	Pliki cf z X.org
Name:		xorg-cf-files
Version:	1.0.6
Release:	2
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
# Source0-md5:	28649f34fa23143f1945aa2750e1472a
Patch0:		%{name}-mandir.patch
Patch1:		%{name}-libdir.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-util-util-macros >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xorg-cf-files package contains the data files for the imake
utility, defining the known settings for a wide variety of platforms
(many of which have not been verified or tested in over a decade), and
for many of the libraries formerly delivered in the X.Org monolithic
releases.

%description -l pl.UTF-8
Pakiet xorg-cf-files zawiera pliki danych dla narzędzia imake,
definiujące znane ustawienia dla wielu platform (wiele z nich nie było
weryfikowanych ani testowanych od ponad dziesięciu lat) oraz dla wielu
bibliotek kiedyś dostarczanych w monolitycznych wydaniach X.Org.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

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
