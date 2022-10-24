
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