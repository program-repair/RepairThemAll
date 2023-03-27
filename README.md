# Setup

## Overview
This repo extends from [RepairThemAll](https://github.com/program-repair/RepairThemAll), focuses on using LLMs solving APR tasks. Currently this repo only supports Codex and Defects4J benchmark.

## Prerequisite
  * git
  * install svn in your environment (for Defects4J, otherwise Jfreechart can't be checkout)
  * Java 7 and 8, better to use a version manage system to install multiple Java versions.
  * Python 3, better to use `pyenv` to manage multiple Python verions.
  * Docker: optional, only needed if you want to run this inside a docker container.
  * pipenv
  * cpanm
  * PostgreSQL 11+
 
## Setup in localhost
  * Clone this repo
  * `cd ~/llm-repair-them-all`
  * `cp .env.sample .env`
  * ./setup.sh
  * Manually apply [this change](https://github.com/rjust/defects4j/pull/499) int this file `benchmarks/defects4j/framework/core/Vcs.pm`
  * `pipenv shell`
  * `pipenv install`
  
## Setup in Docker
Running llm-repair-them-all on a Docker container is feasible, and various processes can be executed concurrently on separate containers. Here assume the docker is running on a Linux Ubuntu 22.04 LTS.
* Build docker image: `sudo docker build . -t llm --no-cache`
* Start docker container: `sudo docker run -it -v /home/ubuntu/repair:/repair llm:latest`. This command will run and start `bash` inside docker.
* Inside docker, manually apply [this change](https://github.com/rjust/defects4j/pull/499) int this file `benchmarks/defects4j/framework/core/Vcs.pm`
* Inside docker bash: `git config --global user.email "YOUR_EMAIL_ADDRESS" && git config --global user.name "YOUR_NAME"`
* Inside docker bash: `pipenv shell`
* Inside docker bash: `pipenv install`

## Database
The data are saved in PostgreSQL. A database name with `plm` should be created manually. PostgreSQL can be either installed locally or use AWS RDS or other cloud native services.

After creating an empty database `plm`. The database structure can be created by running:\
`bin/bash> python3 src/database.py`

Ensure to exam if the database structure is created after running command above.

## Configuration
Running parameters and settings should be configured in two different places.\
* `.env`: Here you can setup Codex parameters, database connection, Java home path.\
* `src/config.py`: This is a legacy file where you can configure Java params, working directory etc. Some of parameters can be moved to `.env` since the envfile has been loaded at the beginning of this file.

# Process
## Send Request

## Verify Response



