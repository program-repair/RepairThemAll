# RepairThemAll for Large Language Models
install svn!!! (for Defects4J, otherwise Jfreechart can't be checkout)
## Environment
TODO
pipenv install
pipenv shell

## Smallest example per project
Chart: 8
Cli: 10
Closure: 55
Codec: 4
Collections: SKIP
Compress: 13
Csv: 4
Gson: 18
JacksonCore: 20
JacksonDatabind: 7
JacksonXml: 5
Jsoup: 29
JxPath: 21
Lang: 26 
Math: 2
Mockito: 9
Time: 22
## Test Codex
`python src/runner.py`
Example "Run bug 6 in project Lang": `python src/fixa.py -m Codex -b Defects4J -p Lang -i 6  -w /Users/pengyu/src/kth/repair`
Example "Run all bugs in project Lang": `python src/fixa.py -m Codex -b Defects4J -p Lang  -w /Users/pengyu/src/kth/repair`
Example "Run all bugs from all projects": `python src/fixa.py -m Codex -b Defects4J -w /Users/pengyu/src/kth/repair`

## Run unit test
`pytest -vv`

## Notes
* project Collections can be ignored
* Chart uses SVN

## Docker
### Build docker locally:
`docker build -t zpengyu/plm-repair-them-all -f Dockerfile .`
### Build docker image by docker-compose
`docker-compose build --no-cache`
### Run docker by docker-compose
`docker-compose run repair`

### Execute defects4j in docker cli
`pipenv shell`
`pipenv install`

### ask codex for choices
`python3 src/ask.py -m Codex -b Defects4J -p Chart -i 6  -w /repair`
`python3 src/ask.py -m Codex -b Defects4J -p Chart -s 2  -w /repair`

### verify codex response by given postres id range, for example id range [123, 456]
`python3 src/verify.py -i 123-456  -w /repair`