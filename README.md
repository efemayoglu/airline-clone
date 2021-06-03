# airline-clone

#To run by using self

python manage.py runserver

Or

#To run by using docker

docker build --tag airline-ticket-service .

docker run -d -p 4000:8000 airline-ticket-service

applications runs on 4000 like http://127.0.0.1:4000/flights

if you want the run a command inside of the container use this;
08aaedf233fb is a container id if you want to learn it run "docker ps"
docker exec -it 08aaedf233fb bash

also if you want to create a super user inside of the docker
use this command;
python manage.py createsuperuser

