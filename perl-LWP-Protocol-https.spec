%define upstream_name    LWP-Protocol-https
%define upstream_version 6.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Provide https support for LWP::UserAgent
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/LWP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Socket::SSL)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Mozilla::CA)
BuildRequires: perl(Net::HTTPS)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The LWP::Protocol::https module provide support for using https schemed
URLs with LWP. This module is a plug-in to the LWP protocol handling, so
you don't use it directly. Once the module is installed LWP is able to
access sites using HTTP over SSL/TLS.

If hostname verification is requested by LWP::UserAgent's 'ssl_opts', and
neither 'SSL_ca_file' nor 'SSL_ca_path' is set, then 'SSL_ca_file' is
implied to be the one provided by Mozilla::CA. If the Mozilla::CA module
isn't available SSL requests will fail. Either install this module, set up
an alternative 'SSL_ca_file' or disable hostname verification.

This module used to be bundled with the libwww-perl, but it was unbundled
in v6.02 in order to be able to declare its dependencies properly for the
CPAN tool-chain. Applications that need https support can just declare
their dependency on LWP::Protocol::https and will no longer need to know
what underlying modules to install.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


