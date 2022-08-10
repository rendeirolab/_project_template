# A template repository for new projects

This template uses [cookiecutter](https://github.com/cookiecutter/cookiecutter) to create a new project instance.

The contents of the template <a href="{{ cookiecutter.project_slug }}">can be seen here</a>. Varibles with `{{ cookiecuter... }}` will be replaced with the values given at the time of repository creation from the template.

## Usage
Install cookiecutter and use it in the following manner:
```bash
python -m pip install cookiecutter
cookiecutter gh:rendeirolab/_project_template
```
You can also clone the repository and point to its path as sole argument.

Fields to be provided are:
- [required] `project_slug`: A consise and unique string for the project (no whitespace).
- [required] `project_name`: The human readable name of the project.
- `project_description`: An extended human readable description of the project.
- `zenodo_doi`: A DOI for data used/produced by the project.
- `biorxiv_doi`:  A DOI for the project's preprint.
- `full_name`: The user's full name.
- `username`:  The user's username (no whitespace).
- `email`: The user's email.

## Defaults
To have default values filled in (e.g. username, email) create a `.cookiecutterrc` file or use a `COOKIECUTTER_CONFIG` environmental variable [as described here](https://cookiecutter.readthedocs.io/en/stable/advanced/user_config.html).
The file should have, for example:
```yaml
default_context:
    full_name: "Audrey Roy"
    username: "aroy"
    email: "audreyr@cemm.oeaw.ac.at"
```
