  #!/usr/bin/env bash
  
echo "Remove all local Docker artifacts"

echo "Stop all running containers"  
docker stop $(docker container ls -q)

echo "Remove all containers"
docker container prune
docker ps -a -q | xargs docker rm

echo "Remove all images"
docker images -a -q | xargs docker rmi -f
docker image prune -a

echo "Remove all networks"
docker network prune