Name:       libexif
Summary:    Library for extracting extra information from image files
Version:    0.6.21
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        https://github.com/libexif/libexif
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: autoconf
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package devel
Summary:    Files needed for libexif application development
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The libexif-devel package contains the libraries and header files
for writing programs that use libexif.

%package docs
Summary:    Documentation files needed for libexif
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description docs
Documentation files for libexif.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
autoreconf -v -f -i
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

iconv -f latin1 -t utf-8 < COPYING > COPYING.utf8; cp COPYING.utf8 COPYING
iconv -f latin1 -t utf-8 < README > README.utf8; cp README.utf8 README
%find_lang libexif-12

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f libexif-12.lang
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libexif.so.*


%files devel
%defattr(-,root,root,-)
%doc README NEWS
%{_includedir}/libexif
%{_libdir}/*.so
%{_libdir}/pkgconfig/libexif.pc

%files docs
%defattr(-,root,root,-)
%{_datadir}/doc/libexif/

