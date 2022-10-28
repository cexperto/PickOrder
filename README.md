# Pick order API

Project to implement a system that allows clients to schedule, in a available time slots, when a driver can stop by and pick up an order

## Deployment

To deploy this project, ther are 3 options: Manually, cli, docker:

Manually:

run:

    python3 -m venv venv

Activate venv in linux:

    source venv/bin/activate

Activate venv in windows:

    source venv/scripts/activate

Install dependencies:

    pip install -r requirements.txt

Make migrations:

    python3 manage.py makemigrations order

Run migrations:

    python3 manage.py migrate

Run project:

    python3 manage.py runserver


With cli:


for linux
run:

    ./clili

for windows

run:

    ./cliwin


Whit docker:

run:

    docker compose -f docker-compose-dev.yml up


## API Reference

when the project already runnig go to:

Swagger

http://localhost:8000/docs/

or

redoc

http://localhost:8000/redoc/

For driver near endpoint:

#### 
```http
  POST /drivernear
```

Json example:

    {
        "date_order": "2022-10-21",
        "hour":"4:10",
        "latitud": "2",
        "longitude": "3"
    }


Order by date
endpoint for look driver in a specific date
#### 
```http
  get orderbydate/
```
request example:

    orderbydate?date_order=2022-10-22?driver=1


Order by date
endpoint for look order in specific date

#### 
```http
  get orderbydate/
```
request example:

orderbydate?date_order=2022-10-22


## Authors

- [@cexperto](https://github.com/cexperto)


## Running Tests

To run tests, run the following command

Linux

```bash
  python3 manage.py test
```
Windows

```bash
  python manage.py test
```