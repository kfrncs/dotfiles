#!/usr/bin/python3
from subprocess import run, call
import sys
import os
import propagate_dotfiles

print("Downloading Python3.9")
#run(["curl", "--output", 
#    "python3.9.tar.xz", 
#    "https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tar.xz"
#])

#run(["tar", "-xf", "python3.9.tar.xz"])
#os.chdir("Python-3.9.1")
#print("Configuring Python 3.9")
#run("./configure")
#print("make Python 3.9")
#run("make")
#print("make install on Python 3.9")
#run("sudo make install".split())

print("get rid of the old Python symlinks..")
run("sudo rm /usr/bin/python".split())
run("sudo rm /usr/bin/pip".split())
print("..and in with the new")
run("sudo ln /usr/local/bin/python3.9 /usr/bin/python".split())
run("sudo ln /usr/bin/pip3 /usr/bin/pip".split())

print("cleaning up")
run("rm -rf Python-3.9.1".split())
run("rm Python-3.9.1".split())
run("python3.9 -m pip install –upgrade pip".split())
