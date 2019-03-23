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

    def load(self,path):
        with self.fs.open(path) as f:
            return pd.read_csv(f)

    def get_post(self, which='train'):
        path=os.path.join(self.default_path, which, 'post.csv').replace("\\","/")
        return self.load(path)

    def get_role(self, which='train'):
        path=os.path.join(self.default_path, which, 'role.csv').replace("\\","/")
        return self.load(path)

    def get_label_map(self):
        return self.load(os.path.join(self.default_path,'label_map.csv').replace("\\","/"))

    def get_role_answers(self):
        return self.load(os.path.join(self.default_path,'test','role_answers.csv').replace("\\","/"))

    def get_role_random(self):
        return self.load(os.path.join(self.default_path,'test','role_RANDOM.csv').replace("\\","/"))