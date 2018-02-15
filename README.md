# TodoApiList
Simple django rest application with celery integration
# Requirements
1. Installing RabbitMq broker :https://www.rabbitmq.com/download.html
2. run commands
```
Pip install -r requirments.txt
```
```
manage.py makemigrations
```
```
manage.py migrate
```
# How to run
1. Run celery worker instance:
```
manage.py celery worker --loglevel=DEBUG
```
2. Run django development server:
```
manage.py runserver
```
3. Go to  http://127.0.0.1:8000/ 
# Notes
1. Default settings is production  
```
#settings.__init__.py
from .production_settings import * #settings for smtp backend and RabbitMq broker
#from .local_settings import * #settings for file based mail backend and DB broker
```
2. For authnticated requests set JWT token to Authorization header
```
#example
Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo3LCJ1c2VybmFtZSI6InRlc3QxIiwiZXhwIjoxNTAwODM3NzM2LCJlbWFpbCI6InRlc3QxQGdtYWlsLmNvbSJ9.3U8tz5S2NZ3acOG-DukxB16egWPtpr4vi4oG7wOXetI
```




