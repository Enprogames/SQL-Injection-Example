#!/bin/bash

function report_result() {
    # Gets the return value '$?'' of the last command and reports success or not
    last_cmd=$?
    if [[ $last_cmd -eq 0 ]]; then
        echo -e "Success."
    else
        echo -e "\nSomething went wrong! Bailing..."
        exit 1
    fi
}

OS=$(uname -a | cut -c1-5)
# venv
## create venv
echo -e "\n*** Checking to see if virtual environment exists"
if [[ -d "/venv" ]]; then
    echo -e "\n*** Creating new virtual environment using python-venv"
    if [[ $OS =~ "Linux" ]]; then
        echo "Making adjustments due to bad choice of operating system"
        python3 -m venv venv --prompt SQL-Injection-Example
    else
        python -m venv venv --prompt SQL-Injection-Example
    fi
    report_result
else
    echo -e "\n Virtual environment already exists in this directory."
fi

## activate venv
echo -e "\n*** Activating the python virtual environment for this script..."
if [[ $OS =~ "Linux" ]]; then
    source venv/bin/activate
else
    source venv/Scripts/activate
fi
report_result
echo -e "Using: $(which python)"

# upgrade pip
echo -e "\n*** Updating pip to latest version...\n"
python -m pip install --upgrade pip
report_result

# pip install
echo -e "\n*** Installing latest Python requirements...\n"
python -m pip install -r requirements.txt
report_result

# create .env file
echo -e "\n*** Creating .env file"
cat > .env << EOF
SECRET_KEY = 'Enter django secret key here'
EOF
report_result

echo -e "\nSetup Completed Successfully."
