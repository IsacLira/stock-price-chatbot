
# stock-price-chatbot



This is a browser-based chat application using Flask and SocketIO. The app's features include the common user communication and it also provides a chatbot that allows users to request stock prices from `https://stooq.com/`  using the command `/stock=code`.



## Requirements

* Python 3.8

* Redis Database

* Flask
* SocketIO
* RabbitMQ


Install the requirements typing the command:
```
pip install -r requirements.txt
```
* Set the following config variables in a `.env` file at the root folder of the project or use the `.env.sample` as reference.
```
# Rabbit MQ secrets
RABBIT_MQ_USER='guest'
RABBIT_MQ_PASSWORD='guest'
RABBIT_MQ_HOST='localhost'
RABBIT_MQ_PORT=5672
RABBITMQ_QUEUE='chat_queue'


# REDIS secrets
REDIS_HOST='localhost'
REDIS_PORT=6379

# Flask secrets
SECRET_KEY='gjr39dkjn344_!67#'
FLASK_PORT= 5000
```

## Running the app
* Type the following docker command in the terminal:
```
docker-compose -f docker/docker-compose.yml up -d rabbitmq redis
```

* Start the application by typping the command:

```
PYTHONPATH=$PYTHONPATH:$PWD python main.py
```

* And in order to create users use the command:
```
PYTHONPATH=$PYTHONPATH:$PWD python src/services/user_signup.py --user user --password password
```

* The unit tests use the local Redis database and RabbitMQ. To run the tests just type
```
PYTHONPATH=$PYTHONPATH:$PWD pytest
```

Finally, you can access the chat on `127.0.0.1:5000`
