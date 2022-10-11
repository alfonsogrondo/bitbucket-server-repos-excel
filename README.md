# Python script to fetch Bitbucket Server Repositories and write to spreadsheet

# Getting Started

create a .env file with the following properties:

```
USERNAME=<your BB username>
PASSWORD=<your BB password>
BB_API_URL=<BB URL>/rest/api/1.0/projects
EXCEL_OUTPUT_DIRECTORY=dist
```
This script is designed to run with Python3 so either ensure python --version is 3 or run with python3 <main.py>.
Change pip to pip3 below.


# Install Dependencies
```
RUN pip install -r requirements.txt
```
# Running the script

```
python main.py
```
