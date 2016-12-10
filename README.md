<a href="http://www.djangoproject.com/" >
	<img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." style="float: right;" />
</a>

[![Circle CI](https://circleci.com/gh/JTarball/django-myproject/tree/master.svg?style=svg)](https://circleci.com/gh/JTarball/django-myproject/tree/master)


## django-myproject
A basic default django project perfect for something.


The documentation can be found at (once deployed): https://JTarball.github.io/django-myproject/ 

[![Circle CI](https://circleci.com/gh/JTarball/codewheel-backend.svg?style=svg)](https://circleci.com/gh/JTarball/codewheel-backend)





# Django Powered Backend using Docker
<a href="http://www.djangoproject.com/" ><img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." style="float: right;" /></a>
#### Current Integrated Django Version

-	[`1.8.6`, `Django`](https://www.djangoproject.com/download/)

## Useful Docker Commands
`docker login`
  - you will need to login into docker hub (set up an account if you dont have one)

`docker build -t "<IMAGE>" .`
  - this will build the Dockerfile in the current directory and tag it with "jtarball/docker-base:latest"

`docker push "<IMAGE>"`
  - push to docker hub

`docker-compose up`
 - this command will create and start containers

`docker rm $(docker ps -a -q); docker rmi $(docker images -q);`
 - kill and remove all docker images and containers

`docker rmi $(docker images -q --filter "dangling=true")`
 - Clean up un-tagged docker images

`docker stop $(docker ps -a -q)`
 - Stop all docker processes


### Command Docker Network Problem 
Network timed out while trying to connect to https://index.docker.io/v1/repositories/library/debian/images. You may want to check you
docker-machine restart default      # Restart the environment
eval $(docker-machine env default)  # Refresh your environment settings


### How to setup a new Django Website

#### Change site name
- change website name in /<admin_url>/sites/site/ from example.com to what ever the site is to be called.

#### Change email templates
- you will need to use mailchimp & mandrill
- create/edit templates with names in mailchimp (then send to mandrill):
* 'verify-email': A template to confirm registration using email 
* ''


### How to deploy to Amazon Web Services
Based off: [Deploying A Django to AWS Elastic Beanstalk]https://realpython.com/blog/python/deploying-a-django-app-to-aws-elastic-beanstalk/

1. Get AWS Access Key, AWS Secret Access Key & AWS VPC IPD
* [Get AWS Access Key & AWS Secret Access Key](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSGettingStartedGuide/AWSCredentials.html)

* Services -> IAM 
* To get AWS VPC ID: Go to your IAM console, select Create VPC -> VPC ID should visible in one of the columns 
```
https://alexanderzeitler.com/articles/a-lap-around-aws-and-docker-machine/
pip install awscli
aws configure
aws ec2 describe-subnets

```
2. Ensure environment variables are set 
To deploy this project to AWS you must set the following environment variables:

* DOCKERHUB_USER
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_VPC_ID

```
export DOCKERHUB_USER=jtarball
export AWS_ACCESS_KEY_ID=xxxxxx
export AWS_SECRET_ACCESS_KEY=xxxxxx
export AWS_VPC_ID=xxxx
```

3. Create Docker Machine  (Only if needs to be created - so only once)
`create-docker-machine-aws.sh  <MACHINE_NAME>` 
where MACHINE_NAME is the name for the machine you want created 
 
4.
`python build-tag-push.py` 
which will build the docker app, push it to docker hub and a new compose yml file (you will need to be logged in  `docker login`)

5. Check inbounds rules if need ports to work

6. deploy
https://docs.docker.com/machine/examples/aws/

https://developer.rackspace.com/blog/dev-to-deploy-with-docker-machine-and-compose/
- export environment variables
- staging (copy across)
docker-machine scp -r ~/Masterbox/sideprojects/github/tetherbox  prod:~/
- export env
- run docker-compose from inside box

7. build image
 - docker-machine start <production-machine>
 - eval $(docker-machine env <production-machine>)
 - docker-compose build
 - docker-compose up

You can have this in your prompt if you use my bash prompt definiton from here.

Using docker-machine ip awsdocker you can get the public IP address of your machine.

If you're deploying some containers, you might wonder, why you can`t access your containers exposed ports like http://<machine-ip>:<someport>: because firewall 😱.
https://alexanderzeitler.com/articles/a-lap-around-aws-and-docker-machine/vpcsecuritygroup.png
So head over to the EC2 dashboard "Security Groups" section, select your "docker-machine" Security Group (which has been created when spinning up your machine) and make sure to allow some inbound traffic:


static:
cloudfront with options to limit to only static 

8. Serving static files with whitenoise and CDN Amazon Cloudfront 
http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html
- docker storage cloudfront
https://docs.docker.com/registry/storage-drivers/s3/





### Run tests on app
py.test --ds=project.settings.test  <app dir>
REUSE_DB=0 python manage.py test --settings=project.settings.test -s --with-queries blog

## Directory Structure / Files

* **README.md**
  - this file
* **app/**
  - docker for app including development files for django and polymer 
  - derived from 'jtarball/docker-base' (automated build from docker hub)
  - your project directory is in here
* **config/**
  - configuration files for docker
  - docker compose .ymls for different environments
  - env files for different environments
* **deployment/**
  - deployment scripts (create dockerfile for deployment, create amazon aws machine etc.)
* **nginx/**      
  - docker files for nginx service 
* **tests/**      
  - docker tests

### 'app' directory
This is the main docker image used for this project. This folder contains a directory 
which will contain all development files (django). This is shared for development.

## Issues

If you have any problems with or questions about this image, please contact us through a [GitHub issue](https://github.com/JTarball/codewheel-backend/issues).

You can also reach me by email. I would be happy to help  <james.tarball@gmail.com>

## Considerations / Future
In the future I might consider incorporating ideas from the following projects:

* https://github.com/imkevinxu/django-kevin
* https://github.com/luzfcb/cookiecutter-django-oauth
* https://github.com/pydanny/cookiecutter-django
* https://gitlab.com/rosarior/awesome-django

*e.g. caching, sendGrid email support, heroku, better management*
