# -*- coding: utf-8 -*-

"""Bootstrap template repository."""

import logging
import re
import subprocess
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.getLevelName("INFO"),
    handlers=[logging.StreamHandler(sys.stdout)],
    format="%(asctime)s - %(levelname)s - %(message)s",
)

setup = """[metadata]
name = {package_name}
version = 0.0.1
author = {author}
description = [[ DESCRIPTION ]]
long_description = file: README.md
long_description_content_type = text/markdown
url = {url}
project_urls =
    Bug Tracker = {url}/issues

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.9

[options.packages.find]
where = src
"""

environment = """name: {user}_{repo}
dependencies:
    - python=3.9
    - pip
    - ipython
    - jupyter
    - pip:
          - pre-commit
          - types-PyYAML
"""

if __name__ == "__main__":
    logging.info("Getting repo information")
    url = (
        subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            check=True,
            capture_output=True,
        )
        .stdout.decode("utf-8")
        .strip()
    )

    name_match = re.search(r"^https://github.com/(\w+)/(\w+).git$", url, re.IGNORECASE)

    if name_match:
        user = name_match.group(1)
        repo = name_match.group(2)

    logging.info("Writing environment.yml")
    with open("environment.yml", "x") as fh:
        fh.write(environment.format(user=user, repo=repo))

    logging.info("Writing setup.cfg")
    with open("setup.cfg", "x") as fh:
        fh.write(setup.format(package_name=repo, author=user, url=url))

    # make sure git LFS is setup for your account
    logging.info("Initializing git-lfs")
    subprocess.run(["git", "lfs", "install"], check=True)

    logging.info("Checking for conda update")
    subprocess.run(
        ["conda", "update", "-n", "base", "-c", "defaults", "conda"], check=True
    )

    # create and activate a new anaconda environment
    logging.info("Creating conda environment")
    subprocess.run(["conda", "env", "create", "-f", "environment.yml"], check=True)

    # needed to run commands from within conda environment
    conda_run = ["conda", "run", "-n", f"{user}_{repo}"]

    # Setup pre-commit for the repo
    logging.info("Checking for pre-commit hooks updates")
    subprocess.run(conda_run + ["pre-commit", "autoupdate"], check=True)

    logging.info("Installing pre-commit hooks")
    subprocess.run(conda_run + ["pre-commit", "install"], check=True)

    logging.info("Initial pre-commit test run")
    subprocess.run(conda_run + ["pre-commit", "run", "--all-files"], check=True)

    logging.info("Installing /src as a module with pip")
    subprocess.run(["pip", "install", "-e", "."], check=True)

    print(
        "\nTo start using the template and environment:"
        + f"\n\n\033[92m\tconda activate {user}_{repo}\033[0m"
    )
