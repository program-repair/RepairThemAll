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
Example 1: `python src/fixa.py -t dryrun -m Codex -b Defects4J -p Lang -i 6  -w /Users/pengyu/src/kth/repair`

## Run unit test
`pytest -vv`

## Notes
* project Collections can be ignored
* Chart uses SVN
