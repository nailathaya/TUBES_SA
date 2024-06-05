import time as t 

# User database
users = {
    "panjek": {
        "password": "p1",
        "nama": "Muhammad Farhan",
        "nim": "1301220050",
        "ip": 3.65,
        "semester": 4,
        "paket_courses": [
            {"name": "Sistem Operasi", "sks": 3, "priority": 9},
            {"name": "Jaringan Komputer", "sks": 4, "priority": 10},
            {"name": "Strategi Algoritma", "sks": 3, "priority": 8},
            {"name": "Teori Bahasa dan Automata", "sks": 3, "priority": 7},
            {"name": "Pengantar Kecerdasan Buatan", "sks": 3, "priority": 6}
        ],
        "ulang_courses": [
        ],

        "reculang_courses": [
        ],

        "atas_courses": [
            {"name": "Kewarganegaraan", "sks": 2, "priority": 3},
            {"name": "Bahasa Inggris Presentasi", "sks": 3, "priority": 4},
            {"name": "Interaksi Manusia Komputer", "sks": 3, "priority": 5}
        ]
    },
    "adipra": {
        "password": "p2",
        "nama": "Adrian Prakoso",
        "nim": "1301220278",
        "ip": 3.39,
        "semester": 4,
        "paket_courses": [
            {"name": "Sistem Operasi", "sks": 3, "priority": 9},
            {"name": "Jaringan Komputer", "sks": 4, "priority": 10},
            {"name": "Strategi Algoritma", "sks": 3, "priority": 8},
            {"name": "Teori Bahasa dan Automata", "sks": 3, "priority": 7},
            {"name": "Pengantar Kecerdasan Buatan", "sks": 3, "priority": 6},
            {"name": "RPL: Analisis dan Perancangan PL", "sks": 3, "priority": 6}
        ],
        "ulang_courses": [
        ],

        "reculang_courses": [
        ],
        
        "atas_courses": [
            {"name": "Kewarganegaraan", "sks": 2, "priority": 3},
            {"name": "Bahasa Inggris Presentasi", "sks": 3, "priority": 4},
            {"name": "Interaksi Manusia Komputer", "sks": 3, "priority": 5}
        ]
    },
    "haidarsr": {
        "password": "p3",
        "nama": "Haidar Sayyid",
        "nim": "1301223105",
        "ip": 3.6,
        "semester": 4,
        "paket_courses": [
            {"name": "Sistem Operasi", "sks": 3, "priority": 9},
            {"name": "Jaringan Komputer", "sks": 4, "priority": 10},
            {"name": "Strategi Algoritma", "sks": 3, "priority": 8},
            {"name": "Teori Bahasa dan Automata", "sks": 3, "priority": 7},
            {"name": "Pengantar Kecerdasan Buatan", "sks": 3, "priority": 6}
        ],
        "ulang_courses": [
            {"name": "Algoritma Pemrograman", "sks": 4, "priority": 11}
        ],
        "reculang_courses": [
            
        ],
        "atas_courses": [
            {"name": "Kewarganegaraan", "sks": 2, "priority": 3},
            {"name": "Bahasa Inggris Presentasi", "sks": 3, "priority": 4},
            {"name": "Interaksi Manusia Komputer", "sks": 3, "priority": 5}
        ]
    },
    "maruffirdaus": {
        "password": "p4",
        "nama": "Muhammad Ma'ruf Firdaus",
        "nim": "1301223001",
        "ip": 3.8,
        "semester": 4,
        "paket_courses": [
            {"name": "Sistem Operasi", "sks": 3, "priority": 9},
            {"name": "Jaringan Komputer", "sks": 4, "priority": 10},
            {"name": "Strategi Algoritma", "sks": 3, "priority": 8},
            {"name": "Teori Bahasa dan Automata", "sks": 3, "priority": 7},
            {"name": "Pengantar Kecerdasan Buatan", "sks": 3, "priority": 6}
        ],
        "ulang_courses": [
    
        ],
        "reculang_courses": [
            
        ],
        "atas_courses": [
            {"name": "Kewarganegaraan", "sks": 2, "priority": 3},
            {"name": "Bahasa Inggris Presentasi", "sks": 3, "priority": 4},
            {"name": "Interaksi Manusia Komputer", "sks": 3, "priority": 5}
        ]
    },
    "ditorizkyka": {
        "password": "p5",
        "nama": "Andito Rizkyka",
        "nim": "1301220016",
        "ip": 3.89,
        "semester": 4,
        "paket_courses": [
            {"name": "Sistem Operasi", "sks": 3, "priority": 9},
            {"name": "Jaringan Komputer", "sks": 4, "priority": 10},
            {"name": "Strategi Algoritma", "sks": 3, "priority": 8},
            {"name": "Teori Bahasa dan Automata", "sks": 3, "priority": 7},
            {"name": "Pengantar Kecerdasan Buatan", "sks": 3, "priority": 6}
        ],
        "ulang_courses": [
    
        ],
        "reculang_courses": [
            
        ],
        "atas_courses": [
            {"name": "Kewarganegaraan", "sks": 2, "priority": 3},
            {"name": "Bahasa Inggris Presentasi", "sks": 3, "priority": 4},
            {"name": "Interaksi Manusia Komputer", "sks": 3, "priority": 5}
        ]
    }
}

# Login function
def login():
    username = input(f"Enter username\t: ")
    password = input(f"Enter password\t: ")

    if username in users and users[username]["password"] == password:
        print()
        print(f"Welcome, {users[username]['nama']}!")
        print(f"NIM\t\t: {users[username]['nim']}")
        print(f"IP Semester\t: {users[username]['ip']}")
        print(f"Semester\t: {users[username]['semester']}")
        return users[username]
    else:
        print("Invalid username or password")
        return None

# Fungsi untuk perhitungan Brute Force
def brute_force(course_list, max_sks):
    n = len(course_list)            # Memeriksa banyak course dalam array course_list
    best_combination = []           # Variabel untuk menyimpan kombinasi mata kuliah terbaik
    best_priority = 0               # Variabel untuk menyimpan jumlah nilai prioritas terbaik
    
    # Perulangan untuk menemukan dan mengecek semua kombinasi pemilihan mata kuliah
    for i in range(1 << n):
        current_sks = 0
        current_priority = 0
        current_combination = []

        for j in range(n): 
            if i & (1 << j):                                               
                current_sks += course_list[j]['sks']
                current_priority += course_list[j]['priority']
                current_combination.append(course_list[j])

        # Mengecek kombinasi saat ini apakah yang terbaik
        if current_sks <= max_sks and current_priority > best_priority:
            best_priority = current_priority
            best_combination = current_combination

    return best_combination


def greedy(course_list, max_sks):
    # Mengurutkan course dalam array course_list secara descending berdasarkan nilai prioritas
    course_list.sort(key=lambda x: x['priority'], reverse=True)

    current_sks = 0           # Variabel untuk menyimpan jumlah sks dari mata kuliah yang dipilih
    selected_courses = []     # Variabel untuk menyimpan data mata kuliah yang dipilih
    
    # Perulangan untuk menemukan kombinasi mata kuliah dengan profit maksimal
    for course in course_list:
        if current_sks + course['sks'] <= max_sks:
            selected_courses.append(course)
            current_sks += course['sks']

    return selected_courses

# MAX KAPASITAS
class const:
    max_sks = 24 
    

# MATKUL PAKET DAN ULANG
def calc_AbsUlang(ulang_courses):
    curr_sks = const.total_paket_sks
    if len(ulang_courses) > 0:
        total_ulang_sks = sum(course['sks'] for course in ulang_courses)
        if const.total_paket_sks + total_ulang_sks <= const.max_sks:
            curr_sks = const.total_paket_sks + total_ulang_sks
    return curr_sks

# MATKUL DISARANKAN MENGULANG
def calc_RecUlang(curr_sks, Reculang_course):
    Rec_course = []
    for course in Reculang_course:
        print(f"Matkul Disarankan Mengulang: {course['name']}")
        if curr_sks + course['sks'] <= const.max_sks:
            # INPUT USER
            m = input("Mengulang matkul? (y/n): ")
            if m == 'n':
                course['sks'] = 0
            elif m == 'y' and (curr_sks + course['sks'] <= const.max_sks):
                curr_sks += course['sks']
                Rec_course.append(course)
        else:
            print(f"Tidak bisa mengulang mata kuliah {course['name']}")
    return Rec_course

# SISA SKS 
def calc_RemainingSKS(curr_sks):
    return const.max_sks - curr_sks

# Main process
user_data = login()
if user_data:
    paket_courses = user_data['paket_courses']
    ulang_courses = user_data['ulang_courses']
    Reculang_course = user_data['Reculang_course']
    atas_courses = user_data['atas_courses']

    total_paket_sks = sum(course['sks'] for course in paket_courses)

    # Calculate current SKS after adding repeated and recommended courses
    current_sks = calc_AbsUlang(ulang_courses, total_paket_sks)
    rec_courses = calc_RecUlang(current_sks, Reculang_course)

    # Combine results into arrays
    all_courses = paket_courses + ulang_courses + rec_courses + atas_courses

    start_time_brute = time.time()
    brute_result = brute_force(all_courses, const.max_sks)
    end_time_brute = time.time()
    brute_execution_time = end_time_brute - start_time_brute

    start_time_greedy = time.time()
    greedy_result = greedy(all_courses, const.max_sks)
    end_time_greedy = time.time()
    greedy_execution_time = end_time_greedy - start_time_greedy

    # Print selected courses
    def print_selected_courses(method, courses):
        print(f"\nCourses selected using {method}:")
        for course in courses:
            print(f"- {course['name']} (SKS: {course['sks']}, Priority: {course['priority']})")

    print_selected_courses("Brute Force", brute_result)
    print_selected_courses("Greedy", greedy_result)

    # Comparison of the results
    def compare_results(brute, greedy):
        brute_sks = sum(course['sks'] for course in brute)
        brute_priority = sum(course['priority'] for course in brute)
        greedy_sks = sum(course['sks'] for course in greedy)
        greedy_priority = sum(course['priority'] for course in greedy)

        print("\nComparison of Brute Force and Greedy results:")
        print(f"Total SKS (Brute Force): {brute_sks}")
        print(f"Total Priority (Brute Force): {brute_priority}")
        print(f"Total SKS (Greedy): {greedy_sks}")
        print(f"Total Priority (Greedy): {greedy_priority}")

        if brute_priority > greedy_priority:
            print("Metode Brute Force menghasilkan rekomendasi mata kuliah yang lebih efektif.")
        elif brute_priority < greedy_priority:
            print("Metode Greedy menghasilkan rekomendasi mata kuliah yang lebih efektif.")
        else:
            print("Kedua metode menghasilkan rekomendasi mata kuliah yang sama.")

    compare_results(brute_result, greedy_result)

    print()

    print("== WAKTU EKSEKUSI ==")
    print("Waktu eksekusi Brute Force:", brute_execution_time)
    print("Waktu eksekusi Greedy:", greedy_execution_time)

    if brute_execution_time < greedy_execution_time:
        print("Waktu eksekusi dengan metode Brute Force lebih efektif.")
    elif brute_execution_time > greedy_execution_time:
        print("Waktu eksekusi dengan metode Greedy lebih efektif.")
    else:
        print("Kedua metode memiliki waktu eksekusi yang sama.")