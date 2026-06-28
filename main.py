##########################################################################################################################
#################################################### HELPER FUNCTIONS ####################################################
##########################################################################################################################

def cleanRawData(raw_data_input: str, clean_list: list) -> None:
    """convert raw data from string to a list

    Args:
        raw_data_input (str): a raw string that holds the data that needs to be cleaned
        clean_list (list): the list you want to add the cleaned records to
    """
    cleaned_data_spaced = raw_data_input.split(";")

    for record in cleaned_data_spaced:
        indv_record = record.strip().split("-")
        clean_list.append(tuple(indv_record))


def addIndividualRecord(new_record: str, clean_list: list) -> None:
    """Add a new record to the list.

    Args:
        new_record (str): New record to add to the list. Format: ID, Name, Course (as string comma separated)
        clean_list (list): The list to add your individual record to.
    """
    clean_list.append(tuple(new_record.split(', ')))


def printRecords(records_list: list | set):
    """Print the cleaned data list

    Args:
        records_list (list | set): List containing the clean data.
    """
    for record in records_list:
        id, name, course = record
        print(f"ID: {id}, Name: {name}, Course: {course}")


##########################################################################################################################
###################################################### PROGRAM FLOW ######################################################
##########################################################################################################################

raw_data = " 101-Alice Smith-CS100 ; 102-Bob Jones-MA200 ; 103-Charlie Brown-CS100 ; 101-Alice Smith-MA200 "
clean_records_database = []

# CLEANING THE DATA
cleanRawData(raw_data, clean_records_database)

# ADDING A NEW STUDENT RECORD
addIndividualRecord("104, Diana Prince, PH100", clean_records_database)

# PRINT ENTIRE DATABASE LIST
print("All Records: ")
printRecords(clean_records_database)


##################################### COURSE ANALYSIS ################################
# TWO SEPARATE SETS FOR CS AND MA STUDENTS
cs_students = set(record[1] for record in clean_records_database if record[2] == "CS100") 
ma_students = set(record[1] for record in clean_records_database if record[2] == "MA200") 

# NOT REQUIRED BY THE ASSIGNMENT
# print("\nCS Students: ")
# printRecords(cs_students)

# print("\nMA Students: ")
# printRecords(ma_students)

# STUDENTS ENROLLED IN BOTH COURSES (WITH DUPLICATE NAME ENTRIES)
students_enrolled_in_both_courses = [record[1] for record in clean_records_database if record[2] == "CS100" or record[2] == "MA200"]
print("\nStudents enrolled in both courses: ")
print(students_enrolled_in_both_courses)

# STUDENTS ENROLLED ONLY IN CS100
students_enrolled_only_in_cs100 = [record[1] for record in clean_records_database if record[2] == "CS100"]
print("\nStudents enrolled in CS100: ")
print(students_enrolled_only_in_cs100)

# ALL UNIQUE STUDENTS WITH EITHER CS100 OR MA100
unique_student_list_cs100_ma200 = list(set(record[1] for record in clean_records_database if record[2] == "CS100" or record[2] == "MA200")) # Fix required: student with PH100 must not be added
print("\nMaster list of students taking either CS100 or MA200: ")
print(unique_student_list_cs100_ma200)