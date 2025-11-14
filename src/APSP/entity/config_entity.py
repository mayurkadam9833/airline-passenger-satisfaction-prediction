from pathlib import Path 
from dataclasses import dataclass 


@dataclass(frozen=True)
class DataIngestionConfig: 
    root_dir: Path
    source_url: str 
    local_data_path: Path 
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig: 
    root_dir: Path 
    unzip_data_path: Path 
    status_file: str
    all_schema: dict