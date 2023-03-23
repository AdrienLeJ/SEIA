#!/bin/bash


# Economiser de l'espace disque
sudo apt purge -y thunderbird*
sudo apt purge -y libreoffice*
sudo apt purge -y docker*

# Mise a jour
sudo apt-get update

# Installation PyEnv

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
exec "$SHELL"

# Installation de Python 3.8

pyenv install 3.8.0

pyenv virtualenv 3.8.0 projetm2
pyenv activate projetm2

# Installation OpenCV 
sudo apt install -y opencv-python

# Clone PySide2
git clone https://github.com/hiroyuki-s1/PySide2InstallForJetson.git ~/PySide2InstallForJetson

# Installation PySide2
cd ~/PySide2InstallForJetson/dist
python3.8 -m pip install PySide2-5.9.0a1-5.9.5-cp36-cp36m-linux_aarch64.whl
cd && rm -rf PySide2InstallForJetson

# Installation torch et torchvision
pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 -f 