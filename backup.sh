#!/bin/bash
# TODO convert to python

echo "copying ~/.tmux.conf"
cp ~/.tmux.conf tmux.conf

echo "copying ~/.config/nvim/init.vim" 
mkdir -p ./config/nvim
cp ~/.config/nvim/init.vim ./config/nvim/

echo "copying ~/.config/fish/config.fish"
mkdir -p ./config/fish/
cp ~/.config/fish/config.fish ./config/fish/

# echo "copy ~/.config/alacritty/alacritty.yml"
# mkdir -p ./config/alacritty
# cp ~/.config/alacritty/alacritty.yml ./config/alacritty
