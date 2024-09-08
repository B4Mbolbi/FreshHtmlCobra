from services.service_checked_directory import *
from services.service_get_info import *
from services.service_save import *


pathHTmlDirectory = input("\033[32m {}" .format('Введите путь к папке с шаблонами проекта - '))

struct_cild =chec_structure(pathHTmlDirectory)
struct = check_structure_shild(pathHTmlDirectory)

if struct and struct_cild:
    get_info_idex_file(pathHTmlDirectory)
    service_save(pathHTmlDirectory, get_info_idex_file(pathHTmlDirectory))
