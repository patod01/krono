if [[ $1 = "job" ]]; then
     cd %s
     source .venv/bin/activate
     printf "\n$(date)\n" >> built/longi.txt
     pytest -k $2 -v >> built/longi.txt
     pytest -k delay -v \
     | grep -v platform \
     | grep -v cachedir \
     | grep -v rootdir >> built/longi.txt
     deactivate
fi
