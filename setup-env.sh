sudo apt-get update

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
exec "$SHELL"
pyenv install 3.8.0



pyenv virtualenv 3.8.0 projetm2
pyenv activate projetm2

sudo apt-get install libgtk-3-dev

sudo apt-get install torch==1.10.0 torchvision==0.11.1