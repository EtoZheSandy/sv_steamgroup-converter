# Steam Group ID Converter

Это небольшой скрипт для конвертации Steam Group ID (таких как) **6035128** 
В более простой и понятный вид что для получение информации о группе:
ID: $GroupId8, Группа: $name, Участников $amount, Ссылка: $Url

Так ID группы **6035128** станет:
ID: 964095, Группа: Left 4 Dead 2, Участников: 993,688, Ссылка: https://steamcommunity.com/groups/L4D2


# Как с этим работать?
В скрипте есть 3 переменные которые можно менять по вашем усмотрению.
- **amountMember** = 500
	> Определяет минимальное количество участников группы Steam, если их будет меньше **500** (стандартно), то группа вам не покажется в итоговом выводе.
- **SteamGroupIDList** = "964095,554109,883,3703047,554111,2574770"
	> В эту переменную необходимо вписать ваш список GroupID который хотите проверить и получить информацию о интересующих ID
- **MySteamGroupIDList** = "964095,554109"
	> В нее вы можете вписать список групп из своего **server.cfg** для сравнение их с **SteamGroupIDList**  на дубли и вычеркивание таковых из итогового списка.

## Хорошо а если мне не нужно сравнивать с моим списком?

Достаточно будет закомментировать данную переменную, поставив знак # перед ней.

`#MySteamGroupIDList = "964095,554109"`


## А какая версия Python для запуска?

Я проверял и разрабатывал на 3.11, касательно того будет ли он работать на более ранних или поздних версиях, я не смогу подсказать.

## Скрипт преобразовал неправильный URL для группы!
Официальные страницы игр могут не корректно конвертировать в URL группы так-как не являются по своей сути группой. Но работать такой id будет. 
Для получения правильной ссылке заменить ID на "некоректный" https://steamcommunity.com/gid/ВАШ_ID
