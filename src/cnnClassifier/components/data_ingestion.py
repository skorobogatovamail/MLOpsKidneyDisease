import os
import zipfile
import gdown
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    

    def download_file(self) -> str:
        """fetch data from URL"""

        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            root_dir = self.config.root_dir
            os.makedirs(root_dir, exist_ok=True)
            
            logger.info(f'downloading file from {dataset_url} to {zip_download_dir}')
            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(url=prefix+file_id, output=zip_download_dir)
            logger.info(f'Sucessfully downloaded file from {dataset_url} to {zip_download_dir}')
        except Exception as e:
            raise e
    

    def extract_zip_file(self):
        """Extracts zip file into new directory"""
        zip_dir = self.config.local_data_file
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(zip_dir, 'r') as f:
            f.extractall(unzip_dir)

