import json
import requests
import pandas as pd
from io import StringIO

# define what a dataset contains
class dataset: 
    def __init__(self, tag, name, sep, url, skip):
        self.tag = tag
        self.url = url
        self.name = name
        self.sep = sep
        self.skip = skip

class datasetManager:
    def defineDatasets():
        with open("./classes/datasets.conf.json", 'r') as data_file:
            data = json.load(data_file)
        datasets = []
        for datasetConf in data:
            datasets.append(dataset(
                datasetConf['tag'], 
                datasetConf['name'], 
                datasetConf['seperator'], 
                datasetConf['url'], 
                datasetConf['skip']
            ))
        return datasets
    
    def loadDatasets(datasets):
        dataframes = {}
        # set categories
        for dataset in datasets:
            dataframes[dataset.tag] = {}
        # load files into categories
        for dataset in datasets:
            data = requests.get(dataset.url).text
            dataframe = pd.read_csv(StringIO(data), error_bad_lines=False, sep=dataset.sep, low_memory=False, skiprows=dataset.skip)
            dataframes[dataset.tag][dataset.name] = dataframe
        return dataframes

    def mapFeature(feature):
        with open(f"./classes/mapping/{feature}.mapping.json", 'r') as data_file:
            data = json.load(data_file)
        
        return data

    def renameFeatures(datasetName):
        with open(f"./classes/renaming/{datasetName}.renaming.json", 'r') as data_file:
            data = json.load(data_file)

        return data

        


        

