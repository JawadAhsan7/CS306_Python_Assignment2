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
printRecords(clean_records_database)
