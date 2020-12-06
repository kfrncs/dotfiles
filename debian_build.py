#!/usr/bin/python3
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


# DEBIAN 

# turn this into a shell script:
# https://linuxize.com/post/how-to-install-python-3-8-on-debian-10/
# cuz i'm not using python3.7

# $ curl -O https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tar.xz
# $ tar xf Python-blah-blah
# $ cd Python-3.9.0
# $ ./configure --enable-optimizations
# $ make -j 12 (this computer is 12 core. the output of nproc is just the amount of cores)
# $ sudo make altinstall
#       fix symlink:
# $ sudo ln /usr/local/bin/python3.9 /usr/bin/python  

# initial install
install_list = [
    "base-devel",
    "gcc",
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
]

# unpack install_list with * to install 
for i in range(len(install_list)):
    run(["sudo", "apt", "--assume-yes", "install", install_list[i]])

### TODO add section generating ssh keys, w/ links and automation (raspberry pi, gitlab, github)
print("doing ssh stuff.... NOT")

print("Installing Rust")
run("wget https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init".split())
run("chmod +x rustup-init".split())
run("./rustup-init")

print("installing fisher and starship")
run("yay -S fisher starship".split())

### TODO bring in script for populating dotfiles
print("populating dotfiles...... NOT")

# fisher plugs (for some reason not working)

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

print("cleaning up")
run("rm -rfv rust-init/".split())
run("rm -fv rustup-init.1".split())

