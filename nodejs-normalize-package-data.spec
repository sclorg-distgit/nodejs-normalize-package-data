%{?scl:%scl_package nodejs-normalize-package-data}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-normalize-package-data
Version:        1.0.3
Release:        1.sc1%{?dist}
Summary:        Normalizes npm/package.json metadata
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/meryn/normalize-package-data
Source0:        http://registry.npmjs.org/normalize-package-data/-/normalize-package-data-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

#for tests
#BuildRequires:  %{?scl_prefix}npm(tap)
#BuildRequires:  %{?scl_prefix}npm(underscore)
#BuildRequires:  %{?scl_prefix}npm(async)
#BuildRequires:  %{?scl_prefix}npm(semver)
#BuildRequires:  %{?scl_prefix}npm(github-url-from-git)

%description
normalize-package-data exports a function that normalizes package metadata. This
data is typically found in a package.json file, but in principle could come from
any source - for example the npm registry.

normalize-package-data is used by read-package-json to normalize the data it
reads from a package.json file. In turn, read-package-json is used by npm and
various npm-related tools.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/normalize-package-data
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/normalize-package-data

%nodejs_symlink_deps

%check
#%nodejs_symlink_deps --check
#%tap test/*.js || :

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/normalize-package-data
%doc README.md LICENSE AUTHORS

%changelog
* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.3-1
- New upstream release 1.0.3

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 0.2.8-1
- New upstream release 0.2.8

* Fri Nov 08 2013 Tomas Hrcka <thrcka@redhat.com> - 0.2.1-1.1
- Software collections support

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.1-1
- new upstream release 0.2.1

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- new upstream release 0.2.0
- temporarily ignore test results to make semver update easier

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.6-2
- restrict to compatible arches

* Sun Jun 02 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.6-1
- initial package
