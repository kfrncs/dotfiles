#!/usr/bin/python
from subprocess import run
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

# GNOME STUFF

# disable hotcorners:
# $ gsettings set org.gnome.shell enable-hot-corners false

# ARCH

# initial install
install_list = [
    "base-devel",
    "wget", 
    "tree", 
    "git", 
    "neovim", 
    "tmux", 
    "xclip",
    "bat",
    "fish",
    "nodejs",
    "npm"
    # some deps for alacritty
    "cmake", "freetype2", "fontconfig", "pkg-config", "make", "libxcb",
    "alacritty",
    "go", "go-tools",
]

# unpack install_list with * to install 
run(["sudo", "pacman", "-S", *install_list])

print("Installing Rust")
run("wget https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init".split())
run("chmod +x rustup-init".split())
run("./rustup-init")

# install yay
print("cloning yay")
run("git clone https://aur.archlinux.org/yay.git".split())
os.chdir("yay")
print("building yay")
run("makepkg -si".split())
print("leaving yay folder")
os.chdir("..")

print("installing fisher, package manager for fish")
run("yay -S fisher".split())

# fisher plugs (for some reason not working)

# pisces
# run(["fisher", "install", "laughedelic/pisces"])

# z fish
# run("fisher install jethrokuan/z".split())

# git status plugin
# run("fisher install mattgreen/lucid.fish".split())

# gitnow (git helper)
# run("fisher install joseluisq/gitnow@2.5.".split())
