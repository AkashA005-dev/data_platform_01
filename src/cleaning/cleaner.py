import csv
from datetime import datetime

USER_SCHEMA1 = {
    "user_id" : int,
    "name" : str,
}

def clean_user_id(value):
    try:
        return int(str(value).strip()) , None
    except (TypeError , ValueError):
        return None , "INVALID_USER_ID"


def clean_name(value) :
    try:
        name = " ".join(value.split())
        return name , None
    except Exception:
        pass
    return None , "Invalid_Name"



def clean_invalid_data(input_path, cleaned_path, rejected_path):
    with open(input_path, newline="") as infile, \
         open(cleaned_path, "w", newline="") as cleaned_file, \
         open(rejected_path, "w", newline="") as rejected_file:
        
        reader = csv.DictReader(infile)

        fields = list(USER_SCHEMA1.keys())

        cleaned_writer = csv.DictWriter(
            cleaned_file, fieldnames=fields
        )

        fields = ["user_id", "name","error", "processed_at"]

        rejected_writer = csv.DictWriter(
            rejected_file , fieldnames=fields
        )

        cleaned_writer.writeheader()
        rejected_writer.writeheader()

        for row in reader:
            cleaned_row = {}
            errors = []

            user_id , err = clean_user_id(row.get("user_id"))
            if err:
                errors.append(err)
            
            cleaned_row["user_id"] = user_id

            name , err = clean_name(row.get("name"))
            if err:
                errors.append(err)
            
            cleaned_row["name"] = name


            if errors:
                row["error"] = ",".join(errors)
                row["processed_at"] = datetime.now()
                rejected_writer.writerow(row)
            else:
                cleaned_writer.writerow(cleaned_row)
                
