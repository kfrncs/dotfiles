#!/usr/bin/python3
from subprocess import run, call
import sys
import os

# ARE YOU SURE YOU WANT TO DO THIS? Y/N
print("#####################################################################")
print("WARNING:")
print("THIS SCRIPT IS FOR BUILDING A NEW SYSTEM. ARE YOU SURE?")
print("#####################################################################")
answer = input("Y/N? ")

if answer.lower() != "y" and answer.lower() != "yes":
    print("Ok bye")
    sys.exit()


# ARCH

# TODO add community repos

# initial install
install_list = [
#    "base-devel",
    "wget", 
    "curl",
    "tree", 
    "git", 
    "neovim", 
    "tmux", 
    "xclip",
#    "bat",
    "fish",
    "nodejs",
    "npm",
    # some deps for alacritty
    "cmake", "fontconfig", "pkg-config", "make", 
#    "freetype2", "libxcb",
#    "alacritty",
#    "go", "go-tools",
    "python3", "python-pip", "ipython",
#    "ncurses",
    "jupyter-notebook",
#    "texlive-most" # LaTeX
]
# install vim-plug
run(["curl", "-fLo", "/.local/share/nvim/site/autoload/plug.vim", "--create-dirs", "https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"])

# unpack install_list with * to install 
run(["sudo", "apt", "install", *install_list])

### TODO add section generating ssh keys, w/ links and automation (raspberry pi, gitlab, github)
print("doing ssh stuff.... NOT")

print("Installing Rust")
run("wget https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init".split())
run("chmod +x rustup-init".split())
run("./rustup-init")


### TODO call script to propagate dotfiles 
import propagate_dotfiles

# GNOME STUFF

# disable hotcorners:
# $ gsettings set org.gnome.shell enable-hot-corners false

# print("installing pip plugins")
# run(["pip", "install", "-U", "gazpacho"])

print("cleaning up")
run("rm -rfv rust-init/".split())
run("rm -fv rustup-init.1".split())

print("Pat 1 complete. Restart/logout and come back, then run part 2")
