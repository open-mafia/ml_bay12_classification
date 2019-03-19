"""Data loading."""

import logging
import os
import gcsfs
import pandas as pd
import cloudstorage as gcs

class GCSLoader():
    """Loads the data from google cloud storage.
    Propably in future will be rebuilt to authenticate using service accounts instead, this is just for start.

    Attributes
    ----------
    fs : gcsfs.core.GCSFileSystem
        Google cloud storage file system object pointing to project in gcs
    path : str
        Path to where the data for mafia classification is.

     """

    def __init__(self,project, path):
        self.fs= gcsfs.GCSFileSystem(project=project)
        self.default_path=path


    def get_post(self, which='train'):
        path=os.path.join(self.default_path, which, 'post.csv').replace("\\","/")
        with self.fs.open(path) as f:
            post = pd.read_csv(f)
        return post
        
        
    def get_role(self, which='train'):
        path=os.path.join(self.default_path, which, 'role.csv').replace("\\","/")
        with self.fs.open(path) as f:
            role = pd.read_csv(f)
        return role

    def get_label_map(self):
        with self.fs.open(os.path.join(self.default_path,'label_map.csv').replace("\\","/")) as f:
            label_map = pd.read_csv(f)
        return label_map