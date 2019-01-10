# Tic Tac Toe

## Prerequisites

* Python 3.7
* PostgreSQL

## Setup

Install dependencies:

```
$ pipenv install
```

If `pipenv` is not installed on your system, you can easily install it with `pip install pipenv`.

Create databases in Postgres named `tictactoe` and `test_tictactoe`, then add a `.env` file that stores the connection parameters with the following syntax:

```
DB_ADDRESS='postgresql+psycopg2://<user>:<password>@localhost:<port_id>/tictactoe'
TEST_DB_ADDRESS='postgresql+psycopg2://<user>:<password>@localhost:<port_id>/test_tictactoe'
```

## Running the Tests

```
$ python3 run_tests.py
```

## Playing the Game

```
$ python3 startgame.py
```
