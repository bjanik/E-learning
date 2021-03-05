#!/bin/bash

docker build -t flask ./app

docker run -d --name flask_app -p 3000:4000 flask