def getSpesifikasi():
    return {
        'Motherboard': 'Asus H110M-K',
        'CPU': 'Intel Core™ i7-7700K',
        'Memory': 'V-GeN Platinum 16GB PC21300/2666Mhz',
        'Storage': 'SSD V-Gen Platinum SATA III 512 GB',
        'Graphic': 'Integrated graphics processor - Intel HD Graphics',
        'Audio': 'Realtek ALC887 8-channel High Definition Audio CODEC',
        'LAN': 'Realtek RTL8111H Gigabit LAN supports LANGuard'
    }

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
                'path': f'C:\\Users\\{getUsers()[0]}\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'jam_update': '09:03 AM',
                'tgl_update': '05/11/2023'
            },
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
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Desktop\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'jam_update': '07:28 PM',
                'tgl_update': '11/04/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Desktop\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Documents\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'jam_update': '11:35 AM',
                'tgl_update': '11/21/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Documents\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Downloads\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'jam_update': '05:12 AM',
                'tgl_update': '11/27/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Downloads\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Music\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'jam_update': ' 09:21 AM',
                'tgl_update': '11/08/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Music\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Pictures\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'jam_update': '10:15 AM',
                'tgl_update': '11/24/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Pictures\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Videos\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'jam_update': '10:13 AM',
                'tgl_update': '11/26/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Videos\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ]
    ]