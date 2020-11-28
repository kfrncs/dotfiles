test $TERM != "screen"; and exec tmux

# add rust/cargo to path
set -x PATH $PATH ~/.cargo/bin

# export ssh keys
set -x SSH_KEY_PATH ~/.ssh/id_rsa.pub 

# set RUST_SRC_PATH for Racer
set -x RUST_SRC_PATH /home/ken/.rustup/toolchains/nightly-2020-10-24-x86_64-unknown-linux-gnu

# remove the default fish greeting
set fish_greeting

# set prompt to Starship
starship init fish | source

# make it so ... and .... go up 2 and 3 directories
function ...
  ../..
end
function ....
  ../../..
end

