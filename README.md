
# stock-price-chatbot

  

This is chat application using Flask and SocketIO. The app's features include the common user communication and also provides a chatbot that allows users to request stock prices using the command `/stock=code`.

  

## Requirements

* Python 3.8

* Redis Database

* Flask

* RabbitMQ

  

## Installation
  
* Install the requirements typing the command :
```
pip install -r requirements.txt 
```
* Save the default env variables in a `.env` file at the project root.
```
RABBIT_MQ_USER='guest'
RABBIT_MQ_PASSWORD='guest'
RABBIT_MQ_HOST='localhost'
RABBIT_MQ_PORT=5672
RABBITMQ_QUEUE='chat_queue2'

REDIS_HOST='localhost'
REDIS_PORT=6379
```
## Running the app
* Start the server by typping at the project root:
```python
PYTHONPATH=$PYTHONPATH:$PWD python server.py
```
* Run the chatbot by typping the following command:
```python
PYTHONPATH=$PYTHONPATH:$PWD python bot.py
```

* To create users use the command:
````
PYTHONPATH=$PYTHONPATH:$PWD python src/repository/user_signup.py --user 'user' --password `password`
```
Finally, you can access at the endpoint `127.0.0.1:5000`