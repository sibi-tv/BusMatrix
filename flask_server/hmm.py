from flask import jsonify
import requests

response = requests.get('https://store.transitstat.us/passio_go/rutgers/stations')
data = response.json()

# Test jsonify by passing the data
json_data = jsonify(data)

# Print the JSON data
print(json_data)