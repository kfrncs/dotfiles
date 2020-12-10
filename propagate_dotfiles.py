#!/usr/bin/python3
from subprocess import run
import sys
import os

def propagate():

    # make nvim config folder if needed
    run(["mkdir", "-p", "/home/ken/.config/nvim/"])
    run(["mkdir", "-p", "/home/ken/.config/fish/"])


    # [FROM, TO], [FROM, TO]
    config_list = [
            ["config/nvim/init.vim", "/home/ken/.config/nvim/init.vim",],
            ["config/fish/config.fish", "/home/ken/.config/fish/config.fish"],
            ["tmux.conf", "/home/ken/.tmux.conf"],
    ]

    # [FROM, TO], [FROM, TO]
    arch_list = [
        ["config/alacritty/alacritty.yml", "/home/ken/.config/alacritty/alacritty.yml"]
    ]
    
    # do the actual copy
    for i in range(len(config_list)):
        print(f"copying {config_list[i][0]} to {config_list[i][1]}"), 
        run(["cp", config_list[i][0], config_list[i][1],])
    

if __name__ == '__main__':

    # ARE YOU SURE YOU WANT TO DO THIS? Y/N
    print("#####################################################################")
    print("WARNING:")
    print("You're about to overwrite the dotfiles on the system you're on. ARE YOU SURE?")
    print("#####################################################################")
    answer = input("Y/N? ")

    if answer.lower() != "y" and answer.lower() != "yes":
        print("Ok bye")
        sys.exit()

    propagate()
