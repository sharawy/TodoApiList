from .settings import *

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'test.todoListApi@gmail.com'
EMAIL_HOST_PASSWORD = 'test987654'
EMAIL_PORT = 587


BROKER_URL = "amqp://" # use rabbitMQ

