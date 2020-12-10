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


print("Installing Wasmer")
call("curl https://get.wasmer.io -sSfL | sh", shell=True)
call("sudo ln ~/.wasmer/bin/wasmer /usr/bin/wasmer", shell=True)

# print("installing fisher")
call("curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher", shell=True)

cargo_list = [
    'bat',
    'skim',
    'starship',
]

run(["cargo", "install", *cargo_list])



# pisces
run(["fisher", "install", "laughedelic/pisces"])

# z fish
run(["fisher", "install", "jethrokuan/z"])

# git status plugin
run(["fisher", "install", "mattgreen/lucid.fish"])

# gitnow (git helper)
run(["fisher", "install", "joseluisq/gitnow@2.5.", "ojiry/fish-tmux", "oh-my-fish/plugin-bang-bang"])

