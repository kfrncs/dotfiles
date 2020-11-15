#!/usr/bin/bash
echo "copying ~/.zshrc"
cp ~/.zshrc zshrc
echo "copying ~/.tmux.conf"
cp ~/.tmux.conf tmux.conf
echo "copying ~/.config/nvim/init.vim" 
cp ~/.config/nvim/init.vim ./config/nvim/
echo "copying ~/.config/termite/config"
cp ~/.config/termite/config ./config/termite/
echo "copying ~/.config/fish/config.fish"
cp ~/.config/fish/config.fish ./config/fish/
