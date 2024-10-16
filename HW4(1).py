from pathlib import Path 

p = Path('salary_file.txt')

with open(p, 'w') as fh:
    fh.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")

def total_salary(path):
    total_salaries = 0
    count = 0
    
    try:
        with open(p, 'r') as fh:
            for line in fh:
                name, salary = line.strip().split(',')
                total_salaries += int(salary) 
                count += 1 
        
        average_salary = total_salaries / count if count > 0 else 0
        return total_salaries, int(average_salary)

    except FileNotFoundError:
        print(f"Файл {path} не знайден.")
        
    

total, average = total_salary(p)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")