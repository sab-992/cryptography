from pathlib import Path


# Logging
ENABLE_LOGGING: bool = False
PRINT_TO_STDOUT: bool = False
MAX_LOG_HASH_FILENAME_SIZE: int = 64
LOG_FOLDER_PATH: str = f"{Path(__file__).parent.resolve()}/logs"

# I/O
OUTPUT_FOLDER_PATH: str = "output"
INPUT_FOLDER_PATH: str = "input"