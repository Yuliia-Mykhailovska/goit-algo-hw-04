from pathlib import Path

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            total = 0
            for line in lines:
                _, salary_str = line.split(',')
                total += int(salary_str)

            average = int(total / len(lines))

            return total, average
        
    except FileNotFoundError:
        print(f'Файл {path} не знайдено')

total, average = total_salary('zp.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
