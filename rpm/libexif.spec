Name:       libexif
Summary:    Library for extracting extra information from image files
Version:    0.6.22.1
Release:    1
License:    LGPLv2+
URL:        https://libexif.github.io/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: autoconf
BuildRequires: gettext
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package devel
Summary:    Files needed for libexif application development
Requires:   %{name} = %{version}-%{release}

%description devel
The libexif-devel package contains the libraries and header files
for writing programs that use libexif.

%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Obsoletes:  %{name}-docs

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%reconfigure --disable-static --disable-docs
%make_build

%install
%make_install

rm -rf %{buildroot}%{_datadir}/doc/libexif
iconv -f latin1 -t utf-8 < COPYING > COPYING.utf8; cp COPYING.utf8 COPYING
iconv -f latin1 -t utf-8 < README > README.utf8; cp README.utf8 README
%find_lang libexif-12

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
make check

%files -f libexif-12.lang
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libexif.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libexif
%{_libdir}/libexif.so
%{_libdir}/pkgconfig/libexif.pc

%files doc
%defattr(-,root,root,-)
%doc README NEWS ABOUT-NLS SECURITY.md
