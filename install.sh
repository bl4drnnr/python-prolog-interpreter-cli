#!/usr/bin/env bash

repository="https://github.com/bl4drnnr/python-prolog-interpreter-cli.git"

echo "Python Prolog Interpreter CLI installation..."

cd "$HOME"
mkdir -p "$HOME/.ppil"
cd "$HOME/.ppil"

git clone "$repository"

cd "$HOME/.ppil/python-prolog-interpreter-cli"

for EACH_PROFILE in ".profile" ".bashrc" ".bash_profile" ".zprofile" ".zshrc"
    do
      echo "alias ppil='python3 ${HOME}/.ppil/python-prolog-interpreter-cli/main.py'" >> "${HOME}/${EACH_PROFILE}"
    done

/usr/bin/pip3 install -r "$HOME/.ppil/python-prolog-interpreter-cli/requirements.txt"

echo "Python Prolog Interpreter CLI have been successfully installed..."
