import requests
import xmltodict as xmltodict

AllID = [] # Переменная для парсинга через Steam
ResultID = []  # Переменная для сохранение пропарсенных групп

#### Тут ты можешь вписать свои знаничения в 3 переменные ниже
#Лимит участников группы для отображение в результате
amountMember = 500
# Список Steam ID Group, это лишь пример ID, сюда ты можешь вписать свои по примеру
SteamGroupIDList = "6035128,964095,554109,883,3703047,554111,2574770,1998399,4190169,3380750,10324870,4617636,3651243,1698036,3501808,6180012,24925891,3945817,25038663,938619,2194475"
#Список ваших ID Group из server.cfg, если не будете сравнивать - достаточно закоментировать поставив знак # перед переменной
MySteamGroupIDList = "6035128,964095,554109,883,3703047,554111"



def checkDoubleID(SteamIDList): #Проверка на дубли между SteamGroupIDList и MySteamGroupIDList
    for groupID in SteamIDList.replace(' ', '').split(','):  # проходимся по каждому ID
        if groupID not in AllID:  # проверяем повторяется ли он
            AllID.append(groupID)  # если уникален - добавляем
        else:
            pass  # Если повторяется - пропускаем

#проверка на дубли через функцию checkDoubleID
try: #на случай если закоментируют MySteamGroupIDList
    checkDoubleID(SteamGroupIDList)
    checkDoubleID(MySteamGroupIDList)
except:
    pass


print(f'Количество групп без дублей: {len(AllID)}\n')
for groupID in AllID:  # основной цикл для проверки ID групп и получения по ним информации
    try:
        url = f'https://steamcommunity.com/gid/{groupID}/memberslistxml/?xml=1'
        groupuUrl = 'https://steamcommunity.com/groups/'
        getUrl = requests.get(url)
        getUrl = xmltodict.parse(getUrl.content)

        # проверка на участников, их должно быть более 500, иначе зачем нам пустая группа в подписках, верно?
        if int(getUrl['memberList']['groupDetails']['memberCount']) > amountMember:
            ResultID.append(groupID)
            print(f"ID: {groupID}, Группа: {getUrl['memberList']['groupDetails']['groupName']}, "
                  f"Участников: {'{0:,}'.format(int((getUrl['memberList']['groupDetails']['memberCount'])))}, Ссылка: {groupuUrl + getUrl['memberList']['groupDetails']['groupURL']}")
        else:
            pass
    except:  # если не удалось получить группу - пропускаем
        pass

print(f'\nВсего групп с {amountMember}+ участников: {len(ResultID)}')

sv_steamgroup = 'sv_steamgroup "'
for groupID in ResultID:
    sv_steamgroup = sv_steamgroup + groupID + ','

print(f'\nВот список групп сразу в переменной для server.cfg\n')
print(sv_steamgroup[:-1] + '"')  # для красивого вывода строки, которую можно сразу вставить в server.cfg