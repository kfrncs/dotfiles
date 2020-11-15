test $TERM != "screen"; and exec tmux

# add rust/cargo to path
set -x PATH $PATH ~/.cargo/bin

# export ssh keys
set -x SSH_KEY_PATH ~/.ssh/id_rsa.pub 

# remove the default fish greeting
set fish_greeting

# set prompt to Starship
starship init fish | source
