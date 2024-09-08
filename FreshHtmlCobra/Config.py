ABSOLUTE_DIRECT = ['data', 'finish_file', 'layout', 'templates']

CHILD_DIRECT ={
    "data":['data.json','refresh_template.json'],
    "layout":['css','js','index.html']
}
temp_data = '''\n
папка data
    -файл  data.json
    -файл refresh_template.json
'''
temp_layout = '''\n
папка layout
    -папка css 
        файлы стилей
    -папка js
        файлы скриптов
    index.html
'''

temp_proect = '''
--------------------
папка data
    -файл  data.json
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
'''

