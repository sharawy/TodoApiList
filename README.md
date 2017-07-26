# TodoApiList
Simple django rest application with celery integration
# Requirements
1. Installing RabbitMq broker :https://www.rabbitmq.com/download.html
2. run command 
```
Pip install -r requirments.txt
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
# Note
Default settings is production  
```
#settings.__inti__.py
from .production_settings import * #settings for smtp backend and RabbitMq broker
#from .local_settings import * #settings for file based mail backend and DB broker
```





