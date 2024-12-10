
class Item:
    Name = str() # строка-имя предмета
    Tag = str()  # строка-тип предмета
        # возможные значения: Artifact, Artisan Item, Fervor Stone, Relic, Runic Catalyst, Trinket, Legendary Item,
        # Mythical Weapon, Fragment of Mythical Weapon, Lore Book.
    Coordinates = list()  # список наборов координат в текстовом формате
        #(числа с округлением до десятых; наборов координат может быть больше одного, если предмет не уникален)
    Base_Item = str() # строка, в которой может быть указан ванильный предмет, на основе которого сделан данный
    Attack_Damage = str() # урон в целых числах
    Attack_Speed = str() # скорость атаки в в иде числа с округлением до десятых
    Ability = str()  # строка-описание способности (для лег и миф предметов)
    Armor = str() # показатель брони в целых числах
    Armor_Toughness = str() # показатель твёрдости брони в целых числах
    Enchantments = list() # список строк-зачарований
    Bonus_Stats = list() # списока строк-бонусов
    Obtain = list() # набор длинных строк с описанием получения предмета и, возможно, дополнительным описанием

    def reset(self): # функция, помогающая сбрасывать значения объекта из класса
        self.Name = '#NO_INFO'
        self.Tag = '#NO_INFO'
        self.Coordinates = ['#NO_INFO']
        self.Base_Item = '#NO_INFO'
        self.Attack_Damage = '#NO_INFO'
        self.Attack_Speed = '#NO_INFO'
        self.Ability = '#NO_INFO'
        self.Armor = '#NO_INFO'
        self.Armor_Toughness = '#NO_INFO'
        self.Enchantments = ['#NO_INFO']
        self.Bonus_Stats = ['#NO_INFO']
        self.Obtain = ['#NO_INFO']


def write_title_string(file):
    title_string = ('Name;Tag;Coordinates;Base Item;Attack Damage;Attack Speed;Ability;Armor;Armor Toughness;' +
                    'Enchantments;Bonus Stats;Obtain')
    file.write(title_string + '\n')
def reimagination1(pre_file, res_file):
    """
    Функция получает 2 файла: файл на чтение и файл на заполнение.
    Работает для документов Artifacts, ArtisanItems, LegendaryItems, MythicalWeapons.
    Строки с '# ' - категория предмета, строки с '### ' - название предмета
    У лег и миф оружий могут быть Ability (одна или несколько) - текст с описанием.
    У ArtisianItems есть строки Cost, которые надо перезаписывать в object.Obtain.
    Также там есть строки с '## ' - в них написана локация (т.е. Coordinates и Obtain)
    """

    object = Item()
    number_of_obj1 = 0 # считаем число объектов + с его помощью не печатаем в начале документа пустой элемент класса
    location_info_string = '' # в ArtisanItems после '## ' идёт строка с информацией о нахождении ремесленника
    coord_string_AI = '#NO_INFO' # если в файле было две решётки, то нужно обнулить значение этой строки

    for initial_line in pre_file:
        line=initial_line.strip('\n').strip(' ')

        if line.startswith('# '): # в файлах одна решётка означает группу предметов
            tag = line[1:].strip(' ')

        if line.startswith('## '): # две решётки означают локацию (см описание функции), только для ArtisianItems
            location_info_string = line[3:]
            coord_right_AI = location_info_string.rfind('*') - 1  # получаем индекс правой скобки набора координат + 1
            coord_left_AI = location_info_string.find('*') + 2  # получаем индекс левой скобки набора координат
            coord_string_AI = location_info_string[coord_left_AI: coord_right_AI]
            location_info_string = location_info_string.replace('*', '').replace(']', '').replace('[', '')

        if line.startswith('### '): # в файлах три решётки означают название предмета
            # если нашли новый предмет, то старый добавляем в файл, сбрасываем object и задаём новые параметры
            obj_string = (object.Name + ';' + object.Tag + ';' + str(object.Coordinates) + ';' + object.Base_Item
                          + ';' + str(object.Attack_Damage) + ';' + str(object.Attack_Speed) + ';'
                          + object.Ability + ';' + str(object.Armor) + ';' + str(object.Armor_Toughness)
                          + ';' + str(object.Enchantments) + ';' + str(object.Bonus_Stats) + ';' + str(object.Obtain))
            if number_of_obj1 > 0:
                res_file.write(obj_string + '\n')
            number_of_obj1 += max(1, len(object.Coordinates))

            object.reset()
            object.Tag = tag
            object.Name = line[4:].strip(' ')
            if object.Name == '':
                object.Name = 'NO_INFO'
            object.Coordinates = [coord_string_AI] # на случай, если в документе две решётки

        if line.startswith('#### '):
            # четыре решётки означают фрагмент миф предмета
            obj_string = (object.Name + ';' + object.Tag + ';' + str(object.Coordinates) + ';' + object.Base_Item
                          + ';' + str(object.Attack_Damage) + ';' + str(object.Attack_Speed) + ';'
                          + object.Ability + ';' + str(object.Armor) + ';' + str(object.Armor_Toughness)
                          + ';' + str(object.Enchantments) + ';' + str(object.Bonus_Stats) + ';' + str(object.Obtain))
            res_file.write(obj_string + '\n')
            number_of_obj1 += max(1, len(object.Coordinates))

            object.reset()
            object.Tag = 'Fragment of Mythical Weapon'
            object.Name = line[5:].strip(' ')

        if line.startswith('| **Base Item'):
            line = line.strip('|')
            left = line.find('|')
            string = line[left + 1:].strip(' ')
            object.Base_Item = string

        if line.startswith('| **Armor**'):
            line = line.strip('|')
            left = line.find('|')
            string = line[left + 1:].strip(' ')
            object.Armor = string

        if line.startswith('| **Armor Toughness'):
            line = line.strip('|')
            left = line.find('|')
            string = line[left + 1:].strip(' ')
            object.Armor_Toughness = string

        if line.startswith('| **Attack Damage'):
            line = line.strip('|')
            left = line.find('|')
            string = line[left + 1:].strip(' ')
            object.Attack_Damage = string

        if line.startswith('| **Attack Speed'):
            line = line.strip('|')
            left = line.find('|')
            string = line[left + 1:].strip(' ')
            object.Attack_Speed = string

        if line.startswith('| **Ability'):
            line = line.strip('|')
            left = line.find('|')
            string = line[left + 1:].strip(' ').replace('*', '').replace(' <br>', '').replace('[^1]', '')
            object.Ability = string

        if line.startswith('| **Enchantments'):
            line = line.strip('|')
            left = line.find('|')
            string = line[left + 1:].strip(' ')
            object.Enchantments = string.split(' <br>')

        if line.startswith('| **Bonus Stats') or line.startswith('| Stats'):
            line = line.strip('|')
            left = line.find('|')
            string = line[left + 1:].strip(' ')
            object.Bonus_Stats = string.split(' <br>')

        if line.startswith('| **Obtain'):
            line = line.strip('|')
            left = line.find('|')
            string = line[left + 1:].strip(' ')
            string = string.replace('[[', '').replace(']]', '')

            if string.count('**') > 1:  # если в тексте есть координаты (они выделены ** **), то отдельно ищем их
                coord_right = string.rfind('*') - 1  # получаем индекс правой скобки набора координат + 1
                coord_left = string.find('*') + 2  # получаем индекс левой скобки набора координат
                coord_string = string[coord_left: coord_right]
                object.Coordinates.append(coord_string)
                if '#NO_INFO' in object.Coordinates:
                    object.Coordinates.remove('#NO_INFO')

            string = string.replace('*', '')
            object.Obtain.append(string)
            if '#NO_INFO' in object.Obtain:
                object.Obtain.remove('#NO_INFO')


        if line.startswith('| **Cost'):
            line = line.strip('|')
            left = line.find('|')
            string = line[left + 1:].strip(' ')
            item_cost_string = 'Item is sold by NPC for: ' + string.replace(' <br>', ', ') + '. '
            object.Obtain.append(item_cost_string + location_info_string)
            if '#NO_INFO' in object.Obtain:
                object.Obtain.remove('#NO_INFO')

        if line.startswith('**Coordinates'):
            string = line[line.rfind('*'):].strip(' ')  # получаем координаты в скобках
            string = string[2: len(string)]  # убираем скобки
            object.Coordinates.append(string)
            if '#NO_INFO' in object.Coordinates:
                object.Coordinates.remove('#NO_INFO')

def reimagination2(pre_file, res_file):
    """
    Функция получает 2 файла: файл на чтение и файл на заполнение.
    Работает для документов Books.
    В файле Books важны лишь 3 вида строк:
        1) строка с '# ' - название
        2) строка координат вида | X | Y | Z | (пробелов внутри сколько-то)
        3) текстовая строка - информация о предмете (фактически Obtain)
    """
    object = Item()
    number_of_obj2 = 0  # считаем число объектов + с его помощью не печатаем в начале документа пустой элемент класса

    for initial_line in pre_file:
        line = initial_line.strip('\n').strip(' ')
        line = line.replace(']]', '').replace('[[', '')

        if line.startswith('# '): # одна решётка - название книги
            # если нашли новый предмет, то старый добавляем в файл, сбрасываем object и задаём новые параметры
            obj_string = (object.Name + ';' + object.Tag + ';' + str(object.Coordinates) + ';' + object.Base_Item
                          + ';' + str(object.Attack_Damage) + ';' + str(object.Attack_Speed) + ';'
                          + object.Ability + ';' + str(object.Armor) + ';' + str(object.Armor_Toughness)
                          + ';' + str(object.Enchantments) + ';' + str(object.Bonus_Stats) + ';' + str(object.Obtain))
            if number_of_obj2 > 0:
                res_file.write(obj_string + '\n')
            number_of_obj2 += max(1, len(object.Coordinates))

            object.reset()
            object.Name = line[2:].strip(' ')
            if object.Name == '':
                object.Name = 'NO_INFO'
            object.Tag = 'Book'

        if (line.startswith('| ') and not(line.startswith('| *') or line.startswith('|  *')
                                          or line.startswith('| :'))): # нашли строку координат
            line = line.strip('|').replace(' ', '')
            line = '(' + line.replace('|', ', ') + ')'
            if '#NO_INFO' in object.Coordinates:
                object.Coordinates.append(line)
                object.Coordinates.remove('#NO_INFO')

        if line[:3].isalpha() : # если строк аначинается с текста, то в Obtain
            object.Obtain.append(line)
            if '#NO_INFO' in object.Obtain:
                object.Obtain.remove('#NO_INFO')


def reimagination3(pre_file, res_file):
    """
    Функция получает 2 файла: файл на чтение и файл на заполнение.
    Работает для документов FerverStones, Trinkets.
    В файле Books важны лишь 3 вида строк:
        1) строка с '# ' - класс предмета
        2) строка с '### ' - название
        3) текстовая строка - информация о предмете (фактически Obtain)
    """
    object = Item()
    number_of_obj3 = 0  # считаем число объектов + с его помощью не печатаем в начале документа пустой элемент класса

    for initial_line in pre_file:
        line = initial_line.strip('\n').strip(' ')
        line = line.replace(']]', '').replace('[[', '')
        line = line.strip('|').strip(' ')

        if line.startswith('# '): # в файлах одна решётка означает группу предметов
            tag = line[1:].strip(' ')

        if line.startswith('### '): # одна решётка - название предмета
            # если нашли новый предмет, то старый добавляем в файл, сбрасываем object и задаём новые параметры
            obj_string = (object.Name + ';' + object.Tag + ';' + str(object.Coordinates) + ';' + object.Base_Item
                          + ';' + str(object.Attack_Damage) + ';' + str(object.Attack_Speed) + ';'
                          + object.Ability + ';' + str(object.Armor) + ';' + str(object.Armor_Toughness)
                          + ';' + str(object.Enchantments) + ';' + str(object.Bonus_Stats) + ';' + str(object.Obtain))
            if number_of_obj3 > 0:
                res_file.write(obj_string + '\n')
            number_of_obj3 += max(1, len(object.Coordinates))

            object.reset()
            object.Name = line[4:].strip(' ')
            if object.Name == '':
                object.Name = 'NO_INFO'
            object.Tag = tag

        if line[:2].isalpha(): # ищем строку с информацией для Obtain и Coordinates
            string = line[line.find('|') + 1:].strip(' ').replace('|', '')
            right = string.find('*') + 2 # ищем левую и правую скобки координат
            left = string.rfind('*') - 2
            coord_string = string[right : left + 1]
            string = string.replace('*', '')
            object.Coordinates.append(coord_string)
            object.Obtain.append(string)
            if '#NO_INFO' in object.Coordinates:
                object.Coordinates.remove('#NO_INFO')
            if '#NO_INFO' in object.Obtain:
                object.Obtain.remove('#NO_INFO')


def reimagination4(pre_file, res_file):
    """
    Функция получает 2 файла: файл на чтение и файл на заполнение.
    Работает для документов RunicCatalysts.
    В файле Books важны лишь 2 вида строк:
        1) строка с '# ' - класс предмета (она одна)
        2) текстовая строка - информация о предмете (фактически Obtain и Coordinates)
    """
    object = Item()
    number_of_obj4 = 0  # считаем число объектов + с его помощью не печатаем в начале документа пустой элемент класса

    for initial_line in pre_file:
        line = initial_line.strip('\n').strip(' ')
        line = line.replace(']]', '').replace('[[', '')
        line = line.strip('|')

        if line.startswith('# '): # одна решётка - название предмета
            # если нашли новый предмет, то старый добавляем в файл, сбрасываем object и задаём новые параметры
            obj_string = (object.Name + ';' + object.Tag + ';' + str(object.Coordinates) + ';' + object.Base_Item
                          + ';' + str(object.Attack_Damage) + ';' + str(object.Attack_Speed) + ';'
                          + object.Ability + ';' + str(object.Armor) + ';' + str(object.Armor_Toughness)
                          + ';' + str(object.Enchantments) + ';' + str(object.Bonus_Stats) + ';' + str(object.Obtain))
            if number_of_obj4 > 0:
                res_file.write(obj_string + '\n')
            number_of_obj4 += max(1, len(object.Coordinates))

            object.reset()
            object.Name = line[2:].strip(' ')
            if object.Name == '':
                object.Name = 'NO_INFO'
            object.Tag = 'Runic Catalyst'

        if line[0].isalpha(): # нашли строку с текстом
            index_list = [] # найдём индексы всех '|'
            for i in range(len(line)):
                if line[i] == '|':
                    index_list.append(i)

            object.Obtain.append(line[:index_list[0]].strip(' '))
            coord_string = ('(' + line[index_list[2] + 1:index_list[3]].strip(' ') + ', ' +
                             line[index_list[3] + 1:index_list[4]].strip(' ') + ', ' +
                             line[index_list[4] + 1:].strip(' ') + ')'
                             )
            object.Coordinates.append(coord_string)
            if '#NO_INFO' in object.Coordinates:
                object.Coordinates.remove('#NO_INFO')
            if '#NO_INFO' in object.Obtain:
                object.Obtain.remove('#NO_INFO')




#with open('DrehmalApotheosis_v2.2.1_Dataset.txt', mode='w') as D:
with open('DrehmalApotheosis_v2.2.1_Dataset.csv', mode='w') as D:

    write_title_string(D)

    # читаем первый файл и перезаписываем в итоговый
    A=open('DrehmalApotheosis_v2.2.1_Artifacts.txt')
    reimagination1(A, D)

    # читаем второй файл и перезаписываем в итоговый
    LI = open('DrehmalApotheosis_v2.2.1_LegendaryItems.txt')
    reimagination1(LI, D)

    # ну и так далее
    MW = open('DrehmalApotheosis_v2.2.1_MythicalWeapons.txt')
    reimagination1(MW, D)

    AI = open('DrehmalApotheosis_v2.2.1_ArtisanItems.txt')
    reimagination1(AI, D)

    B = open('DrehmalApotheosis_v2.2.1_Books.txt')
    reimagination2(B, D)

    T = open('DrehmalApotheosis_v2.2.1_Trinkets.txt')
    reimagination3(T, D)

    FS = open('DrehmalApotheosis_v2.2.1_FervorStones.txt')
    reimagination3(FS, D)

    RC = open('DrehmalApotheosis_v2.2.1_RunicCatalysts.txt')
    reimagination4(RC, D)




