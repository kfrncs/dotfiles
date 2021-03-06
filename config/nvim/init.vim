" install vim-plug if it's not found
if empty(glob('~/.config/nvim/autoload/plug.vim'))
    silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
        \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

" Make the undo file for persistent undo if it doesn't exist
if empty(glob('~/.config/nvim/undo/'))
    silent !mkdir ~/.config/nvim/undo
endif

" enable persistent undo
set undofile
set undodir=~/.config/nvim/undo/

call plug#begin('~/.config/nvim/autoload/')

" autocomplete
" Plug 'Shougo/deoplete.nvim'
Plug 'rust-lang/rust.vim'

" auto-pair
Plug 'vim-scripts/auto-pairs-gentle'

" call git with :Git
Plug 'tpope/vim-fugitive'

Plug 'preservim/nerdtree'
Plug 'preservim/nerdcommenter'

" Completion
Plug 'racer-rust/vim-racer'
Plug 'ncm2/ncm2'
Plug 'roxma/nvim-yarp'

" NOTE: you need to install completion sources to get completions. Check
" our wiki page for a list of sources: https://github.com/ncm2/ncm2/wiki
Plug 'ncm2/ncm2-bufword'
Plug 'ncm2/ncm2-path'
Plug 'ncm2/ncm2-racer'
Plug 'ncm2/ncm2-pyclang'
Plug 'ncm2/ncm2-jedi' 
Plug 'ncm2/ncm2-tern',  {'do': 'npm install'}
Plug 'ncm2/ncm2-cssomni'
Plug 'ncm2/ncm2-go'
Plug 'ncm2/ncm2-tmux'
Plug 'ncm2/ncm2-cssomni'

Plug 'mg979/vim-visual-multi', {'branch': 'master'}

" languages
Plug 'pangloss/vim-javascript'
Plug 'kchmck/vim-coffee-script'
Plug 'fatih/vim-go'
Plug 'dag/vim-fish'
Plug 'sheerun/vim-polyglot'
Plug 'szymonmaszke/vimpyter' " Jupyter

call plug#end()

" add gutentags to status line
" set statusline+=%{gutentags#statusline()}

if has('nvim')
"  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
"  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif
let g:deoplete#enable_at_startup = 1

" sets colour
colo slate 
let g:airline_theme = "alduin"

" TAB STUFF
" CTRL+DEL closes a tab
nnoremap <C-Delete> :tabclose<CR>

" Disable Ctrl-N mapping from vim-visual-multi
let g:VM_maps = {}
let g:VM_maps["Find Under"] = ''
let g:VM_maps["Find Subword Under"] = ''

" Ctrl-N opens a new tab
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

" autoindent
set autoindent
set cindent

" no swap files
set noswapfile

" custom commands

" change to the directory of the working file
autocmd BufEnter * if &ft !~ '^nerdtree$' | silent! lcd %:p:h | endif

" map jk to escape
imap jk <Esc>

" line numbers & relative line numbers
set number
set relativenumber

" set OS clipboard yank and pull to \y \p
noremap <Leader>y "+y
noremap <Leader>p "+p

" enable mouse. Disable for WSL? Can't paste
" set mouse=a

" rusty tags
autocmd BufRead *.rs :setlocal tags=./rusty-tags.vi;/
autocmd BufWritePost *.rs :silent! exec "!rusty-tags vi --quiet --start-dir=" . expand('%:p:h') . "&" | redraw!

" racer
set hidden
let g:racer_cmd = "/home/ken/.cargo/bin/racer"
let g:racer_experimental_completer = 1

" YouCompleteMe colors
let g:ycm_enable_diagnostic_signs = 0

" enable ncm2 (nvim-completion-manager)for all buffers
autocmd BufEnter * call ncm2#enable_for_buffer()

" IMPORTANT: :help Ncm2PopupOpen for more information
set completeopt=noinsert,menuone,noselect

" Allow code folding in Rust (zc, zo?)
let g:rust_fold = 1

" point ncm clang plugin at the c library
let g:ncm2_pyclang#library_path = '/usr/lib/clang/11.0.0/lib/'

