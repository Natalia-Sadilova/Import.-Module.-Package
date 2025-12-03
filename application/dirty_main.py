import datetime

# Импорт всех функций из модулей
from application.salary import *
from application.db.people import *

def main():
    print("=" * 50)
    print("Программа 'Бухгалтерия' (dirty import version)")
    print("=" * 50)
    
    # Выводим текущую дату
    current_date = datetime.datetime.now()
    print(f"Текущая дата: {current_date.strftime('%d.%m.%Y %H:%M:%S')}")
    
    print("\nЗапуск функций через import *:")
    print("-" * 30)
    
    # Вызываем функцию из salary.py
    print("Вызов функции calculate_salary():")
    calculate_salary()
    
    print("-" * 30)
    
    # Вызываем функцию из people.py
    print("Вызов функции get_employees():")
    get_employees()
    
    print("-" * 30)
    
    # Демонстрация проблемы с импортом *
    print("\nПроверка глобального пространства имен:")
    print(f"calculate_salary в globals(): {'calculate_salary' in globals()}")
    print(f"get_employees в globals(): {'get_employees' in globals()}")
    
    print("-" * 30)
    print("Программа завершена!")

if __name__ == '__main__':
    main()