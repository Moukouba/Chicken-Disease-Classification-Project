from cnnClassifier.constants import *
import os
from pathlib import Path
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig,
                                                PrepareBaseModelConfig,
                                                PrepareCallbacksConfig,
                                                TrainingConfig,
                                                EvaluationConfig)



class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        # Check if the local data file exists, if not, use the source URL
        if os.path.isfile(config.local_data_file):
            data_file = config.local_data_file
        else:
            data_file = config.source_URL

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL=config.source_URL,
            local_data_file = data_file,  # Use local file if it exists, else use URL
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config

    