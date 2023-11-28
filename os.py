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
    parent_dir_name = splittedString[len(splittedString)-2]

    if letak_parent == '.':
        splitted_dir = list(current_dir.split(f'\\{current_dir_name}'))
        parent_dir = splitted_dir[0]

    if letak_parent == '..':
        splitted_dir = list(current_dir.split(f'\\{parent_dir_name}\\{current_dir_name}'))
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
        'jam_update': date_time.strftime("%m/%d/%Y"),
        'tgl_update': date_time.strftime("%m/%d/%Y")
    }

    for i in range(len(dir)):
        if dir[i] == parent_dir:
            dir_content[i].append(new_dir)
            for content_dict in dir_content[i]:
                if content_dict['path'] == f"{kembaliKeParentDir(parent_dir, '.')}\\.":
                    content_dict['jam_update'] = date_time.strftime("%m/%d/%Y")
                    content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")

        if dir[i] == kembaliKeParentDir(new_dir['path'], '..'):
            for content_dict in dir_content[i]:
                if content_dict['path'] == parent_dir:
                    content_dict['jam_update'] = date_time.strftime("%m/%d/%Y")
                    content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")

    dir.append(new_dir['path'])
    dir_content.append([
        {
            'path': f'{parent_dir}\\.',
            'nama': '.',
            'jenis': '<DIR>',
            'jam_update': date_time.strftime("%m/%d/%Y"),
            'tgl_update': date_time.strftime("%m/%d/%Y")
        },
        {
            'path': f'{parent_dir}\\..',
            'nama': '..',
            'jenis': '<DIR>',
            'jam_update': date_time.strftime("%m/%d/%Y"),
            'tgl_update': date_time.strftime("%m/%d/%Y")
        }
    ])

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
    while perintah == '':
        print(f'{current_dir}>', end='')
        perintah = input()

        parsedInput = list(perintah.split(' '))

def main():
    prosesPOST()
    startingOS()
    standByCMD()

main()
