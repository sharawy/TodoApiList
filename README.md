# TodoApiList
Simple django rest application with celery integration
# Requirements
Pip install -r requirments.txt
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

