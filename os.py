import os
import calendar
import datetime
import database
from time import sleep, gmtime

perangkatKeras = database.getPerangkatKeras()
osInfo = database.getOSInfo()
users = database.getUsers()
dir = database.getDirectory()
dir_content = database.get_dir_content()

def kembaliKeParentDir(current_dir, letak_parent):
    splittedString = list(current_dir.split('\\'))
    parent_dir = ''
    current_dir_name = splittedString[len(splittedString)-1]

    if letak_parent == '.':
        parent_dir = current_dir

    if letak_parent == '..':
        splitted_dir = list(current_dir.split(f'\\{current_dir_name}'))
        parent_dir = splitted_dir[0]

    return parent_dir

def mkdir(parent_dir, nama_directory):
    current_GMT = gmtime()
    timestamp = calendar.timegm(current_GMT)
    date_time = datetime.datetime.fromtimestamp(timestamp)

    new_dir = {
        'path': f'{parent_dir}\\{nama_directory}',
        'nama': nama_directory,
        'jenis': '<DIR>',
        'jam_update': date_time.strftime("%I:%M %p"),
        'tgl_update': date_time.strftime("%m/%d/%Y")
    }

    for i in range(len(dir)):
        if dir[i].lower() == parent_dir.lower():
            for content_dict in dir_content[i]:
                if content_dict['nama'].lower() == nama_directory.lower():
                    return print('Folder sudah ada!')
            dir_content[i].append(new_dir)
            dir.append(new_dir['path'])
            dir_content.append([
                {
                    'path': f'{parent_dir}\\.',
                    'nama': '.',
                    'jenis': '<DIR>',
                    'jam_update': date_time.strftime("%I:%M %p"),
                    'tgl_update': date_time.strftime("%m/%d/%Y")
                },
                {
                    'path': f'{parent_dir}\\..',
                    'nama': '..',
                    'jenis': '<DIR>',
                    'jam_update': date_time.strftime("%I:%M %p"),
                    'tgl_update': date_time.strftime("%m/%d/%Y")
                }
            ])
            for content_dict in dir_content[i]:
                if content_dict['path'].lower() == f"{kembaliKeParentDir(parent_dir, '.')}\\.".lower():
                    content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                    content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")

    for i in range(len(dir)):
        if dir[i].lower() == kembaliKeParentDir(parent_dir, '..').lower():
            for content_dict in dir_content[i]:
                if content_dict['path'].lower() == parent_dir.lower():
                    content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                    content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")

                    return print(f'Folder {nama_directory} berhasil dibuat')


def cd(dir_path, current_dir=''):
    if dir_path == '.':
        parent_dir = kembaliKeParentDir(current_dir, '.')
        for i in range(len(dir)):
            if dir[i].lower() == parent_dir.lower():
                return dir[i]
        return current_dir
    elif dir_path == '..':
        parent_dir = kembaliKeParentDir(current_dir, '..')
        for i in range(len(dir)):
            if dir[i].lower() == parent_dir.lower():
                return dir[i]
        return current_dir
    else:
        for i in range(len(dir)):
            if dir[i].lower() == dir_path.lower():
                return dir_path
            if dir[i].lower() == f'{current_dir}\\{dir_path}'.lower():
                return f'{current_dir}\\{dir_path}'
            if dir[i].lower() != f'{current_dir}\\{dir_path}'.lower() and i == len(dir)-1:
                print(f'Folder {dir_path} tidak ada!')
                return current_dir
        
def show_all(current_dir):
    for i in range(len(dir)):
        if dir[i].lower() == current_dir.lower():
            for content_dict in dir_content[i]:
                print(f"{content_dict['tgl_update']}  {content_dict['jam_update']}  {content_dict['jenis']}  {content_dict['nama']}")
    
    print()

def showOSInfo(dict):
    print(f"{dict['name']} v{dict['version']}")
    print(f"(c) {dict['company']}. All rights reserved.")

def samakanPanjangString(string_awal, stringPatokan):
    string_baru = string_awal
    while len(string_baru) < len(stringPatokan):
        string_baru = string_baru + ' '
    return string_baru

def dapatkanStringTerpanjang(list):
    terpanjang = len(list[0])
    string = list[0]
    for i in range(len(list)):
        if len(list[i]) > terpanjang:
            terpanjang = len(list[i])
            string = list[i]
    
    return string

def prosesPOST():
    namaTerpanjang = dapatkanStringTerpanjang(perangkatKeras)

    os.system('cls')
    for i in range(len(perangkatKeras)):
        stringProses = f'{perangkatKeras[i]}     '
        stringTerpanjang = f'{namaTerpanjang}     '
        spasi = samakanPanjangString(stringProses, stringTerpanjang)

        for j in range(10,101,20):
            print(f'{spasi}{j}%', end='\r')
            sleep(0.5)
        print(f'{spasi}    ', end='')
        print('OK')
    sleep(2)
    os.system('cls')

def startingOS():
    for i in range(4):
        stringTampil = 'Starting OS'
        print(f'{stringTampil}   ', end='\r')
        for j in range(4):
            print(stringTampil, end='\r')
            stringTampil = stringTampil + '.'
            sleep(0.5)
    os.system('cls')

def standByCMD():
    current_dir = dir[0]
    parsedInput = []

    os.system('cls')
    showOSInfo(osInfo)
    print()

    perintah = ''
    while True:
        print(f'{current_dir}>', end='')
        perintah = input()

        parsedInput = list(perintah.split(' '))

        if parsedInput[0].lower() == 'cd':
            current_dir = cd(parsedInput[1], current_dir)
        elif parsedInput[0].lower() == 'dir':
            show_all(current_dir)
        elif parsedInput[0].lower() == 'mkdir':
            mkdir(current_dir, parsedInput[1])

commands = [
    {
        'name': 'mkdir',
        'function': mkdir
    }
]

def main():
    # prosesPOST()
    # startingOS()
    standByCMD()

main()
