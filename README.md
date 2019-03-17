ML: Bay12 Mafia Classification
=======================

**Goal:** Classifying mafia-or-town for Bay12 Forums games

Getting Started
---------------

Using conda, create an environment and activate it:
```cmd
conda env create -f env.yml --quiet
activate ml-bay12
```

Next, move to the source directory and "install" the library in development mode:
```cmd
cd src
python setup.py develop
cd ..
```

This should dynamically link the Python library code to your environment. You are now free to start working in a notebook/in the editor/etc.:

```cmd
jupyter notebook
```

Make sure to read `notebooks/README.md`.

Contributing
------------

Since we have a small team, we use the following convention:
- Create branches in the style `fl/branch-name`, where `fl` are your initials and the branch name is taken from the issue/feature tracker.
- Don't commit to master (unless it's a tiny fix :P), create a branch and merge it in instead.

Note that you will not be able to contribute without the data. We hold the data in GCP (for now), not in git. Sorry! 