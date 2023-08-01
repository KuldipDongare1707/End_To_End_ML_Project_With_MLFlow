from MLFlowProject import logger
from MLFlowProject.pipeline.Stage_01_data_ingetion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion  Stage "
try:
        logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed  <<<<< \n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e