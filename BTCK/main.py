import csv

# Danh sách lưu trữ sinh viên
students = []

# Hàm đọc dữ liệu từ file CSV
def load_students(filename="students.csv"):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            global students
            students = [dict(id=row['id'], name=row['name'], age=int(row['age']), major=row['major']) for row in reader]
        print(f"Đã tải {len(students)} sinh viên từ file.")
    except FileNotFoundError:
        print("File không tồn tại. Bắt đầu với danh sách rỗng.")

# Hàm lưu dữ liệu vào file CSV
def save_students(filename="students.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'name', 'age', 'major']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
    print("Đã lưu danh sách sinh viên vào file.")

# Thêm sinh viên
def add_student():
    id = input("Nhập mã sinh viên: ").strip()
    if any(s['id'] == id for s in students):
        print("Lỗi: Mã sinh viên đã tồn tại!")
        return
    name = input("Nhập tên sinh viên: ").strip()
    try:
        age = int(input("Nhập tuổi: "))
    except ValueError:
        print("Tuổi phải là số nguyên!")
        return
    major = input("Nhập ngành học: ").strip()
    students.append({'id': id, 'name': name, 'age': age, 'major': major})
    print("Đã thêm sinh viên thành công.")

# Cập nhật sinh viên theo id
def update_student():
    id = input("Nhập mã sinh viên cần cập nhật: ").strip()
    for student in students:
        if student['id'] == id:
            student['name'] = input(f"Nhập tên mới ({student['name']}): ") or student['name']
            age_input = input(f"Nhập tuổi mới ({student['age']}): ")
            if age_input:
                try:
                    student['age'] = int(age_input)
                except ValueError:
                    print("Tuổi không hợp lệ, giữ nguyên giá trị cũ.")
            student['major'] = input(f"Nhập ngành học mới ({student['major']}): ") or student['major']
            print("Cập nhật thành công.")
            return
    print("Không tìm thấy sinh viên với id này!")

# Xoá sinh viên theo id
def delete_student():
    id = input("Nhập mã sinh viên cần xoá: ").strip()
    for i, student in enumerate(students):
        if student['id'] == id:
            del students[i]
            print("Xoá thành công.")
            return
    print("Không tìm thấy sinh viên với id này!")

# Tìm kiếm sinh viên theo tên
def search_student():
    name = input("Nhập tên sinh viên cần tìm: ").strip().lower()
    found = [s for s in students if name in s['name'].lower()]
    if found:
        print("Kết quả tìm kiếm:")
        for s in found:
            print(s)
    else:
        print("Không tìm thấy sinh viên.")

# Hiển thị danh sách sinh viên
def show_students():
    if not students:
        print("Danh sách sinh viên rỗng.")
        return
    print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Major':<15}")
    print("-"*50)
    for s in students:
        print(f"{s['id']:<5} {s['name']:<20} {s['age']:<5} {s['major']:<15}")

# Menu chính
def menu():
    load_students()
    while True:
        print("\n----- QUẢN LÝ SINH VIÊN -----")
        print("1. Thêm sinh viên")
        print("2. Cập nhật sinh viên")
        print("3. Xoá sinh viên")
        print("4. Tìm kiếm sinh viên")
        print("5. Hiển thị danh sách sinh viên")
        print("6. Lưu danh sách vào file")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            show_students()
        elif choice == '6':
            save_students()
        elif choice == '0':
            save_students()
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()