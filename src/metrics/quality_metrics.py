import csv

def count_rows(path):
    with open(path, newline="") as f:
        return sum(1 for _ in csv.DictReader(f))
    

def generate_metrics(paths):
    return{
        "total_records" : count_rows(paths["invalid_data"]),
        "cleaned_records" : count_rows(paths["cleaned_data"]),
        "rejected_records" : count_rows(paths["rejected_data"]),
        "final_records" : count_rows(paths["final_output"])
    }

def rejection_breakdown(rejected_path):
    reasons = {}

    with open(rejected_path , newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            reason = row["error"]
            reasons[reason] = reasons.get(reason,0) + 1
    
    return reasons