from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Webserver ok, bot ok"

def run():
  app.run(host="0.0.0.0",port=8000)

def keep_alive():
  t = Thread(target=run)
  t.start()