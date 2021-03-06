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


# ARCH

# TODO add community repos

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
    "npm",
    # some deps for alacritty
    "cmake", "freetype2", "fontconfig", "pkg-config", "make", "libxcb",
    "alacritty",
    "go", "go-tools",
    "python3", "python-pip", "ipython",
    "ncurses",
    "jupyter-notebook",
    "texlive-most" # LaTeX
]
#TODO add install vim-plug

# unpack install_list with * to install 
run(["sudo", "pacman", "-S", *install_list])

### TODO add section generating ssh keys, w/ links and automation (raspberry pi, gitlab, github)
print("doing ssh stuff.... NOT")

print("Installing Rust")
run("wget https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init".split())
run("chmod +x rustup-init".split())
run("./rustup-init")

print("Installing Wasmer.... NOT")
# this isnt gonna work
# run('curl https://get.wasmer.io -sSfL | sh'.split())
# sudo ln ~/.wasmer/bin/wasmer /usr/bin/wasmer


#### DID I LOSE THE CARGO SECTION? ON WHICH OS DO YOU LIVE?
# potential TODO to rewrite here

cargo_installs - [
    'bat',
    'skim',
    'starship',
    'alacritty',
]

# install yay
print("cloning yay")
run("git clone https://aur.archlinux.org/yay.git".split())
os.chdir("yay")
print("building yay")
run("makepkg -si".split())
print("leaving yay folder")
os.chdir("..")

print("installing fisher and starship")
run("yay -S fisher starship".split())

### TODO call script to propagate dotfiles 
print("populating dotfiles...... NOT")


# GNOME STUFF

# disable hotcorners:
# $ gsettings set org.gnome.shell enable-hot-corners false


print("check versions for python: ")
run("pip --version".split())

print("installing pip plugins")
# pip install -U gazpacho

# fisher plugs (for some reason not working - maybe the slashes?)

# pisces
# run(["fisher", "install", "laughedelic/pisces"])

# z fish
# run("fisher install jethrokuan/z".split())

# git status plugin
# run("fisher install mattgreen/lucid.fish".split())

# gitnow (git helper)
# run("fisher install joseluisq/gitnow@2.5.".split())

# fish-tmux
# fisher add ojiry/fish-tmux

# bang-bang, enable !! (last cmd) and !$ (last arg)
# fisher install oh-my-fish/plugin-bang-bang

print("cleaning up")
run("rm -rfv yay/".split())
run("rm -rfv rust-init/".split())
run("rm -fv rustup-init.1".split())

# -n is for no-clobber, aka don't overwrite if it exists
print("moving ghostscript in bin so gs alias works")
run("sudo mv -nv /usr/bin/gs /usr/bin/ghostscript".split())
