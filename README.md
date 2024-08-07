# SLCSP

## ElseWhen Technical Applicaiton
Hey my name is Henry, and this is my application to ElseWhen!

## Requirements
Python: 3.11

### install requirements and virual env
this repository has been setup to use pipenv as the software for package, python version and virtualenv management. If you have pipenv installed, the simplest way to setup your environment is to run:

`$ pipenv install `

However, a requirements file has also been generated using the commnad

` $ pipenv requirements > requirements.txt `

pip users can simply install requirements as

` $ pip install -r requirements.txt`

should contributors / reviewers prefer to just us a vanilla pip installation

## Problem

You've been asked to determine the second lowest cost silver plan (SLCSP) for
a group of ZIP codes.

## Task

You've been given a CSV file, `slcsp.csv`, which contains the ZIP codes in the
first column. Fill in the second column with the rate (see below) of the
corresponding SLCSP and emit the answer on `stdout` using the same CSV format as
the input. Write your code in your best programming language.

### Testing

For all things test driven, please refer to the /tests subfolder. Have utilised pytest as my test framework due to familiarity and ease of use. To run these unit tests run the following command in the root directory:

`$ pytest .`
