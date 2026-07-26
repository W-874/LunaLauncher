%global forgeurl https://github.com/W-874/LunaLauncher
%global datadir_name LunaLauncher
%bcond_with tests
%if %{with tests}
%global meson_build_testing true
%else
%global meson_build_testing false
%endif

Name:           lunalauncher
Version:        11.0.2
Release:        1%{?dist}
Summary:        Custom Minecraft launcher based on Prism Launcher

License:        GPL-3.0-only AND CC-BY-SA-4.0
URL:            %{forgeurl}
Source0:        %{name}-%{version}.tar.gz

# Fedora/COPR baseline.
# Keep Fedora-version-specific dependency adjustments grouped here so targets
# like Fedora 42-rawhide can be carried in one spec.
BuildRequires:  cmake >= 3.28
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  meson >= 1.4.0
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtnetworkauth-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtwebsockets-devel
BuildRequires:  scdoc
BuildRequires:  shared-mime-info
BuildRequires:  cmark-devel
BuildRequires:  pkgconfig(gamemode)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(tomlplusplus) >= 3.2.0
BuildRequires:  zlib-devel

Recommends:     java-headless

%description
Luna Launcher is a custom Minecraft launcher based on Prism Launcher with
additional multiplayer, authentication, mirror, theme, server, and
customization features.

%prep
%autosetup -n %{name}-%{version}

%build
%meson \
    --wrap-mode=nodownload \
    -Dbuild_testing=%{meson_build_testing}
%meson_build

%install
%meson_install
install -Dm0644 %{_vpath_builddir}/program_info/org.lunalauncher.LunaLauncher.desktop \
    %{buildroot}%{_datadir}/applications/org.lunalauncher.LunaLauncher.desktop
install -Dm0644 %{_vpath_builddir}/program_info/org.lunalauncher.LunaLauncher.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo/org.lunalauncher.LunaLauncher.metainfo.xml
install -Dm0644 program_info/org.lunalauncher.LunaLauncher.mime.xml \
    %{buildroot}%{_datadir}/mime/packages/org.lunalauncher.LunaLauncher.xml
install -Dm0644 program_info/org.lunalauncher.LunaLauncher.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.lunalauncher.LunaLauncher.svg
install -Dm0644 program_info/org.lunalauncher.LunaLauncher_256.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/org.lunalauncher.LunaLauncher.png
install -d %{buildroot}%{_mandir}/man6
scdoc < program_info/lunalauncher.6.scd | gzip -c \
    > %{buildroot}%{_mandir}/man6/lunalauncher.6.gz

%check
%if %{with tests}
%meson_test
%endif

%post
if [ -x %{_bindir}/update-desktop-database ]; then
    %{_bindir}/update-desktop-database -q %{_datadir}/applications || :
fi
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor || :
fi
if [ -x %{_bindir}/update-mime-database ]; then
    %{_bindir}/update-mime-database %{_datadir}/mime || :
fi

%postun
if [ -x %{_bindir}/update-desktop-database ]; then
    %{_bindir}/update-desktop-database -q %{_datadir}/applications || :
fi
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor || :
fi
if [ -x %{_bindir}/update-mime-database ]; then
    %{_bindir}/update-mime-database %{_datadir}/mime || :
fi

%files
%license LICENSE
%doc README.md
%{_bindir}/lunalauncher
%{_datadir}/applications/org.lunalauncher.LunaLauncher.desktop
%{_datadir}/icons/hicolor/256x256/apps/org.lunalauncher.LunaLauncher.png
%{_datadir}/icons/hicolor/scalable/apps/org.lunalauncher.LunaLauncher.svg
%{_datadir}/metainfo/org.lunalauncher.LunaLauncher.metainfo.xml
%{_datadir}/mime/packages/org.lunalauncher.LunaLauncher.xml
%{_datadir}/%{datadir_name}/
%{_mandir}/man6/lunalauncher.6*

%changelog
* Sun May 24 2026 W-874 <1317825684@qq.com> - 11.0.2-1
- Generalize Fedora packaging for COPR targets Fedora 42 through Rawhide

* Mon May 18 2026 W-874 <1317825684@qq.com> - 11.0.2-1
- Add Fedora 44 COPR-friendly RPM packaging baseline
