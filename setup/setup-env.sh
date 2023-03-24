@@ -2,19 +2,19 @@


# Economiser de l'espace disque
sudo apt purge -y thunderbird*
sudo apt purge -y libreoffice*
sudo apt purge -y docker*
apt purge -y thunderbird*
apt purge -y libreoffice*
apt purge -y docker*

# Mise a jour
sudo apt-get update
apt-get update

# Installation PyEnv

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"

# Installation de Python 3.8
@@ -25,7 +25,7 @@ pyenv virtualenv 3.8.0 projetm2
pyenv activate projetm2

# Installation OpenCV
sudo apt install -y opencv-python
apt install -y opencv-python

# Clone PySide2
git clone https://github.com/hiroyuki-s1/PySide2InstallForJetson.git ~/PySide2InstallForJetson
@@ -36,4 +36,4 @@ python3.8 -m pip install PySide2-5.9.0a1-5.9.5-cp36-cp36m-linux_aarch64.whl
cd && rm -rf PySide2InstallForJetson

# Installation torch et torchvision
pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 -f
pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 -f https://download.pytorch.org/whl/cu102/torch_stable.html