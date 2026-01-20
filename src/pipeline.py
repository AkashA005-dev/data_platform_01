from src.cleaning.cleaner import clean_invalid_data
from src.validation.validator import validate_data
from src.deduplication.deduplicator import deduplicate
from src.utils.logger import get_logger
from src.utils.config_loader import load_config

RAW_FILE = "data/raw/simple_invalid.csv"
VALID_OUTPUT = "data/processed/valid_users.csv"
INVALID_OUTPUT = "data/processed/invalid_users.csv"

logger = get_logger("PIPELINE")

if __name__ == "__main__":

    config = load_config("config/pipeline_config.json")

    paths = config["paths"]

    logger.info("Pipeline started with config-driven Paths")

    
    # validate_data(VALID_OUTPUT=VALID_OUTPUT , INVALID_OUTPUT=INVALID_OUTPUT , RAW_FILE=RAW_FILE)

    clean_invalid_data(
        input_path=paths["invalid_data"],
        cleaned_path=paths["cleaned_data"],
        rejected_path=paths["rejected_data"]
    )

    deduplicate(input_path=paths["cleaned_data"] , output_path=paths["final_output"])

    logger.info("Pipeline completed successfully")