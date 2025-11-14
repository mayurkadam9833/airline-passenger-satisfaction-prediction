import os
import zipfile
from urllib.request import urlretrieve
from src.APSP.entity.config_entity import DataIngestionConfig 
from src.APSP.logging import logger
from src.APSP.utils.common import get_size

class DataIngestion: 
    def __init__(self,config:DataIngestionConfig):
        self.config=config 

    def download_file(self): 
        try: 
            if not os.path.exists(self.config.local_data_path): 
                url,header=urlretrieve(
                    url=self.config.source_url, 
                    filename=self.config.local_data_path)
                logger.info(f"{self.config.local_data_path} download sucessfully from following header:\n{header}")
            
            else: 
                logger.info(f"file is already exists of size {get_size(self.config.local_data_path)}")
        
        except Exception as e: 
            raise e 
    
    def unzip_file(self): 
        unzip_path=self.config.unzip_dir 
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_path,"r")as zipref: 
            zipref.extractall(unzip_path)
            logger.info(f"file extract sucessfully")
            
                
                
