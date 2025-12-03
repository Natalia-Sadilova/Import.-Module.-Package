import datetime

def get_employees():
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Получение списка сотрудников...")
    employees = [
        {"id": 1, "name": "Иванов Иван Иванович", "position": "Главный бухгалтер", "department": "Бухгалтерия"},
        {"id": 2, "name": "Петров Петр Петрович", "position": "Экономист", "department": "Планово-экономический отдел"},
        {"id": 3, "name": "Сидоров Сергей Сергеевич", "position": "Аналитик", "department": "Финансовый отдел"},
        {"id": 4, "name": "Кузнецова Анна Владимировна", "position": "Кассир", "department": "Бухгалтерия"}
    ]
    
    print(f"Всего сотрудников: {len(employees)}")
    for emp in employees:
        print(f"  • {emp['name']} - {emp['position']} ({emp['department']})")
    
    return employees

if __name__ == '__main__':
    get_employees()