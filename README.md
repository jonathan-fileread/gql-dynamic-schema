# For Patrick and Speedy

## Installing

`pip install -r requirements.txt`

## Running fastapi with gql

`fastapi dev main2.py` \
Call `http://127.0.0.1:8000/graphql` with `POST`, using gql input below.

## Data to use

### Store each recordset within `document.json` - these are mongo queries that i have spliced out that will mimic dynamic changes Once the document.json has changed, edit the gql input below in your favorite API platform

old record

`{
    "_id": "65f8a1d3b1f9c45a887f1234",
    "schema": {
        "fields": {
            "friends": "int",
            "last_logged_on": "str"
        }
    },
    "data": {
        "friends": 42,
        "last_logged_on": "2021-09-01T00:00:00"
    }
}`

new record

`{
    "_id": "65f8a1d3b1f9c45a887f1234",
    "schema": {
        "fields": {
            "friends": "int",
            "last_logged_on": "str",
            "test_new_column": "str"
        }
    },
    "data": {
        "friends": 42,
        "last_logged_on": "2021-09-01T00:00:00",
        "test_new_column": "test"
    }
}`


gql input


`{
  getData {
    friends
    lastLoggedOn
  }
}
`

new gql input


`{
  getData {
    friends
    lastLoggedOn
    testNewColumn
  }
}
`