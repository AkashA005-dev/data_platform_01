import csv
from src.utils.logger import get_logger

USER_SCHEMA = {
    "user_id" : int,
    "name" : str,
}

logger = get_logger("VALIDATOR")

# RAW_FILE = "data/raw/simple_invalid.csv"
# VALID_OUTPUT = "data/processed/valid_users.csv"
# INVALID_OUTPUT = "data/processed/invalid_users.csv"


def validate_row(row):
    errors = []

    for column , expected_type in USER_SCHEMA.items():
        value = row.get(column)
        
        
        if value is None or value == "":
            errors.append(f"{column} is missing")
            continue

        try:
            expected_type(value)
        except ValueError:
            errors.append(f"{column} has invalid type : {value}")
    
    return errors 

def process_file(RAW_FILE):
    valid_rows = []
    invalid_rows = []

    with open(RAW_FILE,newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            errors = validate_row(row)

            if errors:
                row["errors"] = "; ".join(errors)
                invalid_rows.append(row)
            else:
                valid_rows.append(row)
    return valid_rows , invalid_rows


def write_csv(path,rows,Fieldnames):
    with open(path,"w",newline="") as f:
        writer = csv.DictWriter(f,fieldnames=Fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def validate_data(VALID_OUTPUT, INVALID_OUTPUT , RAW_FILE):
    logger.info(f" Data Validation Started ")
    valid_rows , invalid_rows = process_file(RAW_FILE)

    if valid_rows:
        write_csv(VALID_OUTPUT,valid_rows,Fieldnames=valid_rows[0].keys())
    logger.info(f" Data validation valid rows : {len(valid_rows)} ")
    
    if invalid_rows:
        write_csv(INVALID_OUTPUT,invalid_rows,Fieldnames=invalid_rows[0].keys())
    logger.info(f" Data validation Invalid row count :  {len(invalid_rows)} ")
    
    print(f"Valid rows written: {len(valid_rows)}")
    print(f"Invalid rows written: {len(invalid_rows)}")

    logger.info(" Validation Completed ")