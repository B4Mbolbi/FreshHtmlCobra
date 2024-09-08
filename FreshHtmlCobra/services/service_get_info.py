import json

def _get_info_refresh(path):
    path = path + '\\data\\refresh_template.json'
    with open(path, 'r',encoding='utf-8') as f:
        data = json.load(f)
    return data

def get_template_file(path):
    arr_refresh = []
    tmplates = path + '\\templates'
    for key,value in _get_info_refresh(path).items():
        with open(tmplates + '\\' + key + '.html', 'r',encoding='utf-8') as f:
            data = f.read()
        arr_refresh.append(data.format(**_get_info_refresh(path)[key]))
    return dict(zip(list(_get_info_refresh(path).keys()), arr_refresh))

def get_info_idex_file(path):
    index = path + '\\layout\\index.html'
    data = path + '\\data\\data.json'
    with open(data, 'r',encoding='utf-8') as f:
        data = json.load(f)
    index_file = ''
    with open(index, 'rb') as f:
        for line in f:
            index_file += line.decode('utf8')
    if len(data) == 0:
        index_file.format(**get_template_file(path))
    else:
        all_data =  data |get_template_file(path)
        index_file = index_file.format(**all_data)
    return index_file

