if [[ $1 = "job" ]]; then
     cd %s
     source .venv/bin/activate
     printf "\n\n$(date)\n" >> built/longi.txt
     pytest -k $2 >> built/longi.txt
     deactivate
fi
