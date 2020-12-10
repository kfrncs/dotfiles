#!/usr/bin/python3
from subprocess import run, call
import sys
import os
import propagate_dotfiles

# ARE YOU SURE YOU WANT TO DO THIS? Y/N
print("#####################################################################")
print("WARNING:")
print("THIS SCRIPT IS FOR BUILDING A NEW SYSTEM. ARE YOU SURE?")
print("#####################################################################")
answer = input("Y/N? ")

if answer.lower() != "y" and answer.lower() != "yes":
    print("Ok bye")
    sys.exit()


# Debian 

# Allows you to add-apt-repository
run(["sudo", "apt", "install", "software-properties-common"])

# TODO add community repos
run("sudo add-apt-repository ppa:neovim-ppa/stable".split())

print("Setting Git identity")
run('git config --global user.email "kennethpatrickfrancis@gmail.com"'.split())
run('git config --global user.name "Ken Francis"'.split())  

# initial install
install_list = [
#    "base-devel", TODO
    "wget", 
    "curl",
    "tree", 
    "git", 
    "neovim", 
    "tmux", 
    "xclip",
    "fish",
    "nodejs",
    "npm",
    "cmake", "pkg-config", "make", 
#    "go", "go-tools", # TODO
    "python3", "python-pip", "ipython",
#    "ncurses", # TODO
    "jupyter-notebook",
#    "texlive-most" # LaTeX # TODO
]

# unpack install_list with * to install 
run(["sudo", "apt", "install", *install_list])

# install vim-plug
run(["sudo", "curl", "-fLo", "/.config/nvim/autoload/plug.vim", "--create-dirs", "https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"])


### TODO add section generating ssh keys, w/ links and automation (raspberry pi, gitlab, github)
print("doing ssh stuff.... NOT")

print("Installing Rust")
run("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh", shell=True)
run("rustup default nightly".split())
call(". /home/ken/.cargo/env", shell=True)

propagate_dotfiles.propagate()

# GNOME STUFF

# disable hotcorners:
# $ gsettings set org.gnome.shell enable-hot-corners false

# print("installing pip plugins")
# run(["pip", "install", "-U", "gazpacho"])


print("Installing Wasmer")
call("curl https://get.wasmer.io -sSfL | sh", shell=True)
call("sudo ln ~/.wasmer/bin/wasmer /usr/bin/wasmer", shell=True)

print()
print("#####################################################################")
print("Please source Rust:")
print("$ source ~/.cargo/env")
print("Copy/paste")
print("#####################################################################")
rust_answer = input("Y/N? ")

if rust_answer.lower() != "y" and rust_answer.lower() != "yes":
    print("Ok bye")
    sys.exit()

cargo_list = [
    'bat',
    'skim',
    'starship',
    'racer',
]
run(["cargo", "install", *cargo_list])

print("cleaning up")
run("rm -fv rust-init".split())
run("rm -fv rustup-init.1".split())
run("rm -rfv __pycache__/".split())


# outro
run('ssh-keygen -t ed25519 -C "kennethpatrickfrancis@gmail.com"'.split())  
print("Your public ssh id_ed25519 (github):")
print(run('cat /home/ken/.ssh/id_ed25519.pub'.split()))  

print("\n\n")
print("all done! don't forget to: \n\n- run :PlugInstall in nvim")
print("- edit /etc/apt/sources.list so that `buster`/release name -> `unstable`")
print("$ source ~/.config/fish/config.fish") 
print("$ chsh -s /usr/bin/fish")
print("$ curl -sL https://git.io/fisher | fish && fisher install jorgebucaran/fisher")
print('$ fisher install jethrokuan/z mattgreen/lucid.fish laughedelic/pisces joseluisq/gitnow')
print('$ fisher install ojiry/fish-tmux oh-my-fish/plugin-bang-bang')
print("$ sudo apt update; sudo apt upgrade; sudo apt full-upgrade")

