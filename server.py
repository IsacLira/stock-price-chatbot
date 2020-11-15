from src import create_app, socketio
from src.utils.config import load_config

app = create_app(debug=True)

if __name__ == '__main__':
    port = load_config('flask')['port']
    socketio.run(app, port=port)
