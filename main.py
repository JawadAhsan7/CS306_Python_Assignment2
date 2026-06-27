raw_data = " 101-Alice Smith-CS100 ; 102-Bob Jones-MA200 ; 103-Charlie Brown-CS100 ; 101-Alice Smith-MA200 "

def clean_raw_data(raw_data_input: str):
    cleaned_data_spaced = raw_data_input.split(";")
    cleaned_data = []

    for record in cleaned_data_spaced:
        indv_record = record.strip().split("-")
        cleaned_data.append(tuple(indv_record))        

    print(cleaned_data)


clean_raw_data(raw_data)