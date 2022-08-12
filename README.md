# itstep-homeworks2-task1a
itstep-homeworks2-task1a

Задание:

Создать функцию которая принимает число и начинает обратный отсчет с интервалом в 1 секунду. Запустить 5 таких функции паралельно. Сделать 2 варианта через threading, и через asyncio.
По наблюдениям описать что работает лучше и почему(не обязательно)
Запушить в гит, скинуть ссылку

Выводы:

1. Вывод в asyncio получается лучше, в связи с тем что переключения происходят в моменты вызова await, а не случайно перемешиваются, как в treading.

asyncio:

Function N 2 lifetime left 14

Function N 4 lifetime left 2

Function N 1 lifetime left 3

{1: 3, 2: 14, 3: 1, 4: 2, 5: 10}

Function N 4 lifetime left 1

Function N 2 lifetime left 13

Function N 3 game over



threading: 

{2: 3, 3: 8, 4: 5, 5: 2}

Function N 3 lifetime left 7Function N 4 lifetime left 4

Function N 2 lifetime left 2

Function N 5 lifetime left 1

{2: 2, 3: 7, 4: 4, 5: 1}

Function N 5 game overFunction N 3 lifetime left 6Function N 2 lifetime left 1



2. Пока не разобрался как в threading запускать процесс так чтобы он работал в backghround и не мешал закрытию программы. Если у меня оставалась фунция отображения состояния в режиме while true, то программа зависала, даже если я не писал t99.join(). Возможно не знаю функцию такого запуска процесса. 
В asycnio все просто, когда таска создается она сразу создается, и работает независимо, главаня программа тоже работает независимо и заканичается, если нам нужно ждать таску мы используем await.
