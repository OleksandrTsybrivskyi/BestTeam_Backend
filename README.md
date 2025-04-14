# BestTeam_Backend

Реалізація backend-частини тестового завдання з використанням фреймвоку **Django Rest Framework** для управління локаціями з врахуванням доступності для людей з інвалідністю та відгуками користувачів.

## Білд та налаштування проекту

### *Клонування*
1. Заходимо в термінал та вводимо команду. <br/>

```bash
    git clone https://github.com/OleksandrTsybrivskyi/BestTeam_Backend.git
```
для клонування репозиторію.


2. Переходимо в директорію. 
```bash
   cd BestTeam_Backend
```

### *Створення та активація venv*

Директорія **venv** необхідна для установлення віртуального середовища Python-проекту. 

1. Вводимо команду для створення venv : ```bash python -m venv venv```

2. Активуємо його: 
```bash
     source venv/bin/activate   # для Linux/macOS 

     venv\Scripts\activate  # для Windows 
```

### *Встановлення необхідних бібліотек*

Для завантаження всіх необіхдних для виконання програми модулів та залежностей портібно ввести команду <br/>

```bash pip install -r requirements.txt ```, 
яка починає інсталяцію у venv. 


### *Проведення міграцій*
Перед запуском проекту виконуємо необхідні міграції. <br/>

```bash 
python manage.py makemigrations 

python manage.py migrate
``` 


### *Запуск програми* 

```bash 
python manage.py runserver 
``` 



