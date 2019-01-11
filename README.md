# Tic Tac Toe

## Prerequisites

* Python 3.7
* PostgreSQL
* pipenv

You can install `pipenv` with `pip install pipenv`.

## Setup

Install dependencies:

```
$ pipenv install
```

Create databases in Postgres named `tictactoe` and `test_tictactoe`, then add a `.env` file that stores the connection parameters with the following syntax:

```
DB_ADDRESS='postgresql+psycopg2://<user>:<password>@localhost:<port_id>/tictactoe'
TEST_DB_ADDRESS='postgresql+psycopg2://<user>:<password>@localhost:<port_id>/test_tictactoe'
```

## Running the Tests

```
$ pipenv run python3 run_tests.py
```

## Playing the Game

```
$ pipenv run python3 startgame.py
```
