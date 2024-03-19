from src.app import app
from src.bot.bot import bot

import threading

import src.bot.imports
import src.imports

if __name__ == "__main__":

    # thread = threading.Thread(target= lambda : bot.polling(none_stop=True, interval=0) , daemon=True)
    # thread.start()

    app.run(host='0.0.0.0' , port=5000)