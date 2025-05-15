Create a file named .python-version in your repo to pin the exact Python version.

cd .
sudo apt install python3-tk
pyenv install 3.11.4
pyenv local 3.11.4



poetry init
poetry add django
poetry install --no-root
