# To-do

## Install package
pip install -r requirements.txt

## Start server
python -m uvicorn main:app --reload

## Swagger
http://.../docs

# Docker run

## Database
docker run --name todo-pg -p 5432:5432 -e POSTGRES_USER=todouser -e POSTGRES_PASSWORD=s1a2v3a4 -e POSTGRES_DB=todo -d postgres:13.3