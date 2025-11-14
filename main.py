from src.APSP.logging import logger
from src.APSP.pipeline.data_ingestion_pipeline import DataIngestionPipeline 


stage_one="Data ingestion" 

if __name__ == "__main__": 
    try: 
        logger.info(f"<<<< stage:{stage_one} started >>>>")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_one} started >>>>")
    except Exception as e: 
        logger.info(e)
        raise e 