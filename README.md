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
- `project_description`: A human readable description of the project.
- `editor`: Which text editor is being used - will generate a few auxiliary files for specific editors.
- `zenodo_doi`: A DOI for data used/produced by the project.
- `biorxiv_doi`:  A DOI for the project's preprint.
- `full_name`: The user's full name.
- `username`:  The user's username (no whitespace).
- `email`: The user's email.
- [do not change] `template_version`: This will keep track of what template version was used to 
- `create_github_repo`: Whether to create a github repository for the project (requires the `gh` command line tool to be installed and authenticated).

## Defaults
To have default values filled in (e.g. username, email) create a `.cookiecutterrc` file or use a `COOKIECUTTER_CONFIG` environmental variable [as described here](https://cookiecutter.readthedocs.io/en/stable/advanced/user_config.html).
The file should have, for example:
```yaml
default_context:
    full_name: "Audrey Roy"
    username: "aroy"
    email: "audreyr@cemm.oeaw.ac.at"
```

## Authenticating with git/Github
To use SSH to authenticate with Github (recommended):
1. Generate a ssh-key with the command: `ssh-keygen`
2. [Add the generated **public** key to your Github profile settings](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
3. Make cookiecutter use SSH by default by adding to your `~/.cookiecutterrc` file:
```yaml
abbreviations:
    gh: git@github.com:{0}.git
```
Alternatively, you can continue to use HTTPS (default) but if you have two factor authentication activated in your Github profile (highly recommended), you will have to:
1. [Create a Github application token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
2. Provide that as your Github password when interacting with Github using git/cookiecutter.

## Editing
To make modifications/improvements to the template open a [pull request on GitHub](https://github.com/rendeirolab/_project_template/pulls).

When merging the PR, make sure to:
1. Add the modifications to the [Changelog](Changelog.md)
2. Increment the version number on [cookiecutter.json](cookiecutter.json).
