# Repair Them All


## Benchmarks

| Benchmark      | # Projects | # Bugs |
| -------------- | -----------| -------|
| Defects4J      |          6 |    395 |
| Bugs.jar       |          8 |   1158 |
| IntroClassJava |          6 |    297 |
| Bears          |         41 |    142 |
| QuixBugs       |         40 |     40 |
| **Total**      |        100 |   1992 |

## Tools

1. Nopol
2. DynaMoth
3. NPEFix
4. Astor

## Usage

There are two scripts: `script/repair.py` and `script/repair-all.py`, the first script is used to repair one specific bug, the second is used to run the repair of all the bugs of a specific benchmark.

General usage:

```bash
python script/repair.py {astor,npefix,nopol,dynamoth}
    --benchmark [defects4j, introclassjava, bugs.jar, Bears, QuixBugs]
    --id <bug_id> # the format is specific for each benchmark
```

Tool Specific options:

#### Astor

```bash
--seed SEED           The random seed
--scope SCOPE, -s SCOPE
                      The scope of the ingredients [local, package, global]
```

#### Nopol/Dynamoth

```bash
 --statement-type STATEMENT_TYPE, -t STATEMENT_TYPE
                        The targeted statement [condition, precondition,
                        pre_then_cond]
  --seed SEED, -s SEED  The random seed
```

#### NPEFix

TODO
