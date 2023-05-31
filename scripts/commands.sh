#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

wait_db.sh
collectstatic.sh
makemigrations.sh
runserver.sh