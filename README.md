# Setup

## Overview
This repo extends from [RepairThemAll](https://github.com/program-repair/RepairThemAll), focuses on using LLMs solving APR tasks. Currently this repo only supports Codex and Defects4J benchmark. If want to use ChatGPT for APR, you can refer the [README.md]().

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

A PostgreSQL GUI application is recommended to install.

## Configuration
Running parameters and settings should be configured in two different places.\
* `.env`: Here you can setup Codex parameters, database connection, Java home path.\
* `src/config.py`: This is a legacy file where you can configure Java params, working directory etc. Some of parameters can be moved to `.env` since the envfile has been loaded at the beginning of this file.

# Process
## Send Request
`src/ask_defects4j.py` can send the request to Codex and save the response in the Database.
* Send request to Codex for by a given project and bug_id: `python3 src/ask_defects4j.py -m Codex -b Defects4J -p Cli -i 1  -w /YOU_REPAIR_DATA_DIR`
* Send request to Codex for the whole project: `python3 src/ask_defects4j.py -m Codex -b Defects4J -p Cli  -w /YOU_REPAIR_DATA_DIR`
* Send request to Codex by a given project and starts from bug_id: `python3 src/ask_defects4j.py -m Codex -b Defects4J -p Cli -s 5  -w /YOU_REPAIR_DATA_DIR`
* Send request to Codex for all bugs in Defects4J: `python3 src/ask_defects4j.py -m Codex -b Defects4J -w /YOU_REPAIR_DATA_DIR`

## Verify Response
`src/verify_defects4j.py` can verify codex response by running unit tests.
* Verify codex response by a given range of database IDs: `python3 src/verify_defects4j.py -i 100-200  -w /repair`

## Internal enumerations of codex response:
* `RESPONDED`: This type represents a response received from Codex but the verification phase has not yet begun. The choice within the Codex response matches `finish_reason=="stop"`. This type of choice is eligible and will be verified in later phases.

* `EXCEED_MAX_LENGTH`: This type indicates that a response has been received from Codex, but the choice has `finish_reason=="length"`, which indicates that Codex is attempting to generate more tokens than allowed. This means the code block in the choice is not closed properly, and further action will not be taken with this choice.

* `RESPONDED_NULL`: This type signifies that a response has been received from Codex, but the choice has `finish_reason==null`. This reason has not been specified in the Codex API documentation. The choices have been examined, and only a portion of the response code chunks are closed properly. Therefore, these choices will not be included in the study.

* `TEMPLATE_ERROR`: This type is assigned when the Codex API times out or when the token limit is exceeded after several attempts. The related data will still be saved in the database, even though no response is received.

* `TEST_SUCCESS`: This type indicates that all unit tests for the verifying choice have passed for the choice with the "RESPONDED" state. This is the only case that will be considered a successfully verified choice.

* `TEST_TIMEOUT`: This type represents a time-out condition when the execution time for running unit tests exceeds 10 minutes.

* `TEST_FAILED_BUT_MATCHED_REDUCED`: This type indicates that the unit tests for the verifying choice have not been fully passed. The number of failed unit tests for the current verifying choice equals the number of failing tests for the original fixed code but is smaller than the number of failing tests for the original buggy code. This means that the original fixed code has not passed all unit tests.

* `TEST_FAILED_BUT_REDUCED`: This type indicates that the unit tests for the verifying choice have not been fully passed. The number of failed unit tests for the current verifying choice is smaller than the number of failing tests for the original buggy code, and the original fixed code has passed all unit tests.

* `TEST_FAILED`: This type indicates that the unit tests for the verifying choice have not been fully passed. The number of failed unit tests for the current verifying choice is greater than or equal to the number of failing tests for the original buggy code.

* `SAMPLE_ERROR`: This type represents an error that occurs during compilation or while running unit tests. Typically, this means that the choice response is unable to make the project fully compile.
