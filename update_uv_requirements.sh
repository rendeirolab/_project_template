# Get code
git clone git@github.com:rendeirolab/_project_template.git

# Make project `None` from template
uvx cookiecutter --no-input _project_template
cd None

# Remove all packages
# xargs uv remove < ../_project_template/requirements.txt
uv remove anndata cloudpickle fa2-modified fastcluster igraph leidenalg matplotlib networkx numpy pandas parmap pingouin pyarrow pymde scanpy scikit-image scikit-learn scipy seaborn seaborn-extensions tqdm
# xargs uv remove --dev < ../_project_template/requirements.dev.txt
uv remove black[d] git-lint ipython mypy pylint rich taskipy

# Remove lock
rm uv.lock

# Add all packages in latest versions
uv add -U --requirements ../_project_template/requirements.txt
uv add -U --dev --requirements ../_project_template/requirements.dev.txt

# Update pyproject.toml in template with versions from `None` project
