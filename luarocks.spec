#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x3FD8F43C2BB3C478 (h@hisham.hm)
#
Name     : luarocks
Version  : 3.9.2
Release  : 25
URL      : https://luarocks.org/releases/luarocks-3.9.2.tar.gz
Source0  : https://luarocks.org/releases/luarocks-3.9.2.tar.gz
Source1  : https://luarocks.org/releases/luarocks-3.9.2.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: luarocks-bin = %{version}-%{release}
Requires: luarocks-data = %{version}-%{release}
Requires: luarocks-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : lua-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-install-modules-into-lib64.patch

%description
<p align="center"><a href="http://luarocks.org"><img border="0" src="http://luarocks.github.io/luarocks/luarocks.png" alt="LuaRocks" width="500px"></a></p>

%package bin
Summary: bin components for the luarocks package.
Group: Binaries
Requires: luarocks-data = %{version}-%{release}
Requires: luarocks-license = %{version}-%{release}

%description bin
bin components for the luarocks package.


%package data
Summary: data components for the luarocks package.
Group: Data

%description data
data components for the luarocks package.


%package license
Summary: license components for the luarocks package.
Group: Default

%description license
license components for the luarocks package.


%prep
%setup -q -n luarocks-3.9.2
cd %{_builddir}/luarocks-3.9.2
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689895078
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static || ./configure --prefix=/usr
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1689895078
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/luarocks
cp %{_builddir}/luarocks-%{version}/COPYING %{buildroot}/usr/share/package-licenses/luarocks/3574b16eef6b2241b99934f62d3e15868b0ea01d || :
cp %{_builddir}/luarocks-%{version}/spec/fixtures/git_repo/LICENSE %{buildroot}/usr/share/package-licenses/luarocks/4dfe495c34967d84e2490b354788bf011ffdd8c5 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/luarocks
/usr/bin/luarocks-admin

%files data
%defattr(-,root,root,-)
/usr/share/lua/5.4/luarocks/admin/cache.lua
/usr/share/lua/5.4/luarocks/admin/cmd/add.lua
/usr/share/lua/5.4/luarocks/admin/cmd/make_manifest.lua
/usr/share/lua/5.4/luarocks/admin/cmd/refresh_cache.lua
/usr/share/lua/5.4/luarocks/admin/cmd/remove.lua
/usr/share/lua/5.4/luarocks/admin/index.lua
/usr/share/lua/5.4/luarocks/argparse.lua
/usr/share/lua/5.4/luarocks/build.lua
/usr/share/lua/5.4/luarocks/build/builtin.lua
/usr/share/lua/5.4/luarocks/build/cmake.lua
/usr/share/lua/5.4/luarocks/build/command.lua
/usr/share/lua/5.4/luarocks/build/make.lua
/usr/share/lua/5.4/luarocks/cmd.lua
/usr/share/lua/5.4/luarocks/cmd/build.lua
/usr/share/lua/5.4/luarocks/cmd/config.lua
/usr/share/lua/5.4/luarocks/cmd/doc.lua
/usr/share/lua/5.4/luarocks/cmd/download.lua
/usr/share/lua/5.4/luarocks/cmd/init.lua
/usr/share/lua/5.4/luarocks/cmd/install.lua
/usr/share/lua/5.4/luarocks/cmd/lint.lua
/usr/share/lua/5.4/luarocks/cmd/list.lua
/usr/share/lua/5.4/luarocks/cmd/make.lua
/usr/share/lua/5.4/luarocks/cmd/new_version.lua
/usr/share/lua/5.4/luarocks/cmd/pack.lua
/usr/share/lua/5.4/luarocks/cmd/path.lua
/usr/share/lua/5.4/luarocks/cmd/purge.lua
/usr/share/lua/5.4/luarocks/cmd/remove.lua
/usr/share/lua/5.4/luarocks/cmd/search.lua
/usr/share/lua/5.4/luarocks/cmd/show.lua
/usr/share/lua/5.4/luarocks/cmd/test.lua
/usr/share/lua/5.4/luarocks/cmd/unpack.lua
/usr/share/lua/5.4/luarocks/cmd/upload.lua
/usr/share/lua/5.4/luarocks/cmd/which.lua
/usr/share/lua/5.4/luarocks/cmd/write_rockspec.lua
/usr/share/lua/5.4/luarocks/core/cfg.lua
/usr/share/lua/5.4/luarocks/core/dir.lua
/usr/share/lua/5.4/luarocks/core/manif.lua
/usr/share/lua/5.4/luarocks/core/path.lua
/usr/share/lua/5.4/luarocks/core/persist.lua
/usr/share/lua/5.4/luarocks/core/sysdetect.lua
/usr/share/lua/5.4/luarocks/core/util.lua
/usr/share/lua/5.4/luarocks/core/vers.lua
/usr/share/lua/5.4/luarocks/deplocks.lua
/usr/share/lua/5.4/luarocks/deps.lua
/usr/share/lua/5.4/luarocks/dir.lua
/usr/share/lua/5.4/luarocks/download.lua
/usr/share/lua/5.4/luarocks/fetch.lua
/usr/share/lua/5.4/luarocks/fetch/cvs.lua
/usr/share/lua/5.4/luarocks/fetch/git.lua
/usr/share/lua/5.4/luarocks/fetch/git_file.lua
/usr/share/lua/5.4/luarocks/fetch/git_http.lua
/usr/share/lua/5.4/luarocks/fetch/git_https.lua
/usr/share/lua/5.4/luarocks/fetch/git_ssh.lua
/usr/share/lua/5.4/luarocks/fetch/hg.lua
/usr/share/lua/5.4/luarocks/fetch/hg_http.lua
/usr/share/lua/5.4/luarocks/fetch/hg_https.lua
/usr/share/lua/5.4/luarocks/fetch/hg_ssh.lua
/usr/share/lua/5.4/luarocks/fetch/sscm.lua
/usr/share/lua/5.4/luarocks/fetch/svn.lua
/usr/share/lua/5.4/luarocks/fs.lua
/usr/share/lua/5.4/luarocks/fs/linux.lua
/usr/share/lua/5.4/luarocks/fs/lua.lua
/usr/share/lua/5.4/luarocks/fs/macosx.lua
/usr/share/lua/5.4/luarocks/fs/tools.lua
/usr/share/lua/5.4/luarocks/fs/unix.lua
/usr/share/lua/5.4/luarocks/fs/unix/tools.lua
/usr/share/lua/5.4/luarocks/fs/win32.lua
/usr/share/lua/5.4/luarocks/fs/win32/tools.lua
/usr/share/lua/5.4/luarocks/fun.lua
/usr/share/lua/5.4/luarocks/loader.lua
/usr/share/lua/5.4/luarocks/manif.lua
/usr/share/lua/5.4/luarocks/manif/writer.lua
/usr/share/lua/5.4/luarocks/pack.lua
/usr/share/lua/5.4/luarocks/path.lua
/usr/share/lua/5.4/luarocks/persist.lua
/usr/share/lua/5.4/luarocks/queries.lua
/usr/share/lua/5.4/luarocks/remove.lua
/usr/share/lua/5.4/luarocks/repos.lua
/usr/share/lua/5.4/luarocks/require.lua
/usr/share/lua/5.4/luarocks/results.lua
/usr/share/lua/5.4/luarocks/rockspecs.lua
/usr/share/lua/5.4/luarocks/search.lua
/usr/share/lua/5.4/luarocks/signing.lua
/usr/share/lua/5.4/luarocks/test.lua
/usr/share/lua/5.4/luarocks/test/busted.lua
/usr/share/lua/5.4/luarocks/test/command.lua
/usr/share/lua/5.4/luarocks/tools/patch.lua
/usr/share/lua/5.4/luarocks/tools/tar.lua
/usr/share/lua/5.4/luarocks/tools/zip.lua
/usr/share/lua/5.4/luarocks/type/manifest.lua
/usr/share/lua/5.4/luarocks/type/rockspec.lua
/usr/share/lua/5.4/luarocks/type_check.lua
/usr/share/lua/5.4/luarocks/upload/api.lua
/usr/share/lua/5.4/luarocks/upload/multipart.lua
/usr/share/lua/5.4/luarocks/util.lua

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/luarocks/3574b16eef6b2241b99934f62d3e15868b0ea01d
/usr/share/package-licenses/luarocks/4dfe495c34967d84e2490b354788bf011ffdd8c5
