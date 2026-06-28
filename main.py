raw_data = " 101-Alice Smith-CS100 ; 102-Bob Jones-MA200 ; 103-Charlie Brown-CS100 ; 101-Alice Smith-MA200 "
clean_records_database = []

def cleanRawData(raw_data_input: str):
    cleaned_data_spaced = raw_data_input.split(";")

    for record in cleaned_data_spaced:
        indv_record = record.strip().split("-")
        clean_records_database.append(tuple(indv_record))

def addIndividualRecords(new_record):
    clean_records_database.append(tuple(new_record.split(', ')))

def printRecords(records_list):
    for record in records_list:
        id, name, course = record
        print(f"ID: {id}, Name: {name}, Course: {course}")

cleanRawData(raw_data)
addIndividualRecords("104, Diana Price, PH100")

print("All Records: ")
printRecords(clean_records_database)

cs_students = set(record for record in clean_records_database if record[2] == "CS100")
ma_students = set(record for record in clean_records_database if record[2] == "MA200")

print("\nCS Students: ")
printRecords(cs_students)

print("\nMA Students: ")
printRecords(ma_students)

students_enrolled_in_both_courses = [record[1] for record in clean_records_database]
print("\nStudents enrolled in both courses: ")
print(students_enrolled_in_both_courses)

students_enrolled_only_in_cs100 = [record[1] for record in clean_records_database if record[2] == "CS100"]
print("\nStudents enrolled in CS100: ")
print(students_enrolled_only_in_cs100)

unique_student_list_cs100_ma200 = set(record[1] for record in clean_records_database)
print("\nMaster list of students taking either CS100 or MA200: ")
print(unique_student_list_cs100_ma200)