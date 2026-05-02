import os
import sys
from ultralytics import YOLO
from src.logger import logging
from src.exception import CustomException


class PredictionPipeline:
    def __init__(self):
        self.model_path = "best.pt"

    def predict(self,image_path):

        try:
            logging.info("Prediction Pipeline: Model is loading")

            model = YOLO(self.model_path)

            logging.info(f"Prediction is started on image: {image_path}")

            results = model.predict(source=image_path, conf=0.5)

            logging.info("Prediction Pipeline: Detection successfully complete!")

            return results
        
        except Exception as e:
            raise CustomException(e,sys)
