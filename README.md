# Web Scraper with Selenium

## Technologies

- [Python 3.9](https://python.org) : Base programming language for development
- [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
- [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
- [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convenient script for easy development experience
- [Selenium](https://www.selenium.dev/) : A free (open-source) automated testing framework used to validate web applications across different browsers and platforms
- [Celery](https://github.com/celery/celery): A simple, flexible, and reliable distributed system to process vast amounts of tasks
- [Flower](https://github.com/mher/flower): A web based tool for monitoring and administrating Celery clusters.
- [Redis](https://github.com/redis/redis-py): A NoSQL Database that serves as a Celery Broker and Result Backend
- [Aiohttp](https://docs.aiohttp.org/en/stable/): An Asynchronous HTTP Client/Server for asyncio and Python.
- [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
- [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## Getting Started

Getting started with this project is very simple, all you need is to have Git and Docker Engine installed on your machine. Then open up your terminal and run this command `git clone https://github.com/olacodes/webscraper.git` to clone the project repository.

Change directory into the project folder `cd webscraper`.

Build images and Spin up services needed for the project that are specified in **_docker-compose.yml_** file by running the command `docker-compose up`.

**NB: Running the above command for the first time will download all docker-images and third party packages needed for the app. This will take up to 5 minutes for the first build, others will be in a blink of an eye**

At this moment, your project should be up and running and start up the following Servers:

- Django Development Server: http://localhost:8000
- Redis Server: http://localhost:6379
- Flower: http://localhost:5555
- Selenium: http://localhost:444

## Exploring The App

Make sure that all the above servers are running before you start exploring the project. If those servers are up and running, have fun with the app!!!

## License

The MIT License - Copyright (c) 2022 - Present, WebScraper.

## Contributors
