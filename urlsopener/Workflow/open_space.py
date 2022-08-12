import os
import sys
import json


data = {"items": [] }

for f in os.listdir('./'):
	if f.endswith('.txt'):
		name = f.replace('.txt', '')
		data["items"].append({ 'title': name, 'arg': name})


json_string = json.dumps(data)

sys.stdout.write(json_string)
