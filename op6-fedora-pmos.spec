Name:           op6-fedora-pmos
Version:        0.3.0
Release:        1%{?dist}
Summary:        OnePlus 6 Fedora and postmarketOS utilities

License:        --
URL:            https://github.com/maggu2810/%{name}/
Source0:        https://github.com/maggu2810/%{name}/archive/refs/tags/v%{version}.tar.gz


%description
OnePlus 6 Fedora and postmarketOS utilities


%prep
%autosetup


%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/op6-fedora-pmos/
install -m 0755 bin/pmos-adopt-and-integrate %{buildroot}/usr/bin/pmos-adopt-and-integrate
install -m 0755 bin/pmos-chroot-adv %{buildroot}/usr/bin/pmos-chroot-adv
install -m 0755 bin/pmos-chroot-setup %{buildroot}/usr/bin/pmos-chroot-setup
install -m 0755 bin/update-all %{buildroot}/usr/bin/update-all


%files
/usr/bin/pmos-adopt-and-integrate
/usr/bin/pmos-chroot-adv
/usr/bin/pmos-chroot-setup
/usr/bin/update-all


%changelog
* Tue May 30 2023 Markus Rathgeb <maggu2810@gmail.com>
- Bump v0.3.0

* Sat May 27 2023 Markus Rathgeb <maggu2810@gmail.com>
- Bump v0.2.0

* Mon May 22 2023 Markus Rathgeb <maggu2810@gmail.com>
- Initial RPM
