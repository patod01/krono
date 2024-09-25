
# if [[ $1 = "i" ]]; then
     python -m venv .venv
     source .venv/bin/activate
     # pip install --upgrade pip
     pip install pytest-playwright
     deactivate
     echo Dependencies installed
# fi
