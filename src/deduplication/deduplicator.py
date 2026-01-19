import csv 

def deduplicate(input_path , output_path):
    seen_user_ids = set()


    with open(input_path, newline="") as infile, \
         open(output_path, "w", newline="") as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile,fieldnames=reader.fieldnames)

        writer.writeheader()

        for row in reader:
            user_id = row.get("user_id")

            if user_id in seen_user_ids :
                continue

            seen_user_ids.add(user_id)
            writer.writerow(row)
