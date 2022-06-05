# Web Scraper with Selenium

![Web Scrapper](https://github.com/olacodes/webscraper/actions/workflows/ci.yml/badge.svg)

[![Black Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

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

## A Simple Architecture

![A Web Scrapper Architecture]("./static/web-scrapper-arch.jpeg/")

## Getting Started

Getting started with this project is very simple, all you need is to have Git and Docker Engine installed on your machine. 

- Clone the repository `git clone https://github.com/olacodes/webscraper.git`
- change directory `cd webscraper`.
- Run `docker-compose up`
  - **NB:** *Running the above command for the first time will download all docker-images and third party packages needed for the app. This will take up to 5 minutes or more for the first build, others will be in a blink of an eye*

At this moment, your project should be up and running and start up the following Servers:

- Django Development Server: http://localhost:8000
- Redis Server: http://localhost:6379
- Flower: http://localhost:5555
- Selenium: http://localhost:4444

## Exploring The App

Make sure that all the above servers are running before you start exploring the project. If those servers are up and running, Let's have fun with the app!!!

### Web Scraper 

- Go to `http://localhost:8000` on your browser
- Click on the Scrape button to scrape data (pdf urls) from `greenbooklive.com`
- Click on `Download` button to download the pdf files.
  - **NB: This files will be saved in the root directory `pdfs/`**

- You can click on the `about` to read more about the Scraper app.

### Flower

You can also monitor and administer PDF Downloads Background Job with flower. Go to `http://localhost:5555` on your browser.

Login with `username: debug` and `password: secret`

## License

The MIT License - Copyright (c) 2022 - Present, WebScraper.

## Contributors
