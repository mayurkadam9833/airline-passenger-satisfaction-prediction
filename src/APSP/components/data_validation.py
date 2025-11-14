import os 
import pandas as pd 
from src.APSP.entity.config_entity import DataValidationConfig 
from src.APSP.logging import logger


class DataValidation: 
    def __init__(self,config:DataValidationConfig):
        self.config=config 
    
    def schema_validation(self): 
        try: 
            data=pd.read_csv(self.config.unzip_data_path)
            all_cols=list(data.columns)
            schema=list(self.config.all_schema.keys()) 
            schema_stat=True

            for col in all_cols: 
                if col == "satisfaction":
                    continue 
                if col not in schema:
                    schema_stat=False 
                
            with open(self.config.status_file,"w")as file: 
                file.write(f"schema validation: {schema_stat}")
            
            logger.info("schema validation completed")
        
        except Exception as e: 
            raise e 
                    
