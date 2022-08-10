from app import create_app, socketio

app = create_app()
socketio.async_mode = True

if __name__ == "__main__":

    socketio.run(app=app, host='0.0.0.0', debug=True)
