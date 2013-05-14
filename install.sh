#!/bin/bash

pwd=`pwd`

## Git
ln -fs $pwd/git/gitconfig ~/.gitconfig
ln -fs $pwd/git/gitignore ~/.gitignore

## SSH
ln -fs $pwd/ssh/config ~/.ssh/config

## Vim
ln -fs $pwd/vim/vimrc ~/.vimrc

## Bash
ln -fs $pwd/bash/bash_aliases ~/.bash_aliases
