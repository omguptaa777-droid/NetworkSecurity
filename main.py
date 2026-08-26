from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.components.data_ingestion import DataIngestion 
from networksecurity.components.data_validation import DataValidation 
from networksecurity.components.data_transformation import DataTransformation

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()

        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)

        datavalidationconfig=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate the data validation")
        datavalidationartifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(datavalidationartifact)
        
        datatransformationconfig=DataTransformationConfig(trainingpipelineconfig)
        data_tranformation=DataTransformation(datavalidationartifact,datatransformationconfig)
        logging.info("Initiate the data transformation")
        datatransformationartifact=data_tranformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(datatransformationartifact)


    except Exception as e:
        raise NetworkSecurityException(e,sys)