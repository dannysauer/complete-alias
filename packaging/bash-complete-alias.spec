#
# spec file for package bash-complete-alias
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           bash-complete-alias
Version:        0.0
Release:        0
Summary:        Automagical shell alias completion
BuildArch:      noarch
Group:          Unspecified
License:        GPL-3.0-or-later
URL:            https://github.com/cykerway/complete-alias
Source:         %{name}.tar.xz
Requires:       bash-completion

%define completiondir /usr/share/bash-completion/completions

%description
Automatically create Bash completion entries for aliases to commands
which already have known completions

%prep
%setup -q -n %{name}

%build
# remove shebang on first line since file will only be sourced
sed -i '1{ /^#!/d }' complete_alias

%install
mkdir -p %buildroot/%completiondir
%{__install} -m 0644 complete_alias %buildroot/%completiondir
mkdir -p "%buildroot/%_docdir/%name"
%{__install} -m 0644 README.md "%buildroot/%_docdir/%name"

%files
%license LICENSE.txt
%doc %_docdir/%name
%completiondir

%changelog
