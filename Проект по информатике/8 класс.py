import random

# Понедельник:
Monday = ["Алгебра", "Геометрия", "Русский язык", "Физика", "Химия", "Информатика", "География",
          "История", "Обществознание", "Физ-ра", "Биология", "Изо", "ОБЖ", "Английский язык", "Музыка"]
k = random.randint(6, 8)
aMonday = random.sample(Monday, k)
AlgebraMonday = aMonday.count("Алгебра")
GeometryMonday = aMonday.count("Геометрия")
RussiaMonday = aMonday.count("Русский язык")
PhysicsMonday = aMonday.count("Физика")
ChemistryMonday = aMonday.count("Химия")
InformaticsMonday = aMonday.count("Информатика")
GeographyMonday = aMonday.count("География")
HistoryMonday = aMonday.count("История")
SocialMonday = aMonday.count("Обществознание")

# Вторник:
Tuesday = ["Алгебра", "Геометрия", "Русский язык", "Физика", "Химия", "Информатика",
           "География", "История", "Обществознание", "Физ-ра", "Биология", "Изо", "ОБЖ", "Английский язык", "Музыка"]
k = random.randint(6, 8)
aTuesday = random.sample(Tuesday, k)
AlgebraTuesday = aTuesday.count("Алгебра")
GeometryTuesday = aTuesday.count("Геометрия")
RussiaTuesday = aTuesday.count("Русский язык")
PhysicsTuesday = aTuesday.count("Физика")
ChemistryTuesday = aTuesday.count("Химия")
InformaticsTuesday = aTuesday.count("Информатика")
GeographyTuesday = aTuesday.count("География")
HistoryTuesday = aTuesday.count("История")
SocialTuesday = aTuesday.count("Обществознание")

# Среда:
Wednesday = ["Алгебра", "Геометрия", "Русский язык", "Физика", "Химия", "Информатика",
             "География", "История", "Обществознание", "Физ-ра", "Биология", "Изо", "ОБЖ", "Английский язык", "Музыка"]
k = random.randint(6, 8)
aWednesday = random.sample(Wednesday, k)
AlgebraWednesday = aWednesday.count("Алгебра")
GeometryWednesday = aWednesday.count("Геометрия")
RussiaWednesday = aWednesday.count("Русский язык")
PhysicsWednesday = aWednesday.count("Физика")
ChemistryWednesday = aWednesday.count("Химия")
InformaticsWednesday = aWednesday.count("Информатика")
GeographyWednesday = aWednesday.count("География")
HistoryWednesday = aWednesday.count("История")
SocialWednesday = aWednesday.count("Обществознание")


# Четверг:
Thursday = ["Алгебра", "Геометрия", "Русский язык", "Физика", "Химия", "Информатика",
            "География", "История", "Обществознание", "Физ-ра", "Биология", "Изо", "ОБЖ", "Английский язык", "Музыка"]
k = random.randint(6, 8)
aThursday = random.sample(Thursday, k)
AlgebraThursday = aThursday.count("Алгебра")
GeometryThursday = aThursday.count("Геометрия")
RussiaThursday = aThursday.count("Русский язык")
PhysicsThursday = aThursday.count("Физика")
ChemistryThursday = aThursday.count("Химия")
InformaticsThursday = aThursday.count("Информатика")
GeographyThursday = aThursday.count("География")
HistoryThursday = aThursday.count("История")
SocialThursday = aThursday.count("Обществознание")


# Пятница:
Friday = ["Алгебра", "Геометрия", "Русский язык", "Физика", "Химия", "Информатика", "География",
          "История", "Обществознание", "Физ-ра", "Биология", "Изо", "ОБЖ", "Английский язык", "Музыка"]
k = random.randint(6, 8)
aFriday = random.sample(Friday, k)
AlgebraFriday = aFriday.count("Алгебра")
GeometryFriday = aFriday.count("Геометрия")
RussiaFriday = aFriday.count("Русский язык")
PhysicsFriday = aFriday.count("Физика")
ChemistryFriday = aFriday.count("Химия")
InformaticsFriday = aFriday.count("Информатика")
GeographyFriday = aFriday.count("География")
HistoryFriday = aFriday.count("История")
SocialFriday = aFriday.count("Обществознание")


# Суббота:
Saturday = ["Алгебра", "Геометрия","Русский язык", "Физика", "Химия", "Информатика",
            "География", "История", "Обществознание", "Физ-ра", "Биология", "Изо", "ОБЖ", "Английский язык", "Музыка"]
k = random.randint(6, 8)
aSaturday = random.sample(Saturday, k)
AlgebraSaturday = aSaturday.count("Алгебра")
GeometrySaturday = aSaturday.count("Геометрия")
RussiaSaturday = aSaturday.count("Русский язык")
PhysicsSaturday = aSaturday.count("Физика")
ChemistrySaturday = aSaturday.count("Химия")
InformaticsSaturday = aSaturday.count("Информатика")
GeographySaturday = aSaturday.count("География")
HistorySaturday = aSaturday.count("История")
SocialSaturday = aSaturday.count("Обществознание")

Algebra = AlgebraMonday + AlgebraTuesday + AlgebraWednesday + AlgebraThursday + AlgebraFriday + AlgebraSaturday
Geometry = GeometryMonday + GeometryTuesday + GeometryWednesday + GeometryThursday + GeometryFriday + GeometrySaturday
Russia = RussiaMonday + RussiaTuesday + RussiaWednesday + RussiaThursday + RussiaFriday + RussiaSaturday
Physics = PhysicsMonday + PhysicsTuesday + PhysicsWednesday + PhysicsThursday + PhysicsFriday + PhysicsSaturday
Chemistry = ChemistryMonday + ChemistryTuesday + ChemistryWednesday + ChemistryThursday + ChemistryFriday + ChemistrySaturday
Informatics = InformaticsMonday + InformaticsTuesday + InformaticsWednesday + InformaticsThursday + InformaticsFriday + InformaticsSaturday
Geography = GeographyMonday + GeographyTuesday + GeographyWednesday + GeographyThursday + GeographyFriday + GeographySaturday
History = HistoryMonday + HistoryTuesday + HistoryWednesday + HistoryThursday + HistoryFriday + HistorySaturday
Social = SocialMonday + SocialTuesday + SocialWednesday + SocialThursday + SocialFriday + SocialSaturday


if Algebra == 4 and Geometry == 2 and Russia == 3 and Physics == 2 and Chemistry == 2 and Informatics == 1 and Geography == 2 and History == 2 and Social == 1:
    print('Понедельник :' + str(aMonday))
    print('Вторник :' + str(aTuesday))
    print('Среда :' + str(aWednesday))
    print('Четверг :' + str(aThursday))
    print('Пятница :' + str(aFriday))
    print('Суббота :' + str(aSaturday))
else:
    while 1==1 :
        
        a1Monday = random.sample(Monday, k)
        AlgebraMonday = a1Monday.count("Алгебра")
        GeometryMonday = a1Monday.count("Геометрия")
        RussiaMonday = a1Monday.count("Русский язык")
        PhysicsMonday = a1Monday.count("Физика")
        ChemistryMonday = a1Monday.count("Химия")
        InformaticsMonday = a1Monday.count("Информатика")
        GeographyMonday = a1Monday.count("География")
        HistoryMonday = a1Monday.count("История")
        SocialMonday = a1Monday.count("Обществознание")
            
        a1Tuesday = random.sample(Tuesday, k)
        AlgebraTuesday = a1Tuesday.count("Алгебра")
        GeometryTuesday = a1Tuesday.count("Геометрия")
        RussiaTuesday = a1Tuesday.count("Русский язык")
        PhysicsTuesday = a1Tuesday.count("Физика")
        ChemistryTuesday = a1Tuesday.count("Химия")
        InformaticsTuesday = a1Tuesday.count("Информатика")
        GeographyTuesday = a1Tuesday.count("География")
        HistoryTuesday = a1Tuesday.count("История")
        SocialTuesday = a1Tuesday.count("Обществознание")

        a1Wednesday = random.sample(Wednesday, k)
        AlgebraWednesday = a1Wednesday.count("Алгебра")
        GeometryWednesday = a1Wednesday.count("Геометрия")
        RussiaWednesday = a1Wednesday.count("Русский язык")
        PhysicsWednesday = a1Wednesday.count("Физика")
        ChemistryWednesday = a1Wednesday.count("Химия")
        InformaticsWednesday = a1Wednesday.count("Информатика")
        GeographyWednesday = a1Wednesday.count("География")
        HistoryWednesday = a1Wednesday.count("История")
        SocialWednesday = a1Wednesday.count("Обществознание")

        a1Thursday = random.sample(Thursday, k)
        AlgebraThursday = a1Thursday.count("Алгебра")
        GeometryThursday = a1Thursday.count("Геометрия")
        RussiaThursday = a1Thursday.count("Русский язык")
        PhysicsThursday = a1Thursday.count("Физика")
        ChemistryThursday = a1Thursday.count("Химия")
        InformaticsThursday = a1Thursday.count("Информатика")
        GeographyThursday = a1Thursday.count("География")
        HistoryThursday = a1Thursday.count("История")
        SocialThursday = a1Thursday.count("Обществознание")

        a1Friday = random.sample(Friday, k)
        AlgebraFriday = a1Friday.count("Алгебра")
        GeometryFriday = a1Friday.count("Геометрия")
        RussiaFriday = a1Friday.count("Русский язык")
        PhysicsFriday = a1Friday.count("Физика")
        ChemistryFriday = a1Friday.count("Химия")
        InformaticsFriday = a1Friday.count("Информатика")
        GeographyFriday = a1Friday.count("География")
        HistoryFriday = a1Friday.count("История")
        SocialFriday = a1Friday.count("Обществознание")


        a1Saturday = random.sample(Saturday, k)
        AlgebraSaturday = a1Saturday.count("Алгебра")
        GeometrySaturday = a1Saturday.count("Геометрия")
        RussiaSaturday = a1Saturday.count("Русский язык")
        PhysicsSaturday = a1Saturday.count("Физика")
        ChemistrySaturday = a1Saturday.count("Химия")
        InformaticsSaturday = a1Saturday.count("Информатика")
        GeographySaturday = a1Saturday.count("География")
        HistorySaturday = a1Saturday.count("История")
        SocialSaturday = a1Saturday.count("Обществознание")

        Algebra1 = AlgebraMonday + AlgebraTuesday + AlgebraWednesday + AlgebraThursday + AlgebraFriday + AlgebraSaturday
        Geometry1 = GeometryMonday + GeometryTuesday + GeometryWednesday + GeometryThursday + GeometryFriday + GeometrySaturday
        Russia1 = RussiaMonday + RussiaTuesday + RussiaWednesday + RussiaThursday + RussiaFriday + RussiaSaturday
        Physics1 = PhysicsMonday + PhysicsTuesday + PhysicsWednesday + PhysicsThursday + PhysicsFriday + PhysicsSaturday
        Chemistry1 = ChemistryMonday + ChemistryTuesday + ChemistryWednesday + ChemistryThursday + ChemistryFriday + ChemistrySaturday
        Informatics1 = InformaticsMonday + InformaticsTuesday + InformaticsWednesday + InformaticsThursday + InformaticsFriday + InformaticsSaturday
        Geography1 = GeographyMonday + GeographyTuesday + GeographyWednesday + GeographyThursday + GeographyFriday + GeographySaturday
        History1 = HistoryMonday + HistoryTuesday + HistoryWednesday + HistoryThursday + HistoryFriday + HistorySaturday
        Social1 = SocialMonday + SocialTuesday + SocialWednesday + SocialThursday + SocialFriday + SocialSaturday

        if Algebra1==4 and Geometry1 == 2 and Russia1 == 3 and Physics1 == 2 and Chemistry1 == 2 and Informatics1 == 1 and Geography1 == 2 and History1 == 2 and Social1 == 1:
            print('Понедельник :' + str(a1Monday))
            print('Вторник :' + str(a1Tuesday))
            print('Среда :' + str(a1Wednesday))
            print('Четверг :' + str(a1Thursday))
            print('Пятнца :' + str(a1Friday))
            print('Суббота :' + str(a1Saturday))
            break


#Изо 







print('Понедельник :' + str(a1Monday))
print('Вторник :' + str(a1Tuesday))
print('Среда :' + str(a1Wednesday))
print('Четверг :' + str(a1Thursday))
print('Пятнца :' + str(a1Friday))
print('Суббота :' + str(a1Saturday))