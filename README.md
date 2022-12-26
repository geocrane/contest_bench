### Верстак-Контест - v.0.1
**Локальное тестирование задач Контеста в Яндекс Практикуме.**

Цель программы предоставить простой и удобный инструмент для тестирования текущего решения, не прибегая к использованию штатной формы Яндекс Контеста. Позволяет сразу использовать данные из примеров к задаче, а при отладке отдельные и более сложные тесты Контеста. Удобен тем, что входные данные и ответы заносятся в единый файл, без необходимости разносить их вручную или создавать множество тестовых файлов._

_Работа программы протестирована на финальных заданиях для спринтов ЯндексПрактикума и на случайной выборке задач из ЯндексКонтеста. Тем не менее, так как логика построена на основе моих решений задач и требованиях моего ревьювера, возможны сюрпризы и ошибки у других студентов. Если кто-то столкнется с неправильной работой тестов, буду благодарен за подробности.

**Основные файлы программы:**
```
bench.py - файл для кода с решением
test.py - файл для запуска тестов
data.txt - входные данные и ответы
settings.py - служебные настройки
```
**Описание работы:**
>**bench.pу:**
Основной рабочий верстак. Здесь нужно писать код решения задачи в том виде, в котором он будет отправляться на ревью, или копироваться в Контест для окончательного результата. По умолчанию программа исходит из условия, что исполняемые функции должны быть спрятаны в блок if _ _name_ _ == "_ _main_ _".

--

>**test.pу:**
Файл с единственной функцией для запуска тестов. Вынесен отдельно для избежания случайных правок в основном теле программы.

--

>**data.txt:**
Файл с данными. Важно правильно настроить **data.txt** перед началом работы. Входные данные должны идти на следующей строке после ключевого маркера **"in"**, ожидаемый ответ после маркера **"out"**. Ответ должен идти после входных данных. Допускается вставка данных сразу для множества тестов, но порядок "входные_данные -> ответ" должен соблюдаться. Пустые строки разрешены.

**Пример заполнения data.txt (задача "Калькулятор"):**
```
in
2 1 + 3 *

out
9

in
7 2 + 4 * 2 +
out
38
```
**Пример заполнения data.txt (задача "Дек"):**
```
in

4
4
push_front 861
push_front -819
pop_back
pop_back


out
861
-819
```
--
>**settings.pу:**
В настройках предусмотрена замена ключевых маркеров "in" и "out" в случае, если данные сочетания используются в задаче как часть входных данных или ожилаемый ответ. Можно указать иные удобные маркеры в settings.pу и использовать их в data.txt соответсвтенно.

>Аналогично, в процессе работы программа использует набор символов **"&&&"** как маркер для разбивки общего списка входных данных на отдельные тесты. Маловероятно, что такое сочетание совпадет с данными задачи, но при совпадении маркер может быть изменен на другой.

> Вывод результата тестирования может осуществляться в полном или сокращенном виде. Настройка  производится изменением значения ASSERTIONS_SHORT_FORMAT на False или True.

Пример успешного результата тестов:
```
TEST 1: ОК!
TEST 2: ОК!
TEST 3: ОК!
```

Пример сжатого результата тестов с ошибками:
```
ТЕСТ 1: ОШИБКА! Получены строки: ['2'] // Правильно: ['3']
ТЕСТ 2: ОШИБКА! Получены строки: ['1'] // Правильно: ['2']
ТЕСТ 3: ОШИБКА! Получены строки: ['0'] // Правильно: ['1']
```

Пример полного результата тестов:
```
ТЕСТ 1: ОШИБКА!
Входные данные:
([{}])

Вывод программы:
False

Правильный ответ:
True
--------------------
ТЕСТ 2: ОК!
```

##### Желательные доработки:
- Добавить автоматическое заполнение данных в data.txt
- Добавить возможность запуска не только из раздела "if name =="
- Проставить кодировку при открытии файлов
- Избавиться от "костылей"-маркеров типа "&&&"

---
###### Технология: Python 3.8.10
###### Разработчик: [Сергей Журавлев](https://github.com/geocrane)
