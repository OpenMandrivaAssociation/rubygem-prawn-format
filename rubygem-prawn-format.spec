%define oname prawn-format

Name:       rubygem-%{oname}
Version:    0.2.3
Release:    %mkrel 1
Summary:    An extension of Prawn that allows inline formatting
Group:      Development/Ruby
License:    GPLv2+
URL:        http://rubyforge.org/projects/prawn
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(prawn-core) >= 0
Requires:   rubygem(echoe) >= 0
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
An extension of Prawn that allows inline formatting

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/manual/
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%{ruby_gemdir}/gems/%{oname}-%{version}/examples/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Wed Nov 03 2010 Rémy Clouard <shikamaru@mandriva.org> 0.2.3-1mdv2011.0
+ Revision: 592794
- import rubygem-prawn-format

