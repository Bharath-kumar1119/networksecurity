from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


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

        datatransformationconfig = DataTransformationConfig(trainingPipelineConfig)
        datatransformation = DataTransformation(datavalidation_artifact,datatransformationconfig)
        logging.info("Initiate Data Transformation")
        datatransformation_artifact = datatransformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(datatransformation_artifact)


    except Exception as e:
        raise NetworkSecurityException(e,sys)