# Pick order API

Project to implement a system that allows clients to schedule, in a
Available time slots, when a driver can stop by and pick up an order


## Deployment

To deploy this project: 

clone this repo

with docker:

run 
```bash
  docker compose -f docker-compose-dev.yml up
```
with cli:

run: 
```bash
  ./cli
```

For run test:

run: 
```bash
python3 manage.py test
  
```




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


## Authors

- [@cexperto](https://github.com/cexperto)


## License

[MIT](https://choosealicense.com/licenses/mit/)

