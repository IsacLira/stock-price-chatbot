
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
* Set the env variables in the `.env` file.

## Running the app
* Start the server by typping at the project root:
```python
PYTHONPATH=$PYTHONPATH:$PWD python server.py
```
* Run the chatbot by typping the following command:
```python
PYTHONPATH=$PYTHONPATH:$PWD python bot.py
```