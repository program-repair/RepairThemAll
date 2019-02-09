# Repair Them All


## Benchmarks

| Benchmark      | # Projects | # Bugs |
| -------------- | -----------| -------|
| Bears          |         71 |    251 |
| Bugs.jar       |          8 |   1158 |
| Defects4J      |          6 |    395 |
| IntroClassJava |          6 |    297 |
| QuixBugs       |         40 |     40 |
| **Total**      |        130 |   2051 |

## Tools

1. Nopol
2. DynaMoth
3. NPEFix
4. jGenProg
5. jKali
6. jMutRepair
7. Carduman
8. Arja
9. GenProg-A
10. RSRepair-A
11. Kali-A

## Usage

1. Init the repository with `./init.sh`.
2. Use `python script/repair.py` to run the repair tools on the benchmarks

General usage:

```bash
python script/repair.py {astor,npefix,nopol,dynamoth}
    --benchmark [Defects4J, IntroclassJava, Bugs.jar, Bears, QuixBugs]
    --id <bug_id> # optional, if not specified all the bugs of the benchmark will be executed. The format is specific for each benchmark
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
