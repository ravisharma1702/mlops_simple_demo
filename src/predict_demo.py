import os
import yaml
import argparse
import joblib
import json
import numpy as np
import requests

def read_params(config_path) :
    with open(config_path) as yaml_file :
        config = yaml.safe_load(yaml_file)
    return config

def predict(config_path):
    config = read_params(config_path)
    request = config["precit_request_file"]
    url = config["precition_service"]
    with open(request) as f:
        file_contents = f.read()

    response = requests.post(url, json=json.loads(file_contents))
    print(response.text)

if __name__ == "__main__" :
    args = argparse.ArgumentParser()
    args.add_argument("--config", default = "params.yaml")
    parsed_args = args.parse_args()
    predict(config_path=parsed_args.config)