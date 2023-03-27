# RepairThemAll for Large Language Models

## Overview
This repo extends from [RepairThemALl](https://github.com/program-repair/RepairThemAll), focuses on using LLMs solving APR tasks. Currently this repo only supports Codex and Defects4J benchmark.

## Prerequsite
  * git
  * install svn in your environment (for Defects4J, otherwise Jfreechart can't be checkout)
  * Java 7 and 8, better to use a version manage system to install multiple Java versions.
  * Python 3, better to use `pyenv` to manage multiple Python verions.
  * Docker: optional, only needed if you want to run this inside a docker container.
  * pipenv
  * perl
  * PostgreSQL 11+
 
## Setup in localhost
  * Clone this repo
  * `cd ~/llm-repair-them-all`
  * cp .env.sample .env
  * ./setup.sh
  * Manually apply [this change](https://github.com/rjust/defects4j/pull/499) int this file `benchmarks/defects4j/framework/core/Vcs.pm`
  * `pipenv shell`
  * `pipenv install`
  
## Setup in Docker

TODO:

