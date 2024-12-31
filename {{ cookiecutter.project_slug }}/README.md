# {{ cookiecutter.project_slug }}

<!-- [![Zenodo badge](https://zenodo.org/badge/doi/<<zenodo_doi>>.svg)](https://doi.org/<<zenodo_doi>>)
[![bioRxiv badge](https://zenodo.org/badge/doi/<<biorxiv_doi>>.svg)](https://doi.org/<<biorxiv_doi>>) ⬅️ read the preprint here
 -->

{{ cookiecutter.project_description }}

This repository was created with a [cookiecutter template](https://github.com/rendeirolab/_project_template), version {{ cookiecutter.template_version }}.

## Organization

- The [metadata](metadata) directory contains metadata relevant to annotate the samples.
- [The samples.csv file](metadata/samples.csv) is the master record of all analyzed samples.
- The [src](src) directory contains source code used to analyze the data.
- Raw data  is under the `data` directory (likely empty in a remote repository on GitHub).
- Processing of the data creates files under the `processed`  directory.
- Outputs from the analysis are present in the `results` directory, with subfolders pertaining to each part of the analysis as described below.
- Assembled figures from plots are under the `figures` directory.
- Manuscript files are under the `manuscript` directory.

## Reproducibility

### Running

To see all available steps type:
```bash
$ make
```

Steps used for the initiall processing of raw data are marked with the `[dev]` label.
```
Makefile for the {{ cookiecutter.project_slug }} project/package.
Available commands:
help                Display help and quit
requirements        Install Python requirements
process             [dev] Process raw data into processed data types
sync                [dev] Sync data/code to CeMM's cluster
upload_data         [dev] Upload processed files to Zenodo
download_data       Download processed data from Zenodo (for reproducibility)
interactive         [dev] Run an interactive session for analysis
analysis            Run the actual analysis
```

To reproduce analysis using the pre-preocessed data, one would so:

```bash
$ make help
$ make requirements   # install python requirements using pip
$ make download_data  # download data from Zenodo
$ make analysis       # run the analysis scripts
```

#### Requirements

- Python 3.10+
- Python packages as specified in the [requirements file](requirements.txt) - install with `make requirements` or `pip install -r requirements.txt`.

#### Virtual environment

It is recommended to use some virtualization or compartimentalization software such as virtual environments or conda to install the requirements.

Here's how to create a virtualenvironment with the repository and installed requirements:

```bash
git clone git@github.com:rendeirolab/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
