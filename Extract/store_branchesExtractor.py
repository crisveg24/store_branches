import requests
import pandas as pd
import numpy as np

class store_branches:
    def __init__(self, csv_path):
        self.csv = csv_path
    def queries(self):
        data = pd.read_csv(self.csv)
    def response (self):
        return self.data.head(5)
