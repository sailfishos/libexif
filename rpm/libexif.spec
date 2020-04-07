Name:       libexif
Summary:    Library for extracting extra information from image files
Version:    0.6.21
Release:    1
License:    LGPLv2+
URL:        https://github.com/libexif/libexif
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: autoconf
BuildRequires: gettext
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Patch0: 0001-fix-CVE-2019-9278.patch

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
Requires:   %{name} = %{version}-%{release}
Obsoletes:  %{name}-docs

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
autoreconf -v -f -i
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

iconv -f latin1 -t utf-8 < COPYING > COPYING.utf8; cp COPYING.utf8 COPYING
iconv -f latin1 -t utf-8 < README > README.utf8; cp README.utf8 README
%find_lang libexif-12

rm %{buildroot}%{_docdir}/%{name}/ABOUT-NLS
rm %{buildroot}%{_docdir}/%{name}/COPYING
mv %{buildroot}%{_docdir}/%{name} %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        README NEWS

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f libexif-12.lang
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libexif.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libexif
%{_libdir}/*.so
%{_libdir}/pkgconfig/libexif.pc

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
