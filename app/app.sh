#!/bin/bash

# команда для сборки на MacOS: "docker buildx build -t local/app:pitermar ."

sudo docker pull ubuntu && sudo docker build -t local/app:pitermar . && sudo docker run -p 8000:8000 -it local/app:pitermar