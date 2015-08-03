#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:           desktop-data-BLINUX
Version:        3.0
Release:        0
Summary:        Shared Desktop Files for BLINUX
License:        BSD-2-Clause
Group:		System/GUI/Other

Provides:       desktop-data
Requires:       hicolor-icon-theme
Requires:       xdg-utils
Requires:       dmz-icon-theme-cursors
Requires:       wallpaper-branding = %{version}
Provides:       desktop-branding = %{version}

BuildArch:      noarch
Source0:	applications.menu

Packager:       Emmanuel Vadot <elbarto@bocal.org>
Url:            http://www.blinux.fr
Vendor:		Blinux

%description
BLINUX default desktop files (menu, wallpapers etc ...)

%prep

%build

%install
mkdir -p %{buildroot}/%{_sysconfdir}/xdg/menus/
install -D -m 644 %{SOURCE0} %{buildroot}/%{_sysconfdir}/xdg/menus/

%files
%defattr(-,root,root)
/etc/xdg/menus/
%config %{_sysconfdir}/xdg/menus/applications.menu

%changelog
* Mon Aug 03 2015 Emmanuel Vadot <elbarto@bocal.org> - 3.9
- Update to 3.0

* Wed Aug 06 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0
- Package creation
