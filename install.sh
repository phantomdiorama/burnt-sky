#!/usr/bin/env bash
# install.sh

# assuming ~/.local/bin is in PATH
# make script executable and copy to local bin
chmod +x burntsky && cp burntsky $HOME/.local/bin/
echo "installed in ~/.local/bin/"
