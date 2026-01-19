from src.cleaning.cleaner import clean_invalid_data
from src.validation.validator import validate_data
from src.deduplication.deduplicator import deduplicate
from src.utils.logger import get_logger

RAW_FILE = "data/raw/simple_invalid.csv"
VALID_OUTPUT = "data/processed/valid_users.csv"
INVALID_OUTPUT = "data/processed/invalid_users.csv"

logger = get_logger("PIPELINE")

if __name__ == "__main__":

    logger.info("Pipeline Started")
    # validate_data(VALID_OUTPUT=VALID_OUTPUT , INVALID_OUTPUT=INVALID_OUTPUT , RAW_FILE=RAW_FILE)

    clean_invalid_data(
        input_path="data/invalid/invalid_data.csv",
        cleaned_path="data/cleaned_rejected/cleaned_invalid_data.csv",
        rejected_path="data/cleaned_rejected/rejected_data.csv"
    )

    # deduplicate(input_path="data/cleaned_rejected/cleaned_invalid_data.csv" , output_path="data/processed/final_users.csv")

    logger.info("Pipeline completed successfully")