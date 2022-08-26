# python-cli-bazel-mongodb-select-all

## Description
A pymongo example w/o login.
Creates a single collection `weapon`
inside `test` database. Inserts a
single record then prints the whole
collection and the collections inside
`test` database.
Creates an index on the `name` field.

## Tech stack
- bazel
- python
- mongodb

## Docker stack
- l.gcr.io/google/bazel:latest

## To run
`sudo ./install.sh -u`

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

# Credits
[Examples](https://pymongo.readthedocs.io/en/stable/tutorial.html)
