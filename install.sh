#!/bin/bash

pwd=`pwd`

## Git
ln -fs $pwd/git/gitconfig ~/.gitconfig
ln -fs $pwd/git/gitignore ~/.gitignore

## SSH
ln -fs $pwd/ssh/config ~/.ssh/config
