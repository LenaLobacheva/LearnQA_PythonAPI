import json

json_text = '{"message":"And this is a second message"}'
obj = json.loads(json_text)

key = "message"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")