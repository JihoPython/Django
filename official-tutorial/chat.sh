#!/bin/sh

REDIS="redis-chat-backend"
CID="DOCKER REDIS CONTAINER ID"

C_RED="\033[0;31m"
C_GREEN="\033[0;32m"
C_DEFAULT="\033[0m"
INFO="${C_GREEN}[INFO]${C_DEFAULT}"


echo "${INFO} ${REDIS} running"
CID=$(docker ps -qaf name=$REDIS)

if [ ! -z $CID ]
then
    echo "${INFO} delete before redis container :: ${C_RED}$(docker rm -f $CID)${C_DEFAULT}"
fi

CID=$(docker run --name ${REDIS} -d -p 6379:6379 redis:alpine)
echo "${INFO} new redis container id :: ${C_GREEN}${CID}${C_DEFAULT}"

echo "${INFO} activate virtual environment"
source bin/activate
cd app

echo "${INFO} run server"
python manage.py runserver

echo ""
echo "${INFO} remove redis container :: ${C_RED}${CID}${C_DEFAULT}"
CID=$(docker rm -f $CID)