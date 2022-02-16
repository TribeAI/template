[![gh-template](https://img.shields.io/badge/use%20this-template-blue?logo=github)](https://github.com/TribeAI/template/generate)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

## Getting Started

Most of the dependencies for the template are written to environment.yml in the bootstrap script. There are a few things that you need to install and setup to be able to do that however.

1. Install [Anaconda](https://www.anaconda.com/products/individual) (or [miniconda](https://docs.conda.io/en/latest/miniconda.html)) if you don't have it already (and make sure to `conda init`).
1. Install the [Git Large File Storage](https://git-lfs.github.com/) extension.

Once you have both Anaconda and git-lfs simply run:

```sh
python bootstrap.py
conda activate [env-name]
```

## Structure

This is simply a recommended starting scaffold. None of the tooling with this template requires any specific naming/folder conventions outside of the standard git/Github conventions (like `.gitignore` and the `.github` folder) and Python/conda requirements (like `setup.cfg` and `environment.yml`). Feel free to rearrange this however is optimal for your project.

```
├── LICENSE
├── README.md
├── data
│
├── models             <- Serialized trained models and model artifacts
│
├── notebooks          <- Jupyter notebooks
│
├── reports            <- Any output/presentation artifacts (like HTML, PDF, LaTeX, etc.)
│
├── environment.yml    <- `conda` environment file to configure package dependencies
│                           (created by `bootstrap.py`)
│
├── setup.cfg          <- makes `src/` pip installable so classes/modules can be imported
│                           (created by `bootstrap.py`)
│
├── src                <- Source code meant to be imported as modules in notebooks or scripts
│  
├── scripts            <- Python files intended to be run from the command line (and not imported)
│  
└── tests              <- (optional)
```

## How do I?

### Use a specific version of Python

Update the Python dependency in [environment.yml](environment.yml) and update the environment: `conda env update --file environment.yml --prune`

```yml
name: tribe
dependencies:
    - python=3.9 # <------ specify Python version
    - ipython
    - jupyter
    - pip:
          - pre-commit
```

### Update package requirements

Same as above.

### Work with large data files

Git will warn you of any file added that is larger than 50mb and [Github blocks pushes](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#file-size-limits) with any file larger than 100mb.

This template repository is already configured to use [Git Large File Storage](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) for common data file formats in [`.gitattributes`](.gitattributes) however. If you want to either commit one of these file types normally (not using LFS) or add additional formats for LFS, simply add add/remove from this file.

### Remove a large file I accidentally comitted

You won't. We use a [pre-commit hook](https://github.com/pre-commit/pre-commit-hooks) that checks for large files to make sure that you never add them in the first place.

## Resources

-   [Hitchhiker's Guide to Python](https://docs.python-guide.org/)
-   [Real Python: Python Code Quality](https://realpython.com/python-code-quality/)
-   [Python Packaging User Guide](https://packaging.python.org/en/latest/)
-   [conda vs. pip vs. virtualenv commands](https://docs.conda.io/projects/conda/en/latest/commands.html#conda-vs-pip-vs-virtualenv-commands)
-   [pre-commit hooks](https://pre-commit.com/hooks.html)

## LICENSE

MIT License

Copyright (c) 2022 Tribe AI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
