# Set default term

sudo update-alternatives --install /usr/bin/x-terminal-emulator x-terminal-emulator /usr/bin/wezterm 1
sudo update-alternatives --set x-terminal-emulator /usr/bin/wezterm
