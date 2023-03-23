import random
# 36
z = int(input('Введите количество параллелей: '))
for x in range(z):
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

    #Технология
    b = random.randint(1, 6)
    while 1==1:
        if b == 1 and len(Monday) < 1:
            Monday.append('Технология')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 1:
            Tuesday.append('Технология')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 1:
            Thursday.append('Технология')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 1:
            Wednesday.append('Технология')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 1:
            Friday.append('Технология')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 1:
            Saturday.append('Технология')
            break
        else:
            b = random.randint(1, 6)

    #Информатика
    b = random.randint(1, 6)
    while 1==1:
        if b == 1 and len(Monday) < 1:
            Monday.append('Информатика')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 1:
            Tuesday.append('Информатика')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 1:
            Thursday.append('Информатика')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 1:
            Wednesday.append('Информатика')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 1:
            Friday.append('Информатика')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 1:
            Saturday.append('Информатика')
            break
        else:
            b = random.randint(1, 6)

    #ОБЖ
    b = random.randint(1, 6)
    while 1==1:
        if b == 1 and len(Monday) < 1:
            Monday.append('ОБЖ')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 1:
            Tuesday.append('ОБЖ')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 1:
            Thursday.append('ОБЖ')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 1:
            Wednesday.append('ОБЖ')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 1:
            Friday.append('ОБЖ')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 1:
            Saturday.append('ОБЖ')
            break
        else:
            b = random.randint(1, 6)

    #Обществознание
    b = random.randint(1, 6)
    while 1==1:
        if b == 1 and len(Monday) < 2:
            Monday.append('Обществознание')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 2:
            Tuesday.append('Обществознание')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 2:
            Thursday.append('Обществознание')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 2:
            Wednesday.append('Обществознание')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 2:
            Friday.append('Обществознание')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 1:
            Saturday.append('Обществознание')
            break
        else:
            b = random.randint(1, 6)
        
    #Родная литература
    b = random.randint(1, 6)
    while 1==1:
        if b == 1 and len(Monday) < 2:
            Monday.append('Родная литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 2:
            Tuesday.append('Родная литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 2:
            Thursday.append('Родная литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 2:
            Wednesday.append('Родная литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 2:
            Friday.append('Родная литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 1:
            Saturday.append('Родная литература')
            break
        else:
            b = random.randint(1, 6)

    #Биология
    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 3:
            Monday.append('Биология')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 3:
            Tuesday.append('Биология')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 3:
            Thursday.append('Биология')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 3:
            Wednesday.append('Биология')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 3:
            Friday.append('Биология')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 2:
            Saturday.append('Биология')
            break
        else:
            b = random.randint(1, 6)

    
    b = random.randint(1, 6)
    while 1==1:
        #2 раз
        if b == 1 and len(Monday) < 3:
            Monday.append('Биология')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 3:
            Tuesday.append('Биология')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 3:
            Thursday.append('Биология')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 3:
            Wednesday.append('Биология')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 3:
            Friday.append('Биология')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 2:
            Saturday.append('Биология')
            break
        else:
            b = random.randint(1, 6)    
    
    #Химия
    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 3:
            Monday.append('Химия')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 3:
            Tuesday.append('Химия')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 3:
            Thursday.append('Химия')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 3:
            Wednesday.append('Химия')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 3:
            Friday.append('Химия')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 2:
            Saturday.append('Химия')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #2 раз
        if b == 1 and len(Monday) < 3:
            Monday.append('Химия')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 3:
            Tuesday.append('Химия')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 3:
            Thursday.append('Химия')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 3:
            Wednesday.append('Химия')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 3:
            Friday.append('Химия')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 2:
            Saturday.append('Химия')
            break
        else:
            b = random.randint(1, 6)

    #География
    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 4:
            Monday.append('География')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 4:
            Tuesday.append('География')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 4:
            Thursday.append('География')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 4:
            Wednesday.append('География')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 4:
            Friday.append('География')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 4:
            Saturday.append('География')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #2 раз
        if b == 1 and len(Monday) < 4:
            Monday.append('География')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 4:
            Tuesday.append('География')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 7:
            Thursday.append('География')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 4:
            Wednesday.append('География')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 4:
            Friday.append('География')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 3:
            Saturday.append('География')
            break
        else:
            b = random.randint(1, 6)

    #Геометрия
    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 4:
            Monday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 4:
            Tuesday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 4:
            Thursday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 4:
            Wednesday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 4:
            Friday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 3:
            Saturday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #2 раз
        if b == 1 and len(Monday) < 5 and Monday.count('Геометрия')<1:
            Monday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 5 and Tuesday.count('Геометрия')<1:
            Tuesday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 5 and Thursday.count('Геометрия')<1:
            Thursday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 5 and Wednesday.count('Геометрия')<1:
            Wednesday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 5 and Friday.count('Геометрия')<1:
            Friday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 4 and Saturday.count('Геометрия')<1:
            Saturday.append('Геометрия')
            break
        else:
            b = random.randint(1, 6)

    #Родной язык
    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 4:
            Monday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 4:
            Tuesday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 4:
            Thursday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 4:
            Wednesday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 4:
            Friday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 4:
            Saturday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #2 раз
        if b == 1 and len(Monday) < 4:
            Monday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 4:
            Tuesday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 4:
            Thursday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 4:
            Wednesday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 4:
            Friday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 3:
            Saturday.append('Родной язык')
            break
        else:
            b = random.randint(1, 6)

    #Русский язык
    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 4:
            Monday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 4:
            Tuesday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 4:
            Thursday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 4:
            Wednesday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 4:
            Friday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 3:
            Saturday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #2 раз
        if b == 1 and len(Monday) < 4:
            Monday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 4:
            Tuesday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 4:
            Thursday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 4:
            Wednesday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 4:
            Friday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 3:
            Saturday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #3 раз
        if b == 1 and len(Monday) < 6 and Monday.count('Русский язык')<1:
            Monday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 6 and Tuesday.count('Русский язык')<1:
            Tuesday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 6 and Thursday.count('Русский язык')<1:
            Thursday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 6 and Wednesday.count('Русский язык')<1:
            Wednesday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 6 and Friday.count('Русский язык')<1:
            Friday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5 and Saturday.count('Русский язык')<1:
            Saturday.append('Русский язык')
            break
        else:
            b = random.randint(1, 6)
        
    #Литература
    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 6:
            Monday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 6:
            Tuesday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 6:
            Thursday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 6:
            Wednesday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 6:
            Friday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5:
            Saturday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #2 раз
        if b == 1 and len(Monday) < 6 and Monday.count('Литература')<1:
            Monday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 6 and Tuesday.count('Литература')<1:
            Tuesday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 6 and Thursday.count('Литература')<1:
            Thursday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 6 and Wednesday.count('Литература')<1:
            Wednesday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 6 and Friday.count('Литература')<1:
            Friday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 4 and Saturday.count('Литература')<1:
            Saturday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #3 раз
        if b == 1 and len(Monday) < 6 and Monday.count('Литература')<1:
            Monday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 6 and Tuesday.count('Литература')<1:
            Tuesday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 6 and Thursday.count('Литература')<1:
            Thursday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 6 and Wednesday.count('Литература')<1:
            Wednesday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 6 and Friday.count('Литература')<1:
            Friday.append('Литература')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 4 and Saturday.count('Литература')<1:
            Saturday.append('Литература')
            break
        else:
            b = random.randint(1, 6)

    #Английский язык
    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 5:
            Monday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 5:
            Tuesday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 5:
            Thursday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 5:
            Wednesday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 5:
            Friday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 4:
            Saturday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #2 раз
        if b == 1 and len(Monday) < 6 and Monday.count('Английский язык')<1:
            Monday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 6 and Tuesday.count('Английский язык')<1:
            Tuesday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 6 and Thursday.count('Английский язык')<1:
            Thursday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 6 and Wednesday.count('Английский язык')<1:
            Wednesday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 6 and Friday.count('Английский язык')<1:
            Friday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5 and Saturday.count('Английский язык')<1:
            Saturday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #3 раз
        if b == 1 and len(Monday) < 6 and Monday.count('Английский язык')<2:
            Monday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 6 and Tuesday.count('Английский язык')<2:
            Tuesday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 6 and Thursday.count('Английский язык')<2:
            Thursday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 6 and Wednesday.count('Английский язык')<2:
            Wednesday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 6 and Friday.count('Английский язык')<2:
            Friday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5 and Saturday.count('Английский язык')<2:
            Saturday.append('Английский язык')
            break
        else:
            b = random.randint(1, 6)

    #Алгебра
    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 5:
            Monday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 5:
            Tuesday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 5:
            Thursday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 5:
            Wednesday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 5:
            Friday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 4:
            Saturday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #2 раз
        if b == 1 and len(Monday) < 6 and Monday.count('Алгебра')<1:
            Monday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 6 and Tuesday.count('Алгебра')<1:
            Tuesday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 6 and Thursday.count('Алгебра')<1:
            Thursday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 6 and Wednesday.count('Алгебра')<1:
            Wednesday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 6 and Friday.count('Алгебра')<1:
            Friday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5 and Saturday.count('Алгебра')<1:
            Saturday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #3 раз
        if b == 1 and len(Monday) < 6 and Monday.count('Алгебра')<1:
            Monday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 6 and Tuesday.count('Алгебра')<1:
            Tuesday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 6 and Thursday.count('Алгебра')<1:
            Thursday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 6 and Wednesday.count('Алгебра')<1:
            Wednesday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 7 and Friday.count('Алгебра')<1:
            Friday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5 and Saturday.count('Алгебра')<1:
            Saturday.append('Алгебра')
            break
        else:
            b = random.randint(1, 6)

    #История
    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 5:
            Monday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 5:
            Tuesday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 5:
            Thursday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 5:
            Wednesday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 5:
            Friday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 4:
            Saturday.append('История')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #2 раз
        if b == 1 and len(Monday) < 6 and Monday.count('История')<1:
            Monday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 6 and Tuesday.count('История')<1:
            Tuesday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 6 and Thursday.count('История')<1:
            Thursday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 6 and Wednesday.count('История')<1:
            Wednesday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 7 and Friday.count('История')<1:
            Friday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5 and Saturday.count('История')<1:
            Saturday.append('История')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #3 раз
        if b == 1 and len(Monday) < 7 and Monday.count('История')<1:
            Monday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 7 and Tuesday.count('История')<1:
            Tuesday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 7 and Thursday.count('История')<1:
            Thursday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 7 and Wednesday.count('История')<1:
            Wednesday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 7 and Friday.count('История')<1:
            Friday.append('История')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5 and Saturday.count('История')<1:
            Saturday.append('История')
            break
        else:
            b = random.randint(1, 6)
    
    #Физика
    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 6:
            Monday.append('Физика')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 6:
            Tuesday.append('Физика')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 6:
            Thursday.append('Физика')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 6:
            Wednesday.append('Физика')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 6:
            Friday.append('Физика')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 4:
            Saturday.append('Физика')
            break
        else:
            b = random.randint(1, 6)
    k = random.randint(1, 6)
    while 1==1:
        #2 раз
        if k == 1 and len(Monday) < 6:
            Monday.append('Физика')
            break
        else:
            k = random.randint(1, 6)
        if k == 2 and len(Tuesday) < 6:
            Tuesday.append('Физика')
            break
        else:
            k = random.randint(1, 6)
        if k == 3 and len(Thursday) < 6:
            Thursday.append('Физика')
            break
        else:
            k = random.randint(1, 6)
        if k == 4 and len(Wednesday) < 6:
            Wednesday.append('Физика')
            break
        else:
            k = random.randint(1, 6)
        if k == 5 and len(Friday) < 6:
            Friday.append('Физика')
            break
        else:
            k = random.randint(1, 6)
        if k == 6 and len(Saturday) < 5:
            Saturday.append('Физика')
            break
        else:
            k = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #3 раз
        if b == 1 and len(Monday) < 7 and Monday.count('Физика')<1:
            Monday.append('Физика')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 7 and Tuesday.count('Физика')<1:
            Tuesday.append('Физика')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 7 and Thursday.count('Физика')<1:
            Thursday.append('Физика')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 7 and Wednesday.count('Физика')<1:
            Wednesday.append('Физика')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 7 and Friday.count('Физика')<1:
            Friday.append('Физика')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5 and Saturday.count('Физика')<1:
            Saturday.append('Физика')
            break
        else:
            b = random.randint(1, 6)

    #Физическая культура

    b = random.randint(1, 6)
    while 1==1:
        #1 раз
        if b == 1 and len(Monday) < 6:
            Monday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 6:
            Tuesday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 6:
            Thursday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 6:
            Wednesday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 6:
            Friday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5:
            Saturday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #2 раз
        if b == 1 and len(Monday) < 7 and Monday.count('Физическая культура')<1:
            Monday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 7 and Tuesday.count('Физическая культура')<1:
            Tuesday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 7 and Thursday.count('Физическая культура')<1:
            Thursday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 7 and Wednesday.count('Физическая культура')<1:
            Wednesday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 7 and Friday.count('Физическая культура')<1:
            Friday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5 and Saturday.count('Физическая культура')<1:
            Saturday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
    b = random.randint(1, 6)
    while 1==1:
        #3 раз
        if b == 1 and len(Monday) < 7 and Monday.count('Физическая культура')<1:
            Monday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 2 and len(Tuesday) < 7 and Tuesday.count('Физическая культура')<1:
            Tuesday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 3 and len(Thursday) < 7 and Thursday.count('Физическая культура')<1:
            Thursday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 4 and len(Wednesday) < 7 and Wednesday.count('Физическая культура')<1:
            Wednesday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 5 and len(Friday) < 7 and Friday.count('Физическая культура')<1:
            Friday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)
        if b == 6 and len(Saturday) < 5 and Saturday.count('Физическая культура')<1:
            Saturday.append('Физическая культура')
            break
        else:
            b = random.randint(1, 6)

    random.shuffle(Monday)
    random.shuffle(Tuesday)
    random.shuffle(Wednesday)
    random.shuffle(Thursday)
    random.shuffle(Friday)
    random.shuffle(Saturday)

    print('Понедельник :' + str(Monday))
    print('Вторник :' + str(Tuesday))
    print('Среда :' + str(Wednesday))
    print('Четверг :' + str(Thursday))
    print('Пятнца :' + str(Friday))
    print('Суббота :' + str(Saturday))
    print(' ')


    