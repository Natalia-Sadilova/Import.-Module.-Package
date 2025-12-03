import datetime

def calculate_salary():
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Расчет зарплаты сотрудников...")
    print("1. Иванов И.И. - 75 000 руб.")
    print("2. Петров П.П. - 65 000 руб.")
    print("3. Сидоров С.С. - 80 000 руб.")
    print("4. Кузнецова А.В. - 70 000 руб.")
    print(f"ИТОГО выплачено: 290 000 руб.")
    return 290000

if __name__ == '__main__':
    calculate_salary()