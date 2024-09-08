-------- Проект FreshHtmlCobra
CREATED FROM   -- B4MBOLBI  --



    Простая альтернатива фреймворкам основанным на js, node.js и другие
которые предназначены для сборки проекта сайта или приложения основанного на html, css, js

Для работы нужно :
1. Иметь собранный шаблон проекта
Пример как он должен выглядеть:
----------------------------------------------
            папка data
                -файл data.json
                -файл refresh_template.json

            папка finish_file
                - в ней находится финишный файл сборки проекта
            папка layout
                -папка css
                    файлы стилей
                -папка js
                    файлы скриптов
                index.html
            папка templates
                - файлы шаблонов в формате html
----------------------------------------------

!!скрипт проверяет строгое соответствие структуры проекта как указано в примере!!
!!скрип проверяет наличие папок data и layout, и все что там в них находится, согласно примеру!!

--------------------------- ОБЫЯСНЕНИЯ ФАЙЛОВ --------------------------

                    =======data.json======

        В нем у вас хранятся данные которые нужно вставлять в главный файл проект INDEX.HTML
        Пример
            {
                "title": "Myapp",
                "price": 300,
                "name": "Alex"
            }
        Пример как это должно выглядеть в index.html
          <!doctype html>
          <html lang="ru">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport"
               content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>{title}</title> <---------------------dict['Myapp']
            <link rel="stylesheet" href="./css/content.css">
            <link rel="stylesheet" href="./css/main.css">
            <link rel="stylesheet" href="./css/Templates.css">
            </head>
            <body>
                 <div class="content">
                    <div class="info_price">{price}</div><---------------------dict['price']
                </div>
                <div class="user">
                    {name}<---------------------dict['name']
                </div>
           </body>
           </html>
        Таким образом эти данные вставятся при рендере в index.html из data.json

                    =====refresh_template.json=====

        такой же принцип как и у data.json, только этот файл взаимодействует с файлами из папки templates
        пример папки templates
            -circle.html
            -cub.html

        пример файла refresh_templates.json
            {
                "cub" : {"text" :  "Я куб"},
                "circle": {"text": "Я круг"}
            }
        !!!ВАЖНО!!! КЛЮЧИ ДОЛЖНЫ СОВПАДАТЬ С ИМЕНАМИ САМИХ ФАЙЛОВ ИНАЧЕ СКРИПТ НЕ СМОЖЕТ СОРЬЕНТИРОВАТЬСЯ И ВСТАВИТЬ ДАННЫЕ

        пример файла cub.html
           <h2 class="cub">{text}</h2>

        пример файла circle.html
           <h2 class="circle">{text}</h2>

        пример файла index.html до рендеринга
            <!doctype html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport"
                      content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>{title}</title>
                <link rel="stylesheet" href="./css/content.css">
                <link rel="stylesheet" href="./css/main.css">
                <link rel="stylesheet" href="./css/Templates.css">
            </head>
            <body>
                {cub}
                {circle}
            </body>
            </html>

        а это после рендеринга
            <!doctype html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport"
                      content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Myapp</title>
                <link rel="stylesheet" href="./css/content.css">
                <link rel="stylesheet" href="./css/main.css">
                <link rel="stylesheet" href="./css/Templates.css">
            </head>
            <body>
                <h2 class="cub">Я куб</h2>
                <h2 class="circle">Я круг</h2>
            </body>
            </html>

        все спокойно и прекрастно вставляется

                    =====finish_file=====
    финишная папка куда сохранится проект после рендера

                    =====layout=====
    папка css
        в ней храните все стили для темплэйтов и для гланого файла index.html
        при это сколько угодно файлов может быть, главное не забудьте их подключить к index.html)))

    папка js
        аналогично что и с папкой css

    файл index.html
        главный файл для сборки

                    =====templates=====
    тут хранятся все ваши шаблоны в формате html


2. Иметь полный путь к вашему проекту
Пример как дожно быть:
    C:\\Users\\Ваш_пользователь\\Desktop\\includes_html
                                                 ^
                                                 |
                                         (это ваш проект)

Как работать со скриптом:
    Запускаешь файл main.py в консоли, даешь ему путь (который указан во втором пункте выше),
  и если все прошло гладко и без ошибок, ищешь файл new_site.html в папке finish_file

  !!если прошло не все гладко, просто следуйте инструкции, !!!повторяю!!! ВСЕ ДОЛЖНО БЫТЬ В СТРОГОМ СООТВЕТСВИИ С ПРИМЕРОМ
  Удачной работы!!))
