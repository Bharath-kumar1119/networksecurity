from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation,DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == '__main__':
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingPipelineConfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate Data Ingestion")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)

        datavalidationconfig = DataValidationConfig(trainingPipelineConfig)
        datavalidation = DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate Data Validation")
        datavalidation_artifact = datavalidation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(datavalidation_artifact)



    except Exception as e:
        raise NetworkSecurityException(e,sys)