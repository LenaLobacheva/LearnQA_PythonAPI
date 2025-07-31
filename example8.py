import requests
import time
import json

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
# 1. Создаем задачу (первый запрос без токена)
print("1. Создаем новую задачу")

response = requests.get(url)
response_data = json.loads(response.text)
print(f"Ответ сервера: {response_data}")

seconds = response_data['seconds']
token = response_data['token']
print(f"Задача создана. Token: {token}, Время выполнения: {seconds} сек")

# 2. Создание одного запроса с token ДО того, как задача готова, убеждение в правильности поля status
print("\n2. Создание одного запроса с token ДО того, как задача готова")

early_check = requests.get(f"https://playground.learnqa.ru/ajax/api/longtime_job?token={token}")
early_data = json.loads(early_check.text)
print(f"Ответ сервера: {early_data}")

if 'status' in early_data and early_data['status'] == "Job is NOT ready":
    print("✓ Статус корректный: задача еще не готова")
else:
    print("✗ Ошибка: неверный статус задачи")

# 3. Ждем указанное количество секунд
print(f"\n3. Ожидаем {seconds} секунд")
time.sleep(seconds)

# 4. Проверяем статус ПОСЛЕ готовности
print("\n4. Проверяем статус ПОСЛЕ готовности...")
final_check = requests.get(f"https://playground.learnqa.ru/ajax/api/longtime_job?token={token}")
final_data = json.loads(final_check.text)
print(f"Ответ сервера: {final_data}")

if 'status' in final_data and final_data['status'] == "Job is ready":
    print("✓ Статус корректный: задача готова")
    if 'result' in final_data:
        print(f"✓ Результат получен: {final_data['result']}")
    else:
        print("✗ Ошибка: отсутствует результат")
else:
    print("✗ Ошибка: неверный статус задачи")