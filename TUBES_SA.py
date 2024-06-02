import time as t 

# Fungsi untuk perhitungan Brute Force
def brute_force(course_list, max_sks):
    n = len(course_list) 
    best_combination = [] 
    best_priority = 0
    
    # Generate all possible combinations of courses
    for i in range(1 << n):
        current_sks = 0
        current_priority = 0
        current_combination = []
        print(f" {(1 << n)}")

        for j in range(n): 
            if i & (1 << j):                                                 
                current_sks += course_list[j]['sks']
                current_priority += course_list[j]['priority']
                current_combination.append(course_list[j])

        # Check if this combination is the best so far
        if current_sks <= max_sks and current_priority > best_priority:
            best_priority = current_priority
            best_combination = current_combination

    return best_combination


def greedy(course_list, max_sks):
    # Sort the course list based on priority (descending)
    course_list.sort(key=lambda x: x['priority'], reverse=True)

    current_sks = 0
    selected_courses = []

    for course in course_list:
        if current_sks + course['sks'] <= max_sks:
            selected_courses.append(course)
            current_sks += course['sks']

    return selected_courses

# Contoh data

paket_courses = [
    {"name": "Sistem Operasi", "sks": 3, "priority": 9},
    {"name": "Jaringan Komputer", "sks": 4, "priority": 10},
    {"name": "Strategi Algoritma", "sks": 3, "priority": 8},
    {"name": "Teori Bahasa dan Automata", "sks": 3, "priority": 7},
    {"name": "Pengantar Kecerdasan Buatan", "sks": 3, "priority": 6},
]

ulang_courses = [
    {"name": "Struktur Data", "sks": 4, "priority": 13}
]

Reculang_course = [
    {"name": "Kalkulus Lanjut", "sks": 3, "priority": 12},
    {"name": "Bahasa Indonesia", "sks": 2, "priority": 11} 
]

atas_courses = [
    {"name": "Kewarganegaraan", "sks": 2, "priority": 3},
    {"name": "Bahasa Inggris Presentasi", "sks": 3, "priority": 4}, 
    {"name": "Interaksi Manusia Komputer", "sks": 3, "priority": 5} 
]

# MAX KAPASITAS
class const:
    max_sks = 24
    total_paket_sks = sum(course['sks'] for course in paket_courses)

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

# Calculate current SKS after adding repeated and recommended courses
current_sks = calc_AbsUlang(ulang_courses)
rec_courses = calc_RecUlang(current_sks, Reculang_course)

# Combine results into arrays
all_courses = paket_courses + ulang_courses + rec_courses + atas_courses

start_time_brute = t.time()
brute_result = brute_force(all_courses, const.max_sks)
end_time_brute = t.time()
brute_execution_time = end_time_brute - start_time_brute

start_time_greedy = t.time()
greedy_result = greedy(all_courses, const.max_sks)
end_time_greedy = t.time()
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