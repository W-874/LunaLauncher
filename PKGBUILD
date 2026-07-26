pkgname=lunalauncher-git
pkgver=11.0.3
pkgrel=1
pkgdesc='A custom Minecraft launcher based on Prism Launcher'
arch=('x86_64')
url='https://github.com/AndreaFrederica/LunaLauncher'
license=('GPL-3.0-or-later')
options=('!debug')
depends=(
  'cmark'
  'gamemode'
  'hicolor-icon-theme'
  'java-runtime>=8'
  'libarchive'
  'qrencode'
  'qt6-5compat'
  'qt6-base'
  'qt6-imageformats'
  'qt6-multimedia'
  'qt6-networkauth'
  'qt6-svg'
  'qt6-websockets'
  'tomlplusplus'
  'zlib'
)
makedepends=(
  'git'
  'java-environment>=8'
  'meson'
  'ninja'
  'scdoc'
)
provides=('lunalauncher')
conflicts=('lunalauncher')
source=()
sha256sums=()

_repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"

pkgver() {
  local version rev_count short_hash

  version="$(sed -nE "s/^[[:space:]]*version: '([^']+)'.*/\1/p" \
    "$_repo_root/meson.build" | head -n1)"
  rev_count="$(git -C "$_repo_root" rev-list --count HEAD)"
  short_hash="$(git -C "$_repo_root" rev-parse --short HEAD)"

  printf '%s.r%s.g%s\n' "$version" "$rev_count" "$short_hash"
}

prepare() {
  local required_paths=(
    'libraries/cmark/meson.build'
    'libraries/libnbtplusplus/include/nbt_tags.h'
    'libraries/qtermwidget/lib/qtermwidget.cpp'
    'libraries/quickjs-ng/quickjs.c'
  )
  local path

  for path in "${required_paths[@]}"; do
    if [[ ! -e "$_repo_root/$path" ]]; then
      printf 'Missing submodule content: %s\n' "$path" >&2
      printf 'Run: git submodule update --init --recursive\n' >&2
      return 1
    fi
  done
}

build() {
  meson setup "$srcdir/build" "$_repo_root" \
    --buildtype=release \
    --prefix=/usr \
    --wrap-mode=nodownload \
    -Db_lto=true \
    -Dbuild_testing=false

  meson compile -C "$srcdir/build"
}

package() {
  DESTDIR="$pkgdir" meson install -C "$srcdir/build" --no-rebuild
}
