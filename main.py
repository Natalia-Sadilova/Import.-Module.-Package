import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    print("=" * 50)
    print("Программа 'Бухгалтерия'")
    print("=" * 50)
    
    # Выводим текущую дату
    current_date = datetime.datetime.now()
    print(f"Текущая дата: {current_date.strftime('%d.%m.%Y %H:%M:%S')}")
    
    print("\nЗапуск функций:")
    print("-" * 30)
    
    # Вызываем функцию из salary.py
    print("Вызов функции calculate_salary():")
    calculate_salary()
    
    print("-" * 30)
    
    # Вызываем функцию из people.py
    print("Вызов функции get_employees():")
    get_employees()
    
    print("-" * 30)
    print("Программа завершена!")

if __name__ == '__main__':
    main()