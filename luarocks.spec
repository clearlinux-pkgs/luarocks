#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3FD8F43C2BB3C478 (h@hisham.hm)
#
Name     : luarocks
Version  : 3.1.2
Release  : 9
URL      : https://luarocks.org/releases/luarocks-3.1.2.tar.gz
Source0  : https://luarocks.org/releases/luarocks-3.1.2.tar.gz
Source99 : https://luarocks.org/releases/luarocks-3.1.2.tar.gz.asc
Summary  : Deployment and management system for Lua modules
Group    : Development/Tools
License  : MIT
Requires: luarocks-bin = %{version}-%{release}
Requires: luarocks-data = %{version}-%{release}
Requires: luarocks-license = %{version}-%{release}
BuildRequires : LuaJIT-dev
BuildRequires : lua-dev
BuildRequires : lua52-dev
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
%setup -q -n luarocks-3.1.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557284221
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static || ./configure --prefix=/usr --with-lua-interpreter=lua
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1557284221
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/luarocks
cp COPYING %{buildroot}/usr/share/package-licenses/luarocks/COPYING
cp spec/fixtures/git_repo/LICENSE %{buildroot}/usr/share/package-licenses/luarocks/spec_fixtures_git_repo_LICENSE
%make_install
## install_append content
./configure --prefix=/usr --with-lua-interpreter=luajit
%make_install
./configure --prefix=/usr --with-lua-interpreter=lua5.2
%make_install
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/luarocks
/usr/bin/luarocks-admin

%files data
%defattr(-,root,root,-)
/usr/share/lua/5.1/luarocks/admin/cache.lua
/usr/share/lua/5.1/luarocks/admin/cmd/add.lua
/usr/share/lua/5.1/luarocks/admin/cmd/make_manifest.lua
/usr/share/lua/5.1/luarocks/admin/cmd/refresh_cache.lua
/usr/share/lua/5.1/luarocks/admin/cmd/remove.lua
/usr/share/lua/5.1/luarocks/admin/index.lua
/usr/share/lua/5.1/luarocks/build.lua
/usr/share/lua/5.1/luarocks/build/builtin.lua
/usr/share/lua/5.1/luarocks/build/cmake.lua
/usr/share/lua/5.1/luarocks/build/command.lua
/usr/share/lua/5.1/luarocks/build/make.lua
/usr/share/lua/5.1/luarocks/cmd.lua
/usr/share/lua/5.1/luarocks/cmd/build.lua
/usr/share/lua/5.1/luarocks/cmd/config.lua
/usr/share/lua/5.1/luarocks/cmd/doc.lua
/usr/share/lua/5.1/luarocks/cmd/download.lua
/usr/share/lua/5.1/luarocks/cmd/help.lua
/usr/share/lua/5.1/luarocks/cmd/init.lua
/usr/share/lua/5.1/luarocks/cmd/install.lua
/usr/share/lua/5.1/luarocks/cmd/lint.lua
/usr/share/lua/5.1/luarocks/cmd/list.lua
/usr/share/lua/5.1/luarocks/cmd/make.lua
/usr/share/lua/5.1/luarocks/cmd/new_version.lua
/usr/share/lua/5.1/luarocks/cmd/pack.lua
/usr/share/lua/5.1/luarocks/cmd/path.lua
/usr/share/lua/5.1/luarocks/cmd/purge.lua
/usr/share/lua/5.1/luarocks/cmd/remove.lua
/usr/share/lua/5.1/luarocks/cmd/search.lua
/usr/share/lua/5.1/luarocks/cmd/show.lua
/usr/share/lua/5.1/luarocks/cmd/test.lua
/usr/share/lua/5.1/luarocks/cmd/unpack.lua
/usr/share/lua/5.1/luarocks/cmd/upload.lua
/usr/share/lua/5.1/luarocks/cmd/which.lua
/usr/share/lua/5.1/luarocks/cmd/write_rockspec.lua
/usr/share/lua/5.1/luarocks/core/cfg.lua
/usr/share/lua/5.1/luarocks/core/dir.lua
/usr/share/lua/5.1/luarocks/core/manif.lua
/usr/share/lua/5.1/luarocks/core/path.lua
/usr/share/lua/5.1/luarocks/core/persist.lua
/usr/share/lua/5.1/luarocks/core/sysdetect.lua
/usr/share/lua/5.1/luarocks/core/util.lua
/usr/share/lua/5.1/luarocks/core/vers.lua
/usr/share/lua/5.1/luarocks/deps.lua
/usr/share/lua/5.1/luarocks/dir.lua
/usr/share/lua/5.1/luarocks/download.lua
/usr/share/lua/5.1/luarocks/fetch.lua
/usr/share/lua/5.1/luarocks/fetch/cvs.lua
/usr/share/lua/5.1/luarocks/fetch/git.lua
/usr/share/lua/5.1/luarocks/fetch/git_file.lua
/usr/share/lua/5.1/luarocks/fetch/git_http.lua
/usr/share/lua/5.1/luarocks/fetch/git_https.lua
/usr/share/lua/5.1/luarocks/fetch/git_ssh.lua
/usr/share/lua/5.1/luarocks/fetch/hg.lua
/usr/share/lua/5.1/luarocks/fetch/hg_http.lua
/usr/share/lua/5.1/luarocks/fetch/hg_https.lua
/usr/share/lua/5.1/luarocks/fetch/hg_ssh.lua
/usr/share/lua/5.1/luarocks/fetch/sscm.lua
/usr/share/lua/5.1/luarocks/fetch/svn.lua
/usr/share/lua/5.1/luarocks/fs.lua
/usr/share/lua/5.1/luarocks/fs/lua.lua
/usr/share/lua/5.1/luarocks/fs/tools.lua
/usr/share/lua/5.1/luarocks/fs/unix.lua
/usr/share/lua/5.1/luarocks/fs/unix/tools.lua
/usr/share/lua/5.1/luarocks/fs/win32.lua
/usr/share/lua/5.1/luarocks/fs/win32/tools.lua
/usr/share/lua/5.1/luarocks/fun.lua
/usr/share/lua/5.1/luarocks/loader.lua
/usr/share/lua/5.1/luarocks/manif.lua
/usr/share/lua/5.1/luarocks/manif/writer.lua
/usr/share/lua/5.1/luarocks/pack.lua
/usr/share/lua/5.1/luarocks/path.lua
/usr/share/lua/5.1/luarocks/persist.lua
/usr/share/lua/5.1/luarocks/queries.lua
/usr/share/lua/5.1/luarocks/remove.lua
/usr/share/lua/5.1/luarocks/repos.lua
/usr/share/lua/5.1/luarocks/require.lua
/usr/share/lua/5.1/luarocks/results.lua
/usr/share/lua/5.1/luarocks/rockspecs.lua
/usr/share/lua/5.1/luarocks/search.lua
/usr/share/lua/5.1/luarocks/signing.lua
/usr/share/lua/5.1/luarocks/test.lua
/usr/share/lua/5.1/luarocks/test/busted.lua
/usr/share/lua/5.1/luarocks/test/command.lua
/usr/share/lua/5.1/luarocks/tools/patch.lua
/usr/share/lua/5.1/luarocks/tools/tar.lua
/usr/share/lua/5.1/luarocks/tools/zip.lua
/usr/share/lua/5.1/luarocks/type/manifest.lua
/usr/share/lua/5.1/luarocks/type/rockspec.lua
/usr/share/lua/5.1/luarocks/type_check.lua
/usr/share/lua/5.1/luarocks/upload/api.lua
/usr/share/lua/5.1/luarocks/upload/multipart.lua
/usr/share/lua/5.1/luarocks/util.lua
/usr/share/lua/5.2/luarocks/admin/cache.lua
/usr/share/lua/5.2/luarocks/admin/cmd/add.lua
/usr/share/lua/5.2/luarocks/admin/cmd/make_manifest.lua
/usr/share/lua/5.2/luarocks/admin/cmd/refresh_cache.lua
/usr/share/lua/5.2/luarocks/admin/cmd/remove.lua
/usr/share/lua/5.2/luarocks/admin/index.lua
/usr/share/lua/5.2/luarocks/build.lua
/usr/share/lua/5.2/luarocks/build/builtin.lua
/usr/share/lua/5.2/luarocks/build/cmake.lua
/usr/share/lua/5.2/luarocks/build/command.lua
/usr/share/lua/5.2/luarocks/build/make.lua
/usr/share/lua/5.2/luarocks/cmd.lua
/usr/share/lua/5.2/luarocks/cmd/build.lua
/usr/share/lua/5.2/luarocks/cmd/config.lua
/usr/share/lua/5.2/luarocks/cmd/doc.lua
/usr/share/lua/5.2/luarocks/cmd/download.lua
/usr/share/lua/5.2/luarocks/cmd/help.lua
/usr/share/lua/5.2/luarocks/cmd/init.lua
/usr/share/lua/5.2/luarocks/cmd/install.lua
/usr/share/lua/5.2/luarocks/cmd/lint.lua
/usr/share/lua/5.2/luarocks/cmd/list.lua
/usr/share/lua/5.2/luarocks/cmd/make.lua
/usr/share/lua/5.2/luarocks/cmd/new_version.lua
/usr/share/lua/5.2/luarocks/cmd/pack.lua
/usr/share/lua/5.2/luarocks/cmd/path.lua
/usr/share/lua/5.2/luarocks/cmd/purge.lua
/usr/share/lua/5.2/luarocks/cmd/remove.lua
/usr/share/lua/5.2/luarocks/cmd/search.lua
/usr/share/lua/5.2/luarocks/cmd/show.lua
/usr/share/lua/5.2/luarocks/cmd/test.lua
/usr/share/lua/5.2/luarocks/cmd/unpack.lua
/usr/share/lua/5.2/luarocks/cmd/upload.lua
/usr/share/lua/5.2/luarocks/cmd/which.lua
/usr/share/lua/5.2/luarocks/cmd/write_rockspec.lua
/usr/share/lua/5.2/luarocks/core/cfg.lua
/usr/share/lua/5.2/luarocks/core/dir.lua
/usr/share/lua/5.2/luarocks/core/manif.lua
/usr/share/lua/5.2/luarocks/core/path.lua
/usr/share/lua/5.2/luarocks/core/persist.lua
/usr/share/lua/5.2/luarocks/core/sysdetect.lua
/usr/share/lua/5.2/luarocks/core/util.lua
/usr/share/lua/5.2/luarocks/core/vers.lua
/usr/share/lua/5.2/luarocks/deps.lua
/usr/share/lua/5.2/luarocks/dir.lua
/usr/share/lua/5.2/luarocks/download.lua
/usr/share/lua/5.2/luarocks/fetch.lua
/usr/share/lua/5.2/luarocks/fetch/cvs.lua
/usr/share/lua/5.2/luarocks/fetch/git.lua
/usr/share/lua/5.2/luarocks/fetch/git_file.lua
/usr/share/lua/5.2/luarocks/fetch/git_http.lua
/usr/share/lua/5.2/luarocks/fetch/git_https.lua
/usr/share/lua/5.2/luarocks/fetch/git_ssh.lua
/usr/share/lua/5.2/luarocks/fetch/hg.lua
/usr/share/lua/5.2/luarocks/fetch/hg_http.lua
/usr/share/lua/5.2/luarocks/fetch/hg_https.lua
/usr/share/lua/5.2/luarocks/fetch/hg_ssh.lua
/usr/share/lua/5.2/luarocks/fetch/sscm.lua
/usr/share/lua/5.2/luarocks/fetch/svn.lua
/usr/share/lua/5.2/luarocks/fs.lua
/usr/share/lua/5.2/luarocks/fs/lua.lua
/usr/share/lua/5.2/luarocks/fs/tools.lua
/usr/share/lua/5.2/luarocks/fs/unix.lua
/usr/share/lua/5.2/luarocks/fs/unix/tools.lua
/usr/share/lua/5.2/luarocks/fs/win32.lua
/usr/share/lua/5.2/luarocks/fs/win32/tools.lua
/usr/share/lua/5.2/luarocks/fun.lua
/usr/share/lua/5.2/luarocks/loader.lua
/usr/share/lua/5.2/luarocks/manif.lua
/usr/share/lua/5.2/luarocks/manif/writer.lua
/usr/share/lua/5.2/luarocks/pack.lua
/usr/share/lua/5.2/luarocks/path.lua
/usr/share/lua/5.2/luarocks/persist.lua
/usr/share/lua/5.2/luarocks/queries.lua
/usr/share/lua/5.2/luarocks/remove.lua
/usr/share/lua/5.2/luarocks/repos.lua
/usr/share/lua/5.2/luarocks/require.lua
/usr/share/lua/5.2/luarocks/results.lua
/usr/share/lua/5.2/luarocks/rockspecs.lua
/usr/share/lua/5.2/luarocks/search.lua
/usr/share/lua/5.2/luarocks/signing.lua
/usr/share/lua/5.2/luarocks/test.lua
/usr/share/lua/5.2/luarocks/test/busted.lua
/usr/share/lua/5.2/luarocks/test/command.lua
/usr/share/lua/5.2/luarocks/tools/patch.lua
/usr/share/lua/5.2/luarocks/tools/tar.lua
/usr/share/lua/5.2/luarocks/tools/zip.lua
/usr/share/lua/5.2/luarocks/type/manifest.lua
/usr/share/lua/5.2/luarocks/type/rockspec.lua
/usr/share/lua/5.2/luarocks/type_check.lua
/usr/share/lua/5.2/luarocks/upload/api.lua
/usr/share/lua/5.2/luarocks/upload/multipart.lua
/usr/share/lua/5.2/luarocks/util.lua
/usr/share/lua/5.3/luarocks/admin/cache.lua
/usr/share/lua/5.3/luarocks/admin/cmd/add.lua
/usr/share/lua/5.3/luarocks/admin/cmd/make_manifest.lua
/usr/share/lua/5.3/luarocks/admin/cmd/refresh_cache.lua
/usr/share/lua/5.3/luarocks/admin/cmd/remove.lua
/usr/share/lua/5.3/luarocks/admin/index.lua
/usr/share/lua/5.3/luarocks/build.lua
/usr/share/lua/5.3/luarocks/build/builtin.lua
/usr/share/lua/5.3/luarocks/build/cmake.lua
/usr/share/lua/5.3/luarocks/build/command.lua
/usr/share/lua/5.3/luarocks/build/make.lua
/usr/share/lua/5.3/luarocks/cmd.lua
/usr/share/lua/5.3/luarocks/cmd/build.lua
/usr/share/lua/5.3/luarocks/cmd/config.lua
/usr/share/lua/5.3/luarocks/cmd/doc.lua
/usr/share/lua/5.3/luarocks/cmd/download.lua
/usr/share/lua/5.3/luarocks/cmd/help.lua
/usr/share/lua/5.3/luarocks/cmd/init.lua
/usr/share/lua/5.3/luarocks/cmd/install.lua
/usr/share/lua/5.3/luarocks/cmd/lint.lua
/usr/share/lua/5.3/luarocks/cmd/list.lua
/usr/share/lua/5.3/luarocks/cmd/make.lua
/usr/share/lua/5.3/luarocks/cmd/new_version.lua
/usr/share/lua/5.3/luarocks/cmd/pack.lua
/usr/share/lua/5.3/luarocks/cmd/path.lua
/usr/share/lua/5.3/luarocks/cmd/purge.lua
/usr/share/lua/5.3/luarocks/cmd/remove.lua
/usr/share/lua/5.3/luarocks/cmd/search.lua
/usr/share/lua/5.3/luarocks/cmd/show.lua
/usr/share/lua/5.3/luarocks/cmd/test.lua
/usr/share/lua/5.3/luarocks/cmd/unpack.lua
/usr/share/lua/5.3/luarocks/cmd/upload.lua
/usr/share/lua/5.3/luarocks/cmd/which.lua
/usr/share/lua/5.3/luarocks/cmd/write_rockspec.lua
/usr/share/lua/5.3/luarocks/core/cfg.lua
/usr/share/lua/5.3/luarocks/core/dir.lua
/usr/share/lua/5.3/luarocks/core/manif.lua
/usr/share/lua/5.3/luarocks/core/path.lua
/usr/share/lua/5.3/luarocks/core/persist.lua
/usr/share/lua/5.3/luarocks/core/sysdetect.lua
/usr/share/lua/5.3/luarocks/core/util.lua
/usr/share/lua/5.3/luarocks/core/vers.lua
/usr/share/lua/5.3/luarocks/deps.lua
/usr/share/lua/5.3/luarocks/dir.lua
/usr/share/lua/5.3/luarocks/download.lua
/usr/share/lua/5.3/luarocks/fetch.lua
/usr/share/lua/5.3/luarocks/fetch/cvs.lua
/usr/share/lua/5.3/luarocks/fetch/git.lua
/usr/share/lua/5.3/luarocks/fetch/git_file.lua
/usr/share/lua/5.3/luarocks/fetch/git_http.lua
/usr/share/lua/5.3/luarocks/fetch/git_https.lua
/usr/share/lua/5.3/luarocks/fetch/git_ssh.lua
/usr/share/lua/5.3/luarocks/fetch/hg.lua
/usr/share/lua/5.3/luarocks/fetch/hg_http.lua
/usr/share/lua/5.3/luarocks/fetch/hg_https.lua
/usr/share/lua/5.3/luarocks/fetch/hg_ssh.lua
/usr/share/lua/5.3/luarocks/fetch/sscm.lua
/usr/share/lua/5.3/luarocks/fetch/svn.lua
/usr/share/lua/5.3/luarocks/fs.lua
/usr/share/lua/5.3/luarocks/fs/lua.lua
/usr/share/lua/5.3/luarocks/fs/tools.lua
/usr/share/lua/5.3/luarocks/fs/unix.lua
/usr/share/lua/5.3/luarocks/fs/unix/tools.lua
/usr/share/lua/5.3/luarocks/fs/win32.lua
/usr/share/lua/5.3/luarocks/fs/win32/tools.lua
/usr/share/lua/5.3/luarocks/fun.lua
/usr/share/lua/5.3/luarocks/loader.lua
/usr/share/lua/5.3/luarocks/manif.lua
/usr/share/lua/5.3/luarocks/manif/writer.lua
/usr/share/lua/5.3/luarocks/pack.lua
/usr/share/lua/5.3/luarocks/path.lua
/usr/share/lua/5.3/luarocks/persist.lua
/usr/share/lua/5.3/luarocks/queries.lua
/usr/share/lua/5.3/luarocks/remove.lua
/usr/share/lua/5.3/luarocks/repos.lua
/usr/share/lua/5.3/luarocks/require.lua
/usr/share/lua/5.3/luarocks/results.lua
/usr/share/lua/5.3/luarocks/rockspecs.lua
/usr/share/lua/5.3/luarocks/search.lua
/usr/share/lua/5.3/luarocks/signing.lua
/usr/share/lua/5.3/luarocks/test.lua
/usr/share/lua/5.3/luarocks/test/busted.lua
/usr/share/lua/5.3/luarocks/test/command.lua
/usr/share/lua/5.3/luarocks/tools/patch.lua
/usr/share/lua/5.3/luarocks/tools/tar.lua
/usr/share/lua/5.3/luarocks/tools/zip.lua
/usr/share/lua/5.3/luarocks/type/manifest.lua
/usr/share/lua/5.3/luarocks/type/rockspec.lua
/usr/share/lua/5.3/luarocks/type_check.lua
/usr/share/lua/5.3/luarocks/upload/api.lua
/usr/share/lua/5.3/luarocks/upload/multipart.lua
/usr/share/lua/5.3/luarocks/util.lua

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/luarocks/COPYING
/usr/share/package-licenses/luarocks/spec_fixtures_git_repo_LICENSE
