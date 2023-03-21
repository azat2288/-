import random
# 36

# Понедельник:
# Monday = ["Алгебра", "Геометрия", "Русский язык", "Физика", "Химия", "Информатика", "География",
#           "История", "Обществознание", "Физ-ра", "Биология", "Изо", "ОБЖ", "Английский язык", "Музыка"]

Monday = []
# Вторник:
Tuesday = []
# Среда:
Wednesday = []
# Четверг:
Thursday = []
# Пятница:
Friday = []
# Суббота:
Saturday = []

# if Algebra == 4 and Geometry == 2 and Russia == 3 and Physics == 2 and Chemistry == 2 and Informatics == 1 and Geography == 2 and History == 2 and Social == 1 and PE == 3 and Biology == 2 and Art == 1 and Music == 1:

# Изо
b = random.randint(1, 6)
while 1==1:
    if b == 1 and len(Monday) < 7:
        Monday.append('Изо')
        break
    else:
        b = random.randint(1, 6)
    if b == 2 and len(Tuesday) < 7:
        Tuesday.append('Изо')
        break
    else:
        b = random.randint(1, 6)
    if b == 3 and len(Thursday) < 7:
        Thursday.append('Изо')
        break
    else:
        b = random.randint(1, 6)
    if b == 4 and len(Wednesday) < 7:
        Wednesday.append('Изо')
        break
    else:
        b = random.randint(1, 6)
    if b == 5 and len(Friday) < 7:
        Friday.append('Изо')
        break
    else:
        b = random.randint(1, 6)
    if b == 6 and len(Saturday) < 6:
        Saturday.append('Изо')
        break
    else:
        b = random.randint(1, 6)

#Информатика
b = random.randint(1, 6)
while 1==1:
    if b == 1 and len(Monday) < 7:
        Monday.append('Информатика')
        break
    else:
        b = random.randint(1, 6)
    if b == 2 and len(Tuesday) < 7:
        Tuesday.append('Информатика')
        break
    else:
        b = random.randint(1, 6)
    if b == 3 and len(Thursday) < 7:
        Thursday.append('Информатика')
        break
    else:
        b = random.randint(1, 6)
    if b == 4 and len(Wednesday) < 7:
        Wednesday.append('Информатика')
        break
    else:
        b = random.randint(1, 6)
    if b == 5 and len(Friday) < 7:
        Friday.append('Информатика')
        break
    else:
        b = random.randint(1, 6)
    if b == 6 and len(Saturday) < 6:
        Saturday.append('Информатика')
        break
    else:
        b = random.randint(1, 6)

print('Понедельник :' + str(Monday))
print('Вторник :' + str(Tuesday))
print('Среда :' + str(Wednesday))
print('Четверг :' + str(Thursday))
print('Пятнца :' + str(Friday))
print('Суббота :' + str(Saturday))
