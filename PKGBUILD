pkgname=codept
pkgver=0
pkgrel=1
epoch=
pkgdesc="Interactively find and copy a unicode codepoint by name on Wayland"
arch=("any")
url=""
license=()
groups=()
depends=("python" "fzy" "wl-clipboard")
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("prep-db.py"
        "codept")
noextract=()
sha256sums=("SKIP" "SKIP")
validpgpkeys=()

build() {
    ./prep-db.py </usr/share/unicode/extracted/DerivedName.txt >unicode.txt
    sed -i 's#^dir=.*$#dir=/usr/lib/codept#' codept
}

package() {
    install -D -t "$pkgdir/usr/lib/codept" unicode.txt
    install -D -t "$pkgdir/usr/bin" codept
}
