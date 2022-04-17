#!/bin/sh

echo '[INFO] redis-chat-backend running...'

docker stop redis-chat-backend
docker rm `docker ps -qaf name=redis-chat-backend`
docker run --name redis-chat-backend -d -p 6379:6379 redis:alpine

echo '[INFO] activate virtual environment...'
source bin/activate
cd app

echo '[INFO] run server...'
python manage.py runserver