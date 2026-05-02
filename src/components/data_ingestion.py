import os
import sys
from src.logger import logging
from src.exception import CustomException

class DataIngestionConfig:

    def __init__(self):

        self.model_file_path = "best.pt"

class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logging.info("Starting the data ingestion process")

        try:

            if os.path.exists(self.ingestion_config.model_file_path):
                logging.info("File is there:{self.ingestion_config.model_file_path}")

                return self.ingestion_config.model_file_path
            else:
                logging.error("No file is there in artifacts folde name as best.pt")
                raise Exception
        except Exception as e:
            raise CustomException(e,sys)
        
