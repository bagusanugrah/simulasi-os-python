import os
import calendar
import datetime
import pytz
import database
from time import sleep, gmtime

help = database.getHelp()
zonawaktu = database.getTimezone()
spesifikasi = database.getSpesifikasi()
perangkatKeras = database.getPerangkatKeras()
osInfo = database.getOSInfo()
users = database.getUsers()
dir = database.getDirectory()
dir_content = database.get_dir_content()

zona = 'default'

def time(timestamp=''):
    global zona
    if zona == 'default':
        return datetime.datetime.fromtimestamp(timestamp)
    else:
        return datetime.datetime.now(pytz.timezone(zona))

def showtime():
    current_GMT = gmtime()
    timestamp = calendar.timegm(current_GMT)
    date_time = time(timestamp)
    timenow = date_time.strftime("%I:%M %p")
    datenow = date_time.strftime("%m/%d/%Y")

    print(f'{datenow}   {timenow}')

def change_timezone():
    global zona

    for i in range(len(zonawaktu)):
        print(f'{i+1}. {zonawaktu[i]}')
    
    inputan_zona = input('Masukkan zona waktu [1-27]: ')

    print()
    for i in range(len(zonawaktu)):
        if inputan_zona == str(i):
            zona = zonawaktu[i]
            return print('Zona waktu berhasil diganti')
    
    print(f'Inputan salah! {inputan_zona} bukan angka dari list zona waktu!')

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
    date_time = time(timestamp)

    new_dir = {
        'path': f'{parent_dir}\\{nama_directory}',
        'nama': nama_directory,
        'jenis': '<DIR>',
        'ukuran': 0,
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
                    'ukuran': 0,
                    'jam_update': date_time.strftime("%I:%M %p"),
                    'tgl_update': date_time.strftime("%m/%d/%Y")
                },
                {
                    'path': f'{parent_dir}\\..',
                    'nama': '..',
                    'jenis': '<DIR>',
                    'ukuran': 0,
                    'jam_update': date_time.strftime("%I:%M %p"),
                    'tgl_update': date_time.strftime("%m/%d/%Y")
                }
            ])
            for content_dict in dir_content[i]:
                if content_dict['path'].lower() == f"{kembaliKeParentDir(parent_dir, '.')}\\.".lower():
                    current_GMT = gmtime()
                    timestamp = calendar.timegm(current_GMT)
                    date_time = time(timestamp)
                    content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                    content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")

    for i in range(len(dir)):
        if dir[i].lower() == kembaliKeParentDir(parent_dir, '..').lower():
            for content_dict in dir_content[i]:
                if content_dict['path'].lower() == parent_dir.lower():
                    current_GMT = gmtime()
                    timestamp = calendar.timegm(current_GMT)
                    date_time = time(timestamp)
                    content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                    content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")

                    return print(f'Folder {nama_directory} berhasil dibuat')

def rename(target_rename, nama_baru, current_dir=''):
    global dir
    global dir_content
    for i in range(len(dir)):
        if dir[i].lower() == target_rename.lower():
            for i in range(len(dir)):
                if dir[i].lower() == target_rename.lower():
                    dir[i] = f'{current_dir}\\{nama_baru}'
                    for content_dict in dir_content[i]:
                        if content_dict['path'].lower() == f'{target_rename}\\.'.lower():
                            content_dict['path'] = f'{current_dir}\\{nama_baru}\\.'
                        if content_dict['path'].lower() == f'{target_rename}\\..'.lower():
                            content_dict['path'] = f'{current_dir}\\{nama_baru}\\..'
            for i in range(len(dir)):
                if dir[i].lower() == kembaliKeParentDir(target_rename, '..').lower():
                    for content_dict in dir_content[i]:
                        if content_dict['path'].lower() == f'{target_rename}'.lower():
                            current_GMT = gmtime()
                            timestamp = calendar.timegm(current_GMT)
                            date_time = time(timestamp)
                            content_dict['path'] = f'{current_dir}\\{nama_baru}'
                            content_dict['nama'] = nama_baru
                            content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                            content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")
                    for content_dict in dir_content[i]:
                        if content_dict['path'].lower() == f'{dir[i]}\\.'.lower():
                            content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                            content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")
                            dir_ada = False
                            for i in range(len(dir)):
                                if dir[i].lower() == kembaliKeParentDir(current_dir, '..').lower():
                                    dir_ada = True
                            if not dir_ada:
                                return print('Rename file/folder berhasil')
            for i in range(len(dir)):
                if dir[i].lower() == kembaliKeParentDir(current_dir, '..').lower():
                    for content_dict in dir_content[i]:
                        if content_dict['path'].lower() == current_dir.lower():
                            current_GMT = gmtime()
                            timestamp = calendar.timegm(current_GMT)
                            date_time = time(timestamp)
                            content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                            content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")
                            return print('Rename file/folder berhasil')
        if dir[i].lower() == f'{current_dir}\\{target_rename}'.lower():
            for i in range(len(dir)):
                if dir[i].lower() == f'{current_dir}\\{target_rename}'.lower():
                    dir[i] = f'{current_dir}\\{nama_baru}'
                    for content_dict in dir_content[i]:
                        if content_dict['path'].lower() == f'{current_dir}\\{target_rename}\\.'.lower():
                            content_dict['path'] = f'{current_dir}\\{nama_baru}\\.'
                        if content_dict['path'].lower() == f'{current_dir}\\{target_rename}\\..'.lower():
                            content_dict['path'] = f'{current_dir}\\{nama_baru}\\..'
            for i in range(len(dir)):
                if dir[i].lower() == kembaliKeParentDir(f'{current_dir}\\{target_rename}', '..').lower():
                    for content_dict in dir_content[i]:
                        if content_dict['path'].lower() == f'{current_dir}\\{target_rename}'.lower():
                            current_GMT = gmtime()
                            timestamp = calendar.timegm(current_GMT)
                            date_time = time(timestamp)
                            content_dict['path'] = f'{current_dir}\\{nama_baru}'
                            content_dict['nama'] = nama_baru
                            content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                            content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")
                    for content_dict in dir_content[i]:
                        if content_dict['path'].lower() == f'{dir[i]}\\.'.lower():
                            current_GMT = gmtime()
                            timestamp = calendar.timegm(current_GMT)
                            date_time = time(timestamp)
                            content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                            content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")
                            dir_ada = False
                            for i in range(len(dir)):
                                if dir[i].lower() == kembaliKeParentDir(current_dir, '..').lower():
                                    dir_ada = True
                            if not dir_ada:
                                return print('Rename file/folder berhasil')
            for i in range(len(dir)):
                if dir[i].lower() == kembaliKeParentDir(current_dir, '..').lower():
                    for content_dict in dir_content[i]:
                        if content_dict['path'].lower() == current_dir.lower():
                            current_GMT = gmtime()
                            timestamp = calendar.timegm(current_GMT)
                            date_time = time(timestamp)
                            content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                            content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")
                            return print('Rename file/folder berhasil')
        if dir[i].lower() != f'{current_dir}\\{target_rename}'.lower() and i == len(dir)-1:
            print(f'Folder {target_rename} tidak ada!')
            return current_dir

def delete(target_hapus, current_dir=''):
    dir_baru = []
    dir_content_baru = []
    global dir
    global dir_content
    for i in range(len(dir)):
        if dir[i].lower() == target_hapus.lower():
            for i in range(len(dir)):
                if dir[i].lower() != target_hapus.lower():
                    dir_baru.append(dir[i])
            for i in range(len(dir)):
                content = []
                for content_dict in dir_content[i]:
                    if content_dict['path'].lower() != target_hapus.lower():
                        content.append(content_dict)
                dir_content_baru.append(content)
            for i in range(len(dir_baru)):
                if dir_baru[i].lower() == kembaliKeParentDir(target_hapus, '..').lower():
                    for content_dict in dir_content_baru[i]:
                        if content_dict['path'].lower() == f'{dir_baru[i]}\\.'.lower():
                            current_GMT = gmtime()
                            timestamp = calendar.timegm(current_GMT)
                            date_time = time(timestamp)
                            content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                            content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")
                            dir_ada = False
                            for i in range(len(dir_baru)):
                                if dir_baru[i].lower() == kembaliKeParentDir(current_dir, '..').lower():
                                    dir_ada = True
                            if not dir_ada:
                                dir = dir_baru
                                dir_content = dir_content_baru
                                return print('Hapus file/folder berhasil')
            for i in range(len(dir_baru)):
                if dir_baru[i].lower() == kembaliKeParentDir(current_dir, '..').lower():
                    for content_dict in dir_content_baru[i]:
                        if content_dict['path'].lower() == current_dir.lower():
                            current_GMT = gmtime()
                            timestamp = calendar.timegm(current_GMT)
                            date_time = time(timestamp)
                            content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                            content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")
                            dir = dir_baru
                            dir_content = dir_content_baru
                            return print('Hapus file/folder berhasil')
        if dir[i].lower() == f'{current_dir}\\{target_hapus}'.lower():
            for i in range(len(dir)):
                if dir[i].lower() != f'{current_dir}\\{target_hapus}'.lower():
                    dir_baru.append(dir[i])
            for i in range(len(dir)):
                content = []
                for content_dict in dir_content[i]:
                    if content_dict['path'].lower() != f'{current_dir}\\{target_hapus}'.lower():
                        content.append(content_dict)
                dir_content_baru.append(content)
            for i in range(len(dir_baru)):
                if dir_baru[i].lower() == kembaliKeParentDir(f'{current_dir}\\{target_hapus}', '..').lower():
                    for content_dict in dir_content_baru[i]:
                        if content_dict['path'].lower() == f'{dir_baru[i]}\\.'.lower():
                            current_GMT = gmtime()
                            timestamp = calendar.timegm(current_GMT)
                            date_time = time(timestamp)
                            content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                            content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")
                            dir_ada = False
                            for i in range(len(dir_baru)):
                                if dir_baru[i].lower() == kembaliKeParentDir(current_dir, '..').lower():
                                    dir_ada = True
                            if not dir_ada:
                                dir = dir_baru
                                dir_content = dir_content_baru
                                return print('Hapus file/folder berhasil')
            for i in range(len(dir_baru)):
                if dir_baru[i].lower() == kembaliKeParentDir(current_dir, '..').lower():
                    for content_dict in dir_content_baru[i]:
                        if content_dict['path'].lower() == current_dir.lower():
                            current_GMT = gmtime()
                            timestamp = calendar.timegm(current_GMT)
                            date_time = time(timestamp)
                            content_dict['jam_update'] = date_time.strftime("%I:%M %p")
                            content_dict['tgl_update'] = date_time.strftime("%m/%d/%Y")
                            dir = dir_baru
                            dir_content = dir_content_baru
                            return print('Hapus file/folder berhasil')
        if dir[i].lower() != f'{current_dir}\\{target_hapus}'.lower() and i == len(dir)-1:
            print(f'Folder {target_hapus} tidak ada!')
            return current_dir

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
    list_sementara = []
    jumlah_file = 0
    total_ukuran = 0
    stringProses = ''

    for i in range(len(dir)):
        if dir[i].lower() == current_dir.lower():
            for content_dict in dir_content[i]:
                if content_dict['jenis'] == '     ':
                    jumlah_file = jumlah_file + 1
                
                total_ukuran = total_ukuran + content_dict['ukuran']
                list_sementara.append(f"{content_dict['tgl_update']}  {content_dict['jam_update']}  {content_dict['jenis']}  {content_dict['ukuran']}")

    stringTerpanjang = dapatkanStringTerpanjang(list_sementara)

    for i in range(len(dir)):
        if dir[i].lower() == current_dir.lower():
            for content_dict in dir_content[i]:
                if content_dict['ukuran'] == 0:
                    stringProses = f"{content_dict['tgl_update']}  {content_dict['jam_update']}  {content_dict['jenis']}   "
                else:
                    stringProses = f"{content_dict['tgl_update']}  {content_dict['jam_update']}  {content_dict['jenis']}  {content_dict['ukuran']}"
                dataTampil = samakanPanjangString(stringProses, stringTerpanjang)
                print(f"{dataTampil}  {content_dict['nama']}")
    
    print(f'{jumlah_file} File(s)      {total_ukuran} Bytes')
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

def showSpec():
    hardware_names = list(spesifikasi.keys())
    namaTerpanjang = dapatkanStringTerpanjang(hardware_names)

    stringProses = f'{namaTerpanjang}   '

    for key in spesifikasi:
        hardware_name = samakanPanjangString(key, stringProses)
        print(f'{hardware_name}:  {spesifikasi[key]}')
    print()

def showCommands():
    command_names = list(help.keys())
    namaTerpanjang = dapatkanStringTerpanjang(command_names)

    stringProses = f'{namaTerpanjang}   '

    for key in help:
        command_name = samakanPanjangString(key, stringProses)
        print(f'{command_name}   {help[key]}')
    print()
    print('Keterangan: Tanda kutip pada contoh hanya sebagai penjelas saja, inputkan perintah tanpa tanda kutip.')
    print()

def stringParser(inputan_string):
    list_awal = list(inputan_string.split(' '))
    list_baru = []

    for i in range(len(list_awal)):
        if list_awal[i] != ' ':
            list_baru.append(list_awal[i])
    
    return list_baru

def startingOS():
    for i in range(4):
        stringTampil = 'Starting OS'
        print(f'{stringTampil}   ', end='\r')
        for j in range(4):
            print(stringTampil, end='\r')
            stringTampil = stringTampil + '.'
            sleep(0.5)
    os.system('cls')

def shutdown():
    os.system('cls')
    for i in range(4):
        stringTampil = 'Shutting down the system'
        print(f'{stringTampil}   ', end='\r')
        for j in range(4):
            print(stringTampil, end='\r')
            stringTampil = stringTampil + '.'
            sleep(0.5)
    return False

def standByCMD():
    current_dir = dir[0]
    parsedInput = []

    os.system('cls')
    showOSInfo(osInfo)
    print()

    sistem_nyala = True
    while sistem_nyala:
        print(f'{current_dir}>', end='')
        perintah = input()

        parsedInput = stringParser(perintah)

        if parsedInput[0].lower() == 'cd':
            if len(parsedInput) < 2:
                print('Berikan argumen pada perintah! Contoh: cd Videos')
            elif len(parsedInput) > 2:
                print('Kelebihan argumen! Perintah hanya membutuhkan satu argumen!')
            else:
                current_dir = cd(parsedInput[1], current_dir)
        elif parsedInput[0].lower() == 'dir':
            if len(parsedInput) > 1:
                print(f'Perintah {parsedInput[0]} tidak membutuhkan argumen sama sekali!')
            else:
                show_all(current_dir)
        elif parsedInput[0].lower() == 'mkdir':
            if len(parsedInput) < 2:
                print('Berikan argumen pada perintah! Contoh: mkdir Projects')
            elif len(parsedInput) > 2:
                print('Kelebihan argumen! Perintah hanya membutuhkan satu argumen!')
            else:
                mkdir(current_dir, parsedInput[1])
        elif parsedInput[0].lower() == 'rename':
            if len(parsedInput) < 3:
                print('Berikan dua argumen pada perintah! Contoh: rename Music Musics')
            elif len(parsedInput) > 3:
                print('Kelebihan argumen! Perintah hanya membutuhkan dua argumen!')
            else:
                rename(parsedInput[1], parsedInput[2], current_dir)
        elif parsedInput[0].lower() == 'delete':
            if len(parsedInput) < 2:
                print('Berikan argumen pada perintah! Contoh: delete Videos')
            elif len(parsedInput) > 2:
                print('Kelebihan argumen! Perintah hanya membutuhkan satu argumen!')
            else:
                delete(parsedInput[1], current_dir)
        elif parsedInput[0].lower() == 'shutdown':
            if len(parsedInput) > 1:
                print(f'Perintah {parsedInput[0]} tidak membutuhkan argumen sama sekali!')
            else:
                sistem_nyala = shutdown()
        elif parsedInput[0].lower() == 'showspec':
            if len(parsedInput) > 1:
                print(f'Perintah {parsedInput[0]} tidak membutuhkan argumen sama sekali!')
            else:
                showSpec()
        elif parsedInput[0].lower() == 'showtime':
            if len(parsedInput) > 1:
                print(f'Perintah {parsedInput[0]} tidak membutuhkan argumen sama sekali!')
            else:
                showtime()
        elif parsedInput[0].lower() == 'changetime':
            if len(parsedInput) > 1:
                print(f'Perintah {parsedInput[0]} tidak membutuhkan argumen sama sekali!')
            else:
                change_timezone()
        elif parsedInput[0].lower() == 'help':
            if len(parsedInput) > 1:
                print(f'Perintah {parsedInput[0]} tidak membutuhkan argumen sama sekali!')
            else:
                showCommands()
        else:
            print(f'Perintah {parsedInput[0]} tidak dikenali!')

def main():
    # prosesPOST()
    # startingOS()
    standByCMD()

main()
