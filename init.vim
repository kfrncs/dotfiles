if &compatible
  set nocompatible
endif
" Add the dein installation directory into runtimepath
set runtimepath+=~/.cache/dein/repos/github.com/Shougo/dein.vim

if dein#load_state('~/.cache/dein')
  call dein#begin('~/.cache/dein')

  call dein#add('~/.cache/dein/repos/github.com/Shougo/dein.vim')
  call dein#add('Shougo/deoplete.nvim')
  if !has('nvim')
    call dein#add('roxma/nvim-yarp')
    call dein#add('roxma/vim-hug-neovim-rpc')
  endif

  call dein#end()
  call dein#save_state()
endif

filetype plugin indent on
syntax enable

call dein#add('Shougo/deoplete.nvim')
if !has('nvim')
  call dein#add('roxma/nvim-yarp')
  call dein#add('roxma/vim-hug-neovim-rpc')
endif
let g:deoplete#enable_at_startup = 1


" sets colour
colo slate 

" TAB STUFF
" CTRL+DEL closes a tab
nnoremap <C-Delete> :tabclose<CR>

" N opens a new tab
nnoremap <C-N> :tabe<CR>

" H and L scroll through tabs in normal mode (instead of gt/gT)
nnoremap H gT
nnoremap L gt
    

" TAB KEY, four spaces
filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
" when indenting with '>' use 4 spaces width
set shiftwidth=4
" on pressing tab insert 4 spaces
set expandtab

" no swap files
set noswapfile

" set up ctags
set tags=tags

" custom commands

" change to the directory of the working file
command Here lcd %:p:h

" map jk to escape
:imap jk <Esc>

" line numbers & relative line numbers
set number
set relativenumber

" set OS clipboard yank and pull to \y \p
noremap <Leader>y "+y
noremap <Leader>p "+p

" enable mouse
set mouse=a
