if [[ $1 = "cron" ]]; then
     cd %s
     source .venv/bin/activate
     date >> built/longi.txt
     pytest -k $2 >> built/longi.txt
     deactivate
fi
