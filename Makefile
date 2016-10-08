# Makefile
# 

all: run

stop:
	docker stop $(docker ps -q)

run:
	bash -c 'pushd config; docker-compose run --service-ports app'

compose:
	echo  $/
	bash -c 'pushd config; docker-compose '