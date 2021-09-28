import csv


def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, newline="") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader, None)
        students = []
        for row in reader:
            row[2] = float(row[2])
            students.append(row)

        students.sort(key=lambda item: item[2], reverse=True)
        names = list(map(lambda student: student[0], students))
        return names[:number_of_top_students]


def write_students_info(file_path_of_students_info, file_path_out):
    with open(file_path_of_students_info, newline="") as file:
        reader = csv.reader(file, delimiter=",")
        header = next(reader, None)
        students = []
        for row in reader:
            students.append(row)

    students.sort(key=lambda item: item[1], reverse=True)

    with open(file_path_out, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for student in students:
            writer.writerow(student)


if __name__ == "__main__":
    print(get_top_performers("../data/students.csv"))
    write_students_info("../data/students.csv", "data/students.csv")
