#!/usr/bin/fish

#TODO: better ssh automation

# get OS name (TODO control flow to do different things for Arch and Deb)
set os (uname -n)
echo "OS detected is `$os`"

echo "before you start, please edit /etc/apt/sources.list so that `buster`/release name -> `unstable`"

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

# echo full upgrade
sudo apt update; sudo apt upgrade; sudo apt full-upgrade

read -P 'What did you set as your username? ' username
echo "username is $username"

#TODO more community repos?
echo "adding community repos"
sudo apt install software-properties-common
sudo add-apt-repository ppa:neovim-ppa/stable

echo "Setting Git identity"
git config --global user.email "kennethpatrickfrancis@gmail.com"
git config --global user.name "Ken Francis"
 
# initial install
echo "installing initial list with apt"
set install_list wget curl tree git neovim tmux xclip fish nodejs npm cmake pkg-config make python3 python-pip ipython jupyter-notebook
sudo apt install $install_list

# missing from auto-installs:
# "base-devel", TODO what's the apt equivalent?
# "texlive-most" # LaTeX # TODO
# "ncurses", # TODO
# "go", "go-tools", # TODO
 
echo "Installing Rust"
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup default nightly
set PATH /home/$username/.cargo/env $PATH
set PATH /home/$username/.cargo/bin $PATH

# put the dotfiles out
chmod +x propagate_dotfiles.py
./propagate_dotfiles.py

echo "Installing Wasmer"
curl https://get.wasmer.io -sSfL | sh
sudo ln ~/.wasmer/bin/wasmer /usr/bin/wasmer

echo "doing some Cargo installs"
set cargo_list bat skim starship racer
cargo install $cargo_list

chsh -s /usr/bin/fish

echo "sourcing fish config"
source ~/.config/fish/config.fish 

echo "installing Fisher and plugins"
curl -sL https://git.io/fisher | fish && fisher install jorgebucaran/fisher
fisher install jethrokuan/z mattgreen/lucid.fish laughedelic/pisces joseluisq/gitnow
fisher install ojiry/fish-tmux oh-my-fish/plugin-bang-bang

echo "cleaning up"
rm -fv rust-init
rm -fv rustup-init.1
rm -rfv __pycache__/

echo "creating ssh key"
ssh-keygen -t ed25519 -C "kennethpatrickfrancis@gmail.com"

echo "all done!"
echo "Your public ssh id_ed25519 (github):"
cat /home/$username/.ssh/id_ed25519.pub

