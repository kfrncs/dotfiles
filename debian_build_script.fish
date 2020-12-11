#!/usr/bin/fish

#TODO: better ssh automation
#TODO more community repos?

# get OS name (TODO control flow to do different things for Arch and Deb)

     |||
     |||
# ___VVV INSTALL LIST ______

set install_list wget curl tree git neovim tmux xclip fish nodejs npm cmake pkg-config make python3 python-pip ipython jupyter-notebook \n
build-essential libncurses5-dev libncursesw5-dev texlive

#------ yep right there ^^^^ ----
#                       ||||
#                       ||||

echo ""; echo "###################################"; echo ""
echo""; echo "before you start, please edit /etc/apt/sources.list so that `buster`/release name -> `unstable`"; echo""; 
echo ""; echo "###################################"; echo ""
echo""; echo "did you run the script with `./debian_build_script.fish | tee -a debian_build.log` ???"
echo ""; echo "###################################"; echo ""
echo 'CAUTION: WE ARE ABOUT TO BUILD A NEW SYSTEM.'
echo ""; echo "###################################"; echo ""
    
read -l -P 'CONTINUE? [y/N] ' confirm

switch $confirm
    case Y y
        echo "Alright, let's do this." # continue
    case '' N n
        echo "ok bye" # exit
        exit
end

# TODO doesn't actually do anything yet
read -P 'Which OS is this? Arch or Debian? ' os
echo "os is $os"

read -P 'What did you set as your username? ' username
echo "username is $username"

echo "changing shells"
echo "/usr/bin/fish" > new_shells
cat /etc/shells >> new_shells
sudo cp new_shells /etc/shells
chsh -s /usr/bin/fish

echo ""; echo "full upgrade"; echo ""
sudo apt -y update; sudo apt -y dist-upgrade; sudo apt -y full-upgrade;

#TODO more community repos?
echo "adding community repos"
sudo apt install software-properties-common -y

echo ""; echo "SKIPPED - see what version of nvim comes up:"
echo "sudo add-apt-repository ppa:neovim-ppa/stable"; echo ""

echo "Setting Git identity"
git config --global user.email "kennethpatrickfrancis@gmail.com"
git config --global user.name "Ken Francis"

# initial install
echo "installing install_list with apt"
sudo apt install $install_list -y

echo "Installing Rust"
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
set PATH /home/$username/.cargo/env $PATH
set PATH /home/$username/.cargo/bin $PATH

# put the dotfiles out
echo "propagating dotfiles"
chmod +x hard_propagate.py
./hard_propagate.py

echo "sourcing fish config"
source ~/.config/fish/config.fish

echo "installing Fisher"
curl -sL https://git.io/fisher | fish && fisher install jorgebucaran/fisher

echo "Changing Rust to nightly"
rustup default nightly

echo "doing some Cargo installs"
set cargo_list bat skim starship racer
cargo install $cargo_list

echo "Installing Wasmer"
curl https://get.wasmer.io -sSfL | sh
sudo ln ~/.wasmer/bin/wasmer /usr/bin/wasmer

echo "installing fisher plugins"
fisher install jethrokuan/z mattgreen/lucid.fish laughedelic/pisces joseluisq/gitnow
fisher install ojiry/fish-tmux oh-my-fish/plugin-bang-bang

echo "installing Go"
curl https://dl.google.com/go/go1.15.6.linux-amd64.tar.gz -o go1.15.tar.gz
tar -C /usr/local -xzf go1.15.tar.gz
set path /usr/local/go $PATH

echo "cleaning up"
rm -fv rust-init
rm -fv rustup-init.1
rm -rfv __pycache__/
rm shells
rm go1.15.tar.gz

echo "creating ssh key"
ssh-keygen -t ed25519 -C "kennethpatrickfrancis@gmail.com"

echo "all done!"
echo "Your public ssh id_ed25519 (github):"
cat /home/$username/.ssh/id_ed25519.pub

