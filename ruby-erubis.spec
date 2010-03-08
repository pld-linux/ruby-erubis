%define pkgname erubis
Summary:	Fast, secure, and very extensible implementation of eRuby
Name:		ruby-%{pkgname}
Version:	2.6.5
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	071dc576fe9f1c547ef2993e0be942b0
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Erubis is a fast, secure, and very extensible implementation of eRuby.
It has the following features.

- Very fast, almost three times faster than ERB and about ten percent
  faster than eruby (implemented in C).
- File caching of converted Ruby script support.
- Auto escaping (sanitizing) support, it means that '<%= %>' can be
  escaped in default. It is desirable for web application.
- Spaces around '<% %>' are trimmed automatically only when '<%' is at
  the beginning of line and '%>' is at the end of line.
- Embedded pattern changeable (default '<% %>'), for example '[% %]'
  or '<? ?>' are available.
- Enable to handle Processing Instructions (PI) as embedded pattern
  (ex. '<?rb ... ?>'). This is desirable for XML/HTML than '<% .. %>'
  because the latter breaks HTML design but the former doesn't.
- Multi-language support (Ruby/PHP/C/Java/Scheme/Perl/Javascript).
- Context object available and easy to combine eRuby template with
  YAML datafile (see the below example).
- Print statement available.
- Easy to expand and customize in subclass
  - Print statement support
  - Lines starting with percent character ('%') support
  - Another embedded pattern support
  - etc...
- Ruby on Rails support.
- Mod_ruby support.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.txt -o -print | xargs touch --reference %{SOURCE0}

%{__sed} -i -e 's,/usr/bin/env ruby,%{__ruby},' bin/erubis

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{ActionView,ERB}
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%attr(755,root,root) %{_bindir}/erubis
%{ruby_rubylibdir}/erubis.rb
%{ruby_rubylibdir}/erubis

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Erubis
