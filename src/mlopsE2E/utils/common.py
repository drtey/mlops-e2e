import os 
from box.exceptions import BoxValueError
import yaml
from mlopsE2E import logger
import logging
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """reads yaml file and returns
    
    Args:
        path_to_yaml (str): Path to the yaml file
        
    Raises:
        ValueError: If the file is empty
        
    Returns:
        ConfigBox: The content of the yaml file as a ConfigBox object
    
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Error reading yaml file: yaml file is empty")
    except Exception as e:
        raise e
    
    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of direcoires
    
    Args:
        path_to_directories (list): List of directories to create
        ignore_log (bool, optional): if multiple logs should be ignored. Defaults to False.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")
            


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data
    
    Args:
        path (Path): path to save the json file
        data (dict): data to save
    """
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"Data saved at: {path}")
    
    
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json data
    
    Args:
        path (Path): path to load the json file
    
    Returns:
        ConfigBox: data as class object from ConfigBox instead of dictionary
    """
    
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"Data loaded sucessfully from: {path}")
    return ConfigBox(content)



@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary data
    
    Args:
        data (Any): data to save as binary 
        path (Path): path to save the binary file
    """
    
    joblib.dump(value=data, filnema=path)
    logger.info(f"Data as bynary file saved at: {path}")
    
    
    
@ensure_annotations
def get_size(path: Path) -> str:
    """get size of the file
    
    Args:
        path (Path): path to the file
        
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    
    return f"~ {size_in_kb} KB"