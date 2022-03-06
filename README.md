SamplerBox PyPI server
====================

This is the PyPI server of SamplerBox

## How to add a new release with the make command?
You can use the following make command to create a new app release:
```bash
make bump app=python-midi version=3.0.1
```

## How to reference the libraries in `requirements.txt`?
Reference the package in your `requirements.txt` as follows:
```shell
--extra-index-url https://sampler-box.github.io/python-package-server/
python-midi==3.0.1
...
```
