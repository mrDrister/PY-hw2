'''#task 1
day = int(input("Введите число дня недели:"))
if day == 1:
    print("Понедельник")
if day == 2:
    print("Вторник")
if day == 3:
    print("Среда")
if day == 4:
    print("Четверг")
if day == 5:
    print("Пятница")
if day == 6:
    print("Суббота")
if day == 7:
    print("Воскресенье")
elif day >=8:
    print("Введите число от 1 до 7")
    '''
''' #task 3
price = float(input("Введите цену товара:"))
age = int(input("Введите ваш возраст:"))
if age < 18: 
    print(price - (price * 0.1))
if age >= 18 and age <= 60: 
    print(price - (price * 0.05))
if age > 60: 
    print(price - (price * 0.15))    
    '''
'''#task 4
subject1 = int(input("Введите оценку с математики:"))
subject2 = int(input("Введите оценку с английского:"))
subject3 = int(input("Введите оценку с физики:"))
if subject1 >= 4 and subject2 >= 4 and subject3 >= 4:
    print("Отлично")
elif subject1 == 0 or subject1 >= 6:
    print("Ошибка, введите оценки от 1 до 5")
elif subject2 == 0 or subject2 >= 6:
    print("Ошибка, введите оценки от 1 до 5")
elif subject3 == 0 or subject3 >= 6:
    print("Ошибка, введите оценки от 1 до 5")
else:
    print("Неудовлетворительно")
'''
'''#task5
subject1 = int(input("Введите оценку с математики:"))
subject2 = int(input("Введите оценку с английского:"))
subject3 = int(input("Введите оценку с физики:"))
subject4 = int(input("Введите оценку с информатики:"))
if subject1 >= 4 and subject2 >= 4 and subject3 >= 4 and subject4 >= 4:
    print("Допущен с отличием")
elif subject1 < 3 or subject2 < 3 or subject3 < 3 or subject4 < 3:
    print("Не допущен")
elif subject1 == 0 or subject1 >= 6:
    print("Ошибка, введите оценки от 1 до 5")
elif subject2 == 0 or subject2 >= 6:
    print("Ошибка, введите оценки от 1 до 5")
elif subject3 == 0 or subject3 >= 6:
    print("Ошибка, введите оценки от 1 до 5")
elif subject4 == 0 or subject4 >= 6:
    print("Ошибка, введите оценки от 1 до 5")      
else:
    print("Допущен")
'''