# obmc_test_locust
Разработка сценария нагрузочного тестирования с использованием Locust

## Перечисление автотестов
В набор входят следующие классы нагрузки:
1) Тестирование OpenBMC API:
    - Получение информации о системе (/redfish/v1/Systems/system).
    - Запрос состояния питания.
2) Тестирование публичного API:
    - Запрос списка постов на JSONPlaceholder (/posts).
    - Запрос погоды на wttr.in (https://wttr.in/Novosibirsk?format=j1).

## Результат тестирования

### Запуск нагрузочного тестирования
1. Для запуска locust с включением в набор задач определенных тестов можно воспользоваться следующей командой:
   ```
   locust -f <filename>
   ```

2. Затем необходимо перейти в веб-интерфейс по адресу: http://localhost:8089, указать количество пользователей и скорость их запуска.

### Тестирование OpenBMC API
1. Запуск нескольких тестовых итераций, чтобы определить нагрузку, при которой начинают появляться ошибки.
   
   ![obmc_100_50_saturation](https://github.com/Doom-ux/obmc_test_locust/blob/media/openBmc_60_30_80_40_80_60_100_50.png)

   Описание паратеров итераций:
    - Run #1: количество пользователей равно 60, скорость их запуска 30 пользователей/сек.
    - Run #2: количество пользователей равно 80, скорость их запуска 40 пользователей/сек.
    - Run #3: количество пользователей равно 80, скорость их запуска 60 пользователей/сек.
    - Run #4: количество пользователей равно 100, скорость их запуска 50 пользователей/сек.

3. Статистическая таблица последней тестовой итерации с количеством пользователей равным 100.

   ![obmc_100_50_saturation](https://github.com/Doom-ux/obmc_test_locust/blob/media/openBmc_60_30_80_40_80_60_100_50_statistics.png)

   <p>По соотношению значения ошибочных запросов с общим количеством запросов <b>процент ошибок</b> состовляет: 97%.</p>
   <p>Среднее время отклика API по таблице равано: 6.67 сек.</p>

## Структура каталогов

```
obmc_test_locust/
    tests/
        locustfile.py
        locustfile2.py
    README.md
```
