from src.APSP.config.configuration import ConfigManager 
from src.APSP.components.data_validation import DataValidation 


class DataValidationPipeline: 
    def __init__(self):
        pass

    def main(self): 
        config=ConfigManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.schema_validation()