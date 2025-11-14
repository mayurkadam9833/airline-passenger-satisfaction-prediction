from src.APSP.constants import *
from src.APSP.utils.common import read_yaml,create_dir
from src.APSP.entity.config_entity import DataIngestionConfig,DataValidationConfig



class ConfigManager:
    def __init__(
        self, 
        config_file=CONFIG_FILE_PATH, 
        schema_file=SCHEMA_FILE_PATH, 
        params_file=PARAMS_FILE_PATH): 

        self.config=read_yaml(config_file)
        self.schema=read_yaml(schema_file)
        self.params=read_yaml(params_file)

        create_dir([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)-> DataIngestionConfig: 
        config=self.config.data_ingestion 

        create_dir([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir, 
            source_url=config.source_url, 
            local_data_path=config.local_data_path, 
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self)-> DataValidationConfig: 
        config=self.config.data_validation 
        schema=self.schema.COLUMNS 

        create_dir([config.root_dir])

        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir, 
            unzip_data_path=config.unzip_data_path, 
            status_file=config.status_file, 
            all_schema=schema
        )
        return data_validation_config