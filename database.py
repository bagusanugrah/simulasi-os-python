def getPerangkatKeras():
    return ['RAM', 'Harddisk Drive', 'CD ROM Drive', 'USB Port']

def getOSInfo(): 
    return {
        'name': 'BGS OS',
        'version': 1.0,
        'company': 'BGS Corporation'
    }

def getUsers():
    return ['Anugrah']

def getDirectory(): 
    return [
        f'C:\\Users\\{getUsers()[0]}',
        f'C:\\Users\\{getUsers()[0]}\\Desktop',
        f'C:\\Users\\{getUsers()[0]}\\Documents',
        f'C:\\Users\\{getUsers()[0]}\\Downloads',
        f'C:\\Users\\{getUsers()[0]}\\Music',
        f'C:\\Users\\{getUsers()[0]}\\Pictures',
        f'C:\\Users\\{getUsers()[0]}\\Videos'
    ]

def get_dir_content():
    return [
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Desktop',
                'nama': 'Desktop',
                'jenis': '<DIR>',
                'jam_update': '07:28 PM',
                'tgl_update': '11/04/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Documents',
                'nama': 'Documents',
                'jenis': '<DIR>',
                'jam_update': '11:35 AM',
                'tgl_update': '11/21/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Downloads',
                'nama': 'Downloads',
                'jenis': '<DIR>',
                'jam_update': '05:12 AM',
                'tgl_update': '11/27/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Music',
                'nama': 'Music',
                'jenis': '<DIR>',
                'jam_update': ' 09:21 AM',
                'tgl_update': '11/08/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Pictures',
                'nama': 'Pictures',
                'jenis': '<DIR>',
                'jam_update': '10:15 AM',
                'tgl_update': '11/24/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Videos',
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