#!/bin/sh

docker-compose down
git fetch
git pull
docker-compose up --build -d