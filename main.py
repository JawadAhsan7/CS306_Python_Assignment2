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

########################### LOGICAL ERRORS IN THE SOLUTION DUE TO MISUNDERSTANDING OF REQUIREMENTS ###########################
##################### ALL CODE BELOW THIS LINE MUST BE REWRITTEN TO COMPLETE THE ASSIGNMENT REQUIREMENTS #####################

# 2. Using appropriate operations, find and print:
#     ◦ The students enrolled in both courses.
#     ◦ The students enrolled only in CS100.
#     ◦ A master list of all unique students taking either CS100 or MA200.


# STUDENTS ENROLLED IN BOTH COURSES
print("\nStudents enrolled in both courses:")
print(cs_students.intersection(ma_students))

# STUDENTS ENROLLED ONLY IN CS100
print("\nStudents enrolled in CS100 and not in MA200:")
print(cs_students.difference(ma_students))

# ALL UNIQUE CS100 AND MA200 STUDENTS
print("\nMaster list of students enrolled in either CS100 or MA200")
print(cs_students.union(ma_students))
