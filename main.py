import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1. Запрос без параметра method (для всех методов)
methods = ["GET", "POST", "PUT", "DELETE"]

for method in methods:
    if method == "GET":
        response = requests.get(url)
    elif method == "POST":
        response = requests.post(url)
    elif method == "PUT":
        response = requests.put(url)
    elif method == "DELETE":
        response = requests.delete(url)

    print(f"{method}-запрос без параметра method:")
    print(f"Текст ответа: {response.text}")

# 2. Http-запрос не из списка - HEAD
print("\n2. Запрос не из списка (HEAD):")
response = requests.head(url)
print(f"HEAD: Status {response.status_code}, Response: {response.text}")  # У HEAD нет тела ответа

# 3. Запрос с правильным значением method
print("\n3. Запрос с правильным значением method")
correct_combinations = [
    ("GET", "GET"),
    ("POST", "POST"),
    ("PUT", "PUT"),
    ("DELETE", "DELETE")
]

for req_method, param_value in correct_combinations:
    if req_method == "GET":
        response = requests.get(url, params={"method": param_value})
    else:
        response = requests.request(req_method, url, data={"method": param_value})

    print(f"{req_method} with method={param_value}: Status {response.status_code}, Response: {response.text}")

#4. Проверка всех возможных сочетаний реальных типов запроса и значений параметра method
print("\n4. Проверка всех сочетаний методов и параметров:")
methods = ["GET", "POST", "PUT", "DELETE"]
param_values = ["GET", "POST", "PUT", "DELETE"]
found_issues = False

for method in methods:
    for param in param_values:
        if method == "GET":
            response = requests.get(url, params={"method": param})
        else:
            response = requests.request(method, url, data={"method": param})

        print(f"{method} with method={param}: Status {response.status_code}, Response: {response.text}")

        # Проверяем несоответствия
        if method != param and "success" in response.text.lower():
            print(f"!!! Найдено несоответствие: {method} запрос с method={param} возвращает успех")
            found_issues = True
        elif method == param and "success" not in response.text.lower():
            print(f"!!! Найдено несоответствие: {method} запрос с method={param} не возвращает успех")
            found_issues = True

if not found_issues:
    print("Несоответствий не найдено")


