import csv 
from src.utils.logger import get_logger

def deduplicate(input_path , output_path):
    seen_user_ids = set()

    logger = get_logger("DEDUPLICATION")
    i1 , un = 0 , 0

    with open(input_path, newline="") as infile, \
         open(output_path, "w", newline="") as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile,fieldnames=reader.fieldnames)
        

        writer.writeheader()

        for row in reader:
            user_id = row.get("user_id")
            i1+=1
            if user_id in seen_user_ids :
                continue

            un+=1
            seen_user_ids.add(user_id)
            writer.writerow(row)

    logger.info(f"Input records count : {i1}")
    logger.info(f"Unique records afte deduplication : {un}")
        
