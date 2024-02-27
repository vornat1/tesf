
fail = input('введите имя файла')
try:
    with open(fail,'r',encoding='utf-8')as f1:
        data = file.readlines()
        print(data)
except FileNotFoundError:
    with open(fail, 'w', encoding='utf-8')as f1:
            

