import os
import calendar
import datetime
from time import sleep, gmtime

perangkatKeras = ['RAM', 'Harddisk Drive', 'CD ROM Drive', 'USB Port']

osInfo = {
    'name': 'BGS OS',
    'version': 1.0,
    'company': 'BGS Corporation'
}

users = ['Anugrah']

dir = [
    f'C:\\Users\\{users[0]}',
    f'C:\\Users\\{users[0]}\\Desktop',
    f'C:\\Users\\{users[0]}\\Documents',
    f'C:\\Users\\{users[0]}\\Downloads',
    f'C:\\Users\\{users[0]}\\Music',
    f'C:\\Users\\{users[0]}\\Pictures',
    f'C:\\Users\\{users[0]}\\Videos'
]

dir_content = [
    [
        {
            'path': f'C:\\Users\\{users[0]}\\Desktop',
            'nama': 'Desktop',
            'jenis': '<DIR>',
            'jam_update': '07:28 PM',
            'tgl_update': '11/04/2023'
        },
        {
            'path': f'C:\\Users\\{users[0]}\\Documents',
            'nama': 'Documents',
            'jenis': '<DIR>',
            'jam_update': '11:35 AM',
            'tgl_update': '11/21/2023'
        },
        {
            'path': f'C:\\Users\\{users[0]}\\Downloads',
            'nama': 'Downloads',
            'jenis': '<DIR>',
            'jam_update': '05:12 AM',
            'tgl_update': '11/27/2023'
        },
        {
            'path': f'C:\\Users\\{users[0]}\\Music',
            'nama': 'Music',
            'jenis': '<DIR>',
            'jam_update': ' 09:21 AM',
            'tgl_update': '11/08/2023'
        },
        {
            'path': f'C:\\Users\\{users[0]}\\Pictures',
            'nama': 'Pictures',
            'jenis': '<DIR>',
            'jam_update': '10:15 AM',
            'tgl_update': '11/24/2023'
        },
        {
            'path': f'C:\\Users\\{users[0]}\\Videos',
            'nama': 'Videos',
            'jenis': '<DIR>',
            'jam_update': '10:13 AM',
            'tgl_update': '11/26/2023'
        }
    ],
    [],
    [],
    [],
    [],
    [],
    []
]

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

    dir.append(new_dir['path'])
    dir_content.append([])




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
        print('OK', end='')
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
    while perintah != '':
        print(f'{current_dir}>', end='')
        perintah = input()

        parsedInput = list(perintah.split(' '))

def main():
    prosesPOST()
    startingOS()
    standByCMD()

main()
