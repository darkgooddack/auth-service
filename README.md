# auth-service
Этот сервис предоставляет API для регистрации и аутентификации пользователей в Django с использованием JWT (JSON Web Token).

## Установка и запуск
1. Клонируйте репозиторий

```
git clone <repo_url>
cd auth-service
```
2. Создайте виртуальное окружение и установите зависимости

```
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
pip install -r requirements.txt
```
3. Примените миграции
```
python manage.py migrate
```

4. Запустите сервер
```
python manage.py runserver
```

## 📌 Маршруты API  

### 🔑 Аутентификация  
- **`POST`** `/register/` – Регистрация нового пользователя  
- **`POST`** `/login/` – Получение JWT-токена  
- **`POST`** `/token/refresh/` – Обновление JWT-токена  

### 🧍🏼‍♀️ Пользователь  
- **`GET`** `/user/` – Получение информации о текущем пользователе  


## 📄 Документация API

Swagger и ReDoc доступны по следующим адресам:  

- **Swagger UI:** [`/api/swagger/`](http://localhost:8000/api/swagger/)  
- **ReDoc:** [`/api/redoc/`](http://localhost:8000/api/redoc/)  
- **OpenAPI схема:** [`/api/openapi/`](http://localhost:8000/api/openapi/)  


## 🚀 Используемые технологии

- **Django Rest Framework (DRF)** – мощный фреймворк для создания REST API  
- **JWT (Simple JWT)** – аутентификация с использованием JSON Web Token  
- **OpenAPI (Swagger, ReDoc)** – авто-документация API для удобного взаимодействия  
