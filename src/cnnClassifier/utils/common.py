from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox, exceptions
from box.exceptions import BoxValueError 
import yaml
from cnnClassifier import logger
from typing import Bool, Any
import os
import json
import joblib
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns ConfigBox

    Args:
        path_to_yaml (str): path to yaml file
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} successfully read')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose: Bool = True):
    """create list of directories

    Args:
        path_to_directories: list of directories to create
        verbose: whether to output success messages, default True
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'created ditectory at: {path}')


@ensure_annotations
def save_json(path: Path, data: dict):
    """saves json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f'json file saved at: {path}')


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """loads json data and returns ConfigBox

    Args:
        path (str): path to json file
    """

    with open(path, 'r') as f:
        content = json.load(f)
    
    logger.info(f'json file loaded from: {path}')
    return ConfigBox(content)


@ensure_annotations
def save_bin(path: Path, data: Any):
    """saves binary file

    Args:
        path (str): path to bin file
        data (Any): data to be saved
    """
    joblib.dump(value=data, filename=path)
    logger.info(f'bin file saved at: {path}')


@ensure_annotations
def load_bin(path: Path) -> Any:
    """loads binary file

    Args:
        path (str): path to bin file
    
    Returns:
        data: object stored in the file
    """

    data = joblib.load(path)
    logger.info(f'bin file loaded from: {path}')
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get file size in kB
    
    Args:
        path (str): path of the file
    
    Returns:
        size in kB 
    """

    size = round(os.paht.get_size(path)/1024)
    return f"~ {size} kB"


@ensure_annotations
def decode_image(imstring: str, filename: str):
    imdata = base64.decode(imstring)
    with open(filename, 'wb') as f:
        f.write(imdata)
        f.close()


@ensure_annotations
def encode_image_into_base64(imagepath: str):
    with open(imagepath, 'rb') as f:
        return base64.b64encode(f.read())