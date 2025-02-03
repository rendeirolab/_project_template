Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com>)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## Unreleased

### Added
  - Add choice of software manager from `uv` (default), `conda` or `pip`.
  - Add choice of editor `vscode`.
  - Add `pyarrow`, `igraph`, `leidenalg`, `fa2-modified`, `fastcluster` and `pymde` as dependencies.

### Changed
  - Add lower bound for all optional dependencies.
  - Changed project __init__.config to remove reference to 'gtex'.

### Removed
  - Makefile targets for upload, processing and download of data.
  - Removed PyQt5 dev dependency.


## [0.4.1] 2025-02-03

### Changed
  - Add missing `scanpy` dependency.

## [0.4.0] 2024-12-31

### Added
  - Cookiecutter option to choose `project_type` from "research" or "software".
  - Automatic git repo creation with initial commit including optional remote repo creation.

### Changed
  - Updated `pyproject.toml` to full compliance.
  - Made project immediately 'buildable' from start with `uv build` command.
  - Project build version file location now dependent on `project_type` (via setuptools_scm).
  - Fix scikit-image dependency version.
  - Fix seaborn_extensions dependency version.
  - Fix git init command instructions.

### Removed
  - Removed `poetry` build system.


## [0.3.0] 2024-10-23

### Added
  - `src.ops` - reusable operations across datasets.
  - Add instructions to create remote repository from command line

### Changed
  - Moved global config to `src/__init__.py`.
  - Better formatting of cookiecutter post-hook message

### Removed
  - Removed `src/types.py` and associated custom types.
  - Removed `src/_config.py`.
  - Removed `imc` requirement.


## [0.2.0] 2023-12-15

### Added
  - Add instructions on how to use SSH or HTTPS with git/github.
  - Added a post gen hook

### Changed
  - Fixed reference to `/research/groups/lab_rendeiro`. Should have been `/research/lab_rendeiro`.
  - Update post cookie creation instructions to default to SSH.
  - Add more packages to be skipped by mypy.

### Removed
  - Removed redundant `requirements.txt`.
  - Retire use of `project_name` variable.


## [0.1.0] 2022-08-23

### Added
  - Added versioning to the template
  - Added Changelog
