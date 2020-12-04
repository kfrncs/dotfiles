#!/usr/bin/bash

echo "copying ~/.tmux.conf"
cp ~/.tmux.conf tmux.conf

echo "copying ~/.config/nvim/init.vim" 
mkdir ./config/nvim
cp ~/.config/nvim/init.vim ./config/nvim/

echo "copying ~/.config/fish/config.fish"
mkdir ./config/fish/
cp ~/.config/fish/config.fish ./config/fish/

echo "copy ~/.config/alacritty/alacritty.yml"
mkdir ./config/alacritty
cp ~/.config/alacritty/alacritty.yml ./config/alacritty
