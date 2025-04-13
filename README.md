# BestTeam_Backend


Бекенд-частина тестового завдання на  **Django** для управління локаціями з врахуванням доступності для людей з інвалідністю та відгуками користувачів.

# Клонування репозиторію
```bash
git clone https://github.com/твій-репозиторій.git
cd BestTestProject

 Створення та активація venv

python -m venv venv   # Створення файлу .venv
source venv/bin/activate        # для Linux/macOS
venv\Scripts\activate           # для Windows

### Встановлення необіхдних бібліотек 
pip install -r requirements.txt


### Проведення міграцій 
python manage.py makemigrations
python manage.py migrate


Запуск локального сервера
python manage.py runserver
