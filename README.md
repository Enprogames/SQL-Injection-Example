# SQL Injection Example
This was created by Ethan Posner and Sebastien Van Den Bremt. A simple Django website to show how easy it is to use SQL injections when user inputs aren't sanitized. Created for a school project.

## Installation
1. Install python [here](https://www.python.org/downloads/). Make sure it is added to your PATH environment variable. Otherwise, you won't be able to run python commands from the terminal like this: `python script.py`.
1. Navigate to project folder using `cd projects` in git bash on windows or terminal on linux
2. Run `git clone https://github.com/Enprogames/SQL-Injection-Example.git`
3. Move into project directory: `cd SQL-Injection-Example`
4. Run setup.sh script: `./setup.sh`. If this is not desired, see alternative instructions below. This does the following:
    - Creates and activates a virtual environment with venv
    - Upgrades pip to latest version and installs all packages from requirements.txt
    - Installs pre-commit hooks as specified in .pre-commit-config.yaml
    - Creates .env file for django secret key. You must copy your django secret key into this file.
    - Creates post-merge hook which will do the following everytime a merge is done:
        - Activate virtual environment
        - Update pip and install any new packages from requirements.txt
    - Create update.sh script which can be used to run post-merge hook manually.
- Alternatively, to setup the project manually and avoid running the setup.sh script, run the following (if using windows, make sure to run windows instructions inside of git bash).
    1. Create python virtual environment using venv
        - On linux: `python3 -m venv venv --prompt SQL-Injection-Example`
        - On windows: `python -m venv venv --prompt SQL-Injection-Example`
    2. Activate virtual environment
        - On linux: source venv/bin/activate
        - On windows: `source venv/Scripts/activate`
    3. Update python package manager (PIP) to latest version
        - `python -m pip install --upgrade pip`
    4. Install all required packages from requirements.txt
        - `python -m pip install -r requirements.txt`
    5. Setup pre-commit hooks (optional if not contributing to project). This stops you from committing files which are improperly formatted.
        - `python -m pre_commit install`
    6. Create a .env file for the django secret key
        - ```
            cat > .env << EOF
            SECRET_KEY = 'Enter django secret key here'
            EOF
          ```
        - Ask the author for the django secret key

## Usage

1. Make sure all installation instructions were followed correctly and worked without errors. It is crucial that you have all required packages installed from requirements.txt.
2. Make sure you're in the root of the project directory
    - If you're outside of the sustainablinds directory, go into it with `cd SQL-Injection-Example`
    - If you're in the django-website directory, run `cd ..`
3. To start the website, run `src/manage.py runserver`
4. Click on the link in the terminal, or go to `http://127.0.0.1:8000/` in your browser.

At the time of writing, the following should be displayed in your browser if everything worked correctly
![website-homepage](Documentation/Images/{projectname-image}.jpg)

## License
Copyright 2022 Ethan Posner and Sebastien Van Den Bremt.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.