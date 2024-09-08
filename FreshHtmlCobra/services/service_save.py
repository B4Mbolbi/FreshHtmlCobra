
def service_save(path, data):
    with open(path +'\\finish_file\\'+'new_site.html', 'w',encoding='utf-8') as f:
        f.write(data)

    print("\033[32m {}" .format('Проект успешно создан!! \n Помещен в папку finish_file\\new_site.html'))