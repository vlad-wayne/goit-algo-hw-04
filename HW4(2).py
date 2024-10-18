from pathlib import Path 

p = Path('cats_file.txt')

with open(p, 'w') as fh:
    fh.write("60b90c1c13067a15887e1ae1,Tayson,3\n"
            "60b90c2413067a15887e1ae2,Vika,1\n"
            "60b90c2e13067a15887e1ae3,Barsik,2\n"
            "60b90c3b13067a15887e1ae4,Simon,12\n"
            "60b90c4613067a15887e1ae5,Tessi,5")


def get_cats_info(path):
    cats  = []

    try:
        
        with open(p, 'r') as fh:
            for line in fh:
                cat_id, name, age = line.strip().split(',')
                cats.append({
                            'id': cat_id,
                            'name': name,
                            'age': age
                            }) 
            
        return cats
        
    
    except FileNotFoundError:
        print(f'Файл {path} не знайдено')
        return []
    
    except IOError:
        print(f"Проблема з доступом до файлу {path}.")
        return []
    
    except Exception as e:
        print(f"Сталася неочікувана помилка: {e}")
        return []

cats_info = get_cats_info(p)
print(cats_info)
