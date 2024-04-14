from flask import Flask, jsonify
import requests
import threading
import json
import time

app = Flask(__name__)

def fetch_data():
    global data
    response = requests.get('https://store.transitstat.us/passio_go/rutgers/stations')
    data = response.json()
    print("Data updated at", time.strftime('%H:%M:%S'))

def update_data_every_minute():
    fetch_data()
    threading.Timer(60.0, update_data_every_minute).start()

# Fetch initial data
fetch_data()
# Schedule data update every minute
update_data_every_minute()

@app.route("/busroute", methods=['GET'])
def members():
    return jsonify(data)
    

if __name__ == "__main__":
    app.run(debug=True)
