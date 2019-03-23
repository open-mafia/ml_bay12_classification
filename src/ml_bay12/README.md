### Google Cloud Storage Loader usage
To be able to load from google cloud storage you will need to install these libs:
```
pip install google-cloud-storage
pip install gcsfs
```

In order to connect to GCS I suggest logging in via Google cloud SDK shell, which you can find [here](https://cloud.google.com/sdk/docs/quickstarts), after choosing your OS.

There you will also find steps to go through with initializing, logging via your google account and then choosing the project. Follow 4 steps that are listed in ```Initilize SDK```.
Don't create service account yet, for now this is the way to access gcs.

Other useful links: 
- [gcsfs](https://gcsfs.readthedocs.io/en/latest/) 
- [Another way to access gcs](https://cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python)
