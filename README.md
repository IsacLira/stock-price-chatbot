
# stock-price-chatbot

  

This is a browser-based chat application using Flask and SocketIO. The app's features include the common user communication and it also provides a chatbot that allows users to request stock prices from `https://stooq.com/`  using the command `/stock=code`.



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
* Set the following config variables in a `.env` file at the root folder of the project.
```
# Rabbit MQ secrets
RABBIT_MQ_USER='guest'
RABBIT_MQ_PASSWORD='guest'
RABBIT_MQ_HOST='localhost'
RABBIT_MQ_PORT=5672
RABBITMQ_QUEUE='chat_queue2'

REDIS_HOST='localhost'
REDIS_PORT=6379

SECRET_KEY = 'gjr39dkjn344_!67#'
```

## Running the app
* Start the server by typping the command:
```
PYTHONPATH=$PYTHONPATH:$PWD python server.py
```

* Run the chatbot with the following command:
```
PYTHONPATH=$PYTHONPATH:$PWD python bot.py
```

* And in order to create users use the command:
```
PYTHONPATH=$PYTHONPATH:$PWD python src/repository/user_signup.py --user 'user' --password `password`
```

Finally, you can access the chat using the endpoint `127.0.0.1:5000`