from src import create_app, socketio
from src.utils.config import load_config
from src.chatbot import ChatBot
import threading

def run_app():
    app = create_app(debug=False)
    port = load_config('flask')['port']
    socketio.run(app, port=port)

def run_bot():
    bot = ChatBot()
    bot.run()

if __name__ == '__main__':
    server = threading.Thread(name='webserver', target=run_app)
    chatbot = threading.Thread(name='chatbot', target=run_bot)
    chatbot.start()
    server.start()
