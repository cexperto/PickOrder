
## Deployment

To deploy this project, ther are 3 options: Manually, cli, docker:

Manually:


venv in linux (make sure have root permissions):

    sudo apt install python3-virtualenv python3-venv
    virtualenv -p `which python3` venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    python3 manage.py makemigrations order
    python3 manage.py migrate
    python3 manage.py runserver


venv in windows:

    python -m venv venv
    source venv/scripts/activate
    pip install -r requirements.txt
    python3 manage.py makemigrations order
    python3 manage.py migrate
    python3 manage.py runserver


With cli:

run:

linux:

    chmod u+x clili
    ./clili

windows:

    chmod u+x cliwin
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