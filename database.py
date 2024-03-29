def getHelp():
    return {
        'help': 'Menampilkan perintah-perintah apa saja yang bisa digunakan.',
        'dir': "Menampilkan semua folder dan file yang ada di suatu directory.",
        'cd': "Membuka directory, contoh: 'cd Videos' atau 'cd ..'.",
        'mkdir': "Membuat folder baru, contoh: 'mkdir Movie'.",
        'rename': "Mengganti nama folder, contoh: 'rename Movie Movies'.",
        'delete': "Menghapus folder, contoh: 'delete Movies'.",
        'showspec': "Menampilkan spesifikasi perangkat keras pada sistem komputer.",
        'showtime': "Menampilkan tanggal dan jam yang sedang berjalan.",
        'changetime': 'Mengganti zona waktu.',
        'clearscr': 'Membersihkan layar.',
        'shutdown': 'Mematikan sistem.'
    }

def getTimezone():
    gmt = []

    for i in range(13):
        gmt.append(f'Etc/GMT+{i}')
    
    for i in range(15):
        gmt.append(f'Etc/GMT-{i}')

    return gmt

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
    return ['Bagus', 'Anugrah']

def getDataLogin():
    return [
        {
            'username': 'bagus',
            'password': 'Bagus1234'
        },
        {
            'username': 'anugrah',
            'password': 'Anugrah1234'
        }
    ]

def getDirectory(): 
    return [
    [
        f'C:\\Users\\{getUsers()[0]}',
        f'C:\\Users\\{getUsers()[0]}\\Desktop',
        f'C:\\Users\\{getUsers()[0]}\\Documents',
        f'C:\\Users\\{getUsers()[0]}\\Downloads',
        f'C:\\Users\\{getUsers()[0]}\\Music',
        f'C:\\Users\\{getUsers()[0]}\\Pictures',
        f'C:\\Users\\{getUsers()[0]}\\Videos'
    ],
    [
        f'C:\\Users\\{getUsers()[1]}',
        f'C:\\Users\\{getUsers()[1]}\\Desktop',
        f'C:\\Users\\{getUsers()[1]}\\Documents',
        f'C:\\Users\\{getUsers()[1]}\\Downloads',
        f'C:\\Users\\{getUsers()[1]}\\Music',
        f'C:\\Users\\{getUsers()[1]}\\Pictures',
        f'C:\\Users\\{getUsers()[1]}\\Videos'
    ]
]

def get_dir_content():
    return [
    [
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '09:03 AM',
                'tgl_update': '05/11/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Desktop',
                'nama': 'Desktop',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:28 PM',
                'tgl_update': '11/04/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Documents',
                'nama': 'Documents',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '11:35 AM',
                'tgl_update': '11/21/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Downloads',
                'nama': 'Downloads',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '05:12 AM',
                'tgl_update': '11/27/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Music',
                'nama': 'Music',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': ' 09:21 AM',
                'tgl_update': '11/08/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Pictures',
                'nama': 'Pictures',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '10:15 AM',
                'tgl_update': '11/24/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Videos',
                'nama': 'Videos',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '10:13 AM',
                'tgl_update': '11/26/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\bgs-os.py',
                'nama': 'bgs-os.py',
                'jenis': '     ',
                'ukuran': 152463,
                'jam_update': '01:50 PM',
                'tgl_update': '11/25/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\bgs-os.exe',
                'nama': 'bgs-os.exe',
                'jenis': '     ',
                'ukuran': 23928635,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Desktop\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:28 PM',
                'tgl_update': '11/04/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Desktop\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Documents\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '11:35 AM',
                'tgl_update': '11/21/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Documents\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Downloads\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '05:12 AM',
                'tgl_update': '11/27/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Downloads\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Music\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': ' 09:21 AM',
                'tgl_update': '11/08/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Music\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Pictures\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '10:15 AM',
                'tgl_update': '11/24/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Pictures\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Videos\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '10:13 AM',
                'tgl_update': '11/26/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[0]}\\Videos\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ]
    ],
    [
        [
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '09:03 AM',
                'tgl_update': '05/11/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Desktop',
                'nama': 'Desktop',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:28 PM',
                'tgl_update': '11/04/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Documents',
                'nama': 'Documents',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '11:35 AM',
                'tgl_update': '11/21/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Downloads',
                'nama': 'Downloads',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '05:12 AM',
                'tgl_update': '11/27/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Music',
                'nama': 'Music',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': ' 09:21 AM',
                'tgl_update': '11/08/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Pictures',
                'nama': 'Pictures',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '10:15 AM',
                'tgl_update': '11/24/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Videos',
                'nama': 'Videos',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '10:13 AM',
                'tgl_update': '11/26/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Desktop\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:28 PM',
                'tgl_update': '11/04/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Desktop\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Documents\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '11:35 AM',
                'tgl_update': '11/21/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Documents\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Documents\\simulasi-os.py',
                'nama': 'simulasi-os.py',
                'jenis': '     ',
                'ukuran': 23184,
                'jam_update': '08:31 AM',
                'tgl_update': '11/20/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Documents\\simulasi-os.exe',
                'nama': 'simulasi-os.exe',
                'jenis': '     ',
                'ukuran': 6982341,
                'jam_update': '11:35 AM',
                'tgl_update': '11/21/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Downloads\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '05:12 AM',
                'tgl_update': '11/27/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Downloads\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Downloads\\intellij.exe',
                'nama': 'intellij.exe',
                'jenis': '     ',
                'ukuran': 792065498,
                'jam_update': '05:12 AM',
                'tgl_update': '11/27/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Downloads\\pycharm.exe',
                'nama': 'pycharm.exe',
                'jenis': '     ',
                'ukuran': 533543254,
                'jam_update': '10:18 AM',
                'tgl_update': '11/26/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Downloads\\xampp.exe',
                'nama': 'xampp.exe',
                'jenis': '     ',
                'ukuran': 152421675,
                'jam_update': '12:27 AM',
                'tgl_update': '11/26/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Music\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': ' 09:21 AM',
                'tgl_update': '11/08/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Music\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Pictures\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '10:15 AM',
                'tgl_update': '11/24/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Pictures\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ],
        [
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Videos\\.',
                'nama': '.',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '10:13 AM',
                'tgl_update': '11/26/2023'
            },
            {
                'path': f'C:\\Users\\{getUsers()[1]}\\Videos\\..',
                'nama': '..',
                'jenis': '<DIR>',
                'ukuran': 0,
                'jam_update': '07:46 AM',
                'tgl_update': '11/28/2023'
            }
        ]
    ]
]