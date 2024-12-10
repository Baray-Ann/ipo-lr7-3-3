import json #Подключение модуля json 
 
#Создание функции для вызова меню 
def showMenu(): 
    menu=("""Доступные операции:   
    1. Вывести все записи.   
    2. Вывести запись по полю.   
    3. Добавить запись.   
    4. Удалить запись по полю.   
    5. Выйти из программы. """) 
    return menu 

def operationCount(count):
    return count + 1

#Создание функции для вывода информации о всех звездах 
def showStarsInfo(data): 
    for star in data: 
        star_id = star.get("id")  
        star_name = star.get("name")  
        star_constellation = star.get("constellation")  
        star_is_visible = bool(star.get("is_visible"))  
        star_radius = star.get("radius")  
        if star_is_visible == True:  
            visible = "Да"  
        else:  
            visible = "Нет"  
        print(f"""-------------------------------------------------------------  
Номер звезды в списке: {star_id}  
Название звезды: {star_name}  
Созвездие, частью которого является звезда: {star_constellation}  
Видно ли звезду невооруженным взглядом: {visible}  
Солнечный радиус звезды: {star_radius}  
""")
 
#Создание функции для вывода информации об одной звезде 
def findStarById(data): 
    find = False
    id = int(input("Введите номер поля: ")) 
    for star in data: 
        search_id = star.get("id")  
        if id == search_id: 
            find = True  
            star_id = star.get("id")  
            star_name = star.get("name")  
            star_constellation = star.get("constellation")  
            star_is_visible = bool(star.get("is_visible"))  
            star_radius = star.get("radius")  
            if star_is_visible == True:  
                visible = "Да"  
            else:  
                visible = "Нет"  
            print(f"""-------------------------------------------------------------  
Номер звезды в списке: {star_id}  
Название звезды: {star_name}  
Созвездие, частью которого является звезда: {star_constellation}  
Видно ли звезду невооруженным взглядом: {visible}  
Солнечный радиус звезды: {star_radius}  
""")  
    if not find: 
        print()  
        print("Запись не найдена.") 
 
#Создание функции для добавления новой звезды 
def addNewStar(data): 
    new_id = len(data) + 1 
    new_name = input("Введите название звезды: ") 
    new_constellation = input("Введите название созвездия: ") 
    new_is_visible = input("Видно ли звезду невооруженным глазом: ") 
    new_radius = input("Введите солнечный радиус: ") 
 
    new_star = {  
    "id": new_id,  
    "name": new_name,  
    "constellation": new_constellation,  
    "is_": True if new_is_visible.lower() == "да" else False,  
    "radius": new_radius  
    }  
  
    data.append(new_star)  
    with open("stars.json", 'w', encoding='utf-8') as out_file: 
        json.dump(data, out_file, ensure_ascii = False, indent = 2)

#Создание функции для удаления звезды
def deleteStar(data):
    delete_id = int(input("Введите номер записи, которую желаете удалить: ")) 
    find = False 
    for star in data: 
        sought_for_id = star.get("id") 
        if delete_id == sought_for_id: 
            find = True 
            data.remove(star) 
            with open("stars.json", "w",encoding="utf-8") as new_file:
                json.dump(data, new_file, ensure_ascii = False, indent = 4) 
                break 
    if not find: 
        print() 
        print("Запись не найдена.")

#Создание функции для выхода из программы
def exitTheProgram():
    print()  
    print(f"Выход из программы. Кол-во операций: {count}")  
    print()

with open("stars.json", 'r', encoding='utf-8') as file: 
    data = json.load(file) 

    count = 0

    while True: 
        print(showMenu())

        num = int(input("Введите номер пункта который хотите выполнить: ")) 

        if num == 1:
            showStarsInfo(data)
            count = operationCount(count)

        elif num == 2:
            findStarById(data)
            count = operationCount(count)

        elif num == 3:
            addNewStar(data)
            count = operationCount(count)
        
        elif num == 4:
            deleteStar(data)
            count = operationCount(count)

        elif num == 5:
            exitTheProgram()
            break

        else:
            print("Ввведено неверное число.")