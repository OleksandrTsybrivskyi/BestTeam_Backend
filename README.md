# BestTeam_Backend

Реалізація backend-частини тестового завдання з використанням фреймвоку **Django Rest Framework** для управління локаціями з врахуванням доступності для людей з інвалідністю та відгуками користувачів.

## Білд та налаштування проекту

### *Клонування*
1. Заходимо в термінал та вводимо команду <br/>

    **git clone https://github.com/OleksandrTsybrivskyi/BestTeam_Backend.git** для клонування репозиторію

2. Переходимо в директорію 

   **cd BestTeam_Backend**

### **Створення та активація venv**

Директорія **venv** необхідна для установлення віртуального середовища Python-проекту. 

1. Вводимо команду для створення venv : **python -m venv venv**   

2. Активуємо його: 

     **source venv/bin/activate**   # для Linux/macOS <br/>

     **venv\Scripts\activate**  # для Windows <br/>

### **Встановлення необіхдних бібліотек**

Для завантаження всіх необіхдних для виконання програми модулів та залежностей портібно ввести команду <br/>
**pip install -r requirements.txt** , 
яка починає інсталяцію у venv. 


### **Проведення міграцій**
Перед запуском проекту виконуємо необхідні міграції <br/>

**python manage.py makemigrations** <br/>

**python manage.py migrate** <br/>


### **Запуск програми** 
**python manage.py runserver** 



