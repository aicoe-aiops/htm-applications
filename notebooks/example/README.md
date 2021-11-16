# Anomaly Detection example code with dataset

The data set and example code is taken from [htm.core](https://github.com/htm-community/htm.core) community.

## Prerequisites

- Standard Python 3.7+ (Recommended)

## Building from source

- Fork the HTM-community htm.core repository from [Github](https://github.com/htm-community/htm.core)

`git clone https://github.com/htm-community/htm.core`

- At a command prompt, `cd` to the root directory of this repository.

- Run: `python setup.py install --user --force`

This will build and install a release version of htm.core. The --user option prevents the system installed site-packages folder from being changed and avoids the need for admin privileges. The --force option forces the package to be replaced if it already exists from a previous build. Alternatively you can type pip uninstall htm.core to remove a previous package before performing a build.

- After that completes you are ready to import the library
```
$ python
>>> import htm  #python library
>>> import htm.bindings #c++ Extension
```

You can run the unit test with

`python setup.py test`

After the passed test, we can now run the anomaly code for the given dataset.
