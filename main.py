from src.APSP.logging import logger
from src.APSP.pipeline.data_ingestion_pipeline import DataIngestionPipeline 
from src.APSP.pipeline.data_validation_pipeline import DataValidationPipeline

stage_one="Data ingestion" 

if __name__ == "__main__": 
    try: 
        logger.info(f"<<<< stage:{stage_one} started >>>>")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_one} completed >>>>")
    except Exception as e: 
        logger.info(e)
        raise e 
    
stage_two="Data Validation" 

if __name__ == "__main__": 
    try: 
        logger.info(f"<<<< stage:{stage_two} started >>>>")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_two} completed >>>>")
    except Exception as e: 
        logger.info(e)
        raise e 