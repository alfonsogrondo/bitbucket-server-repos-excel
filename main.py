import settings
import requests
import json
import pandas as pd
from requests.auth import HTTPBasicAuth
from string import Template

def GetRepos(path, authentication):
    url = settings.BB_API_URL + '/' + path + '/repos/'
    msg_template = Template('***** GETTING $path  *****')
    
    print(msg_template.substitute(path=path))
    
    response = requests.get(url, auth=authentication)
    data = json.loads(response.text)
    repos = data['values']
    for item in repos:
        item['links'] = item['links']['clone'][0]['href']
    
    # drop JSON into a DataFrame
    repos_df = pd.DataFrame.from_dict(repos)
    
    # remove unnessary columns
    repos_df.drop(['project','state','scmId','statusMessage','forkable','public'], axis = 1, inplace = True)

    return repos_df

def GetNestedURL(json):
 # rewrite links item to retrieve the primary href only
    for item in json:
        item['links'] = item['links']['self'][0]['href']
    return json
   

def main():
    print("***** CONNECTING TO BITBUCKET API... *****") 
    
    # grab authentication vars from .env
    auth = HTTPBasicAuth(settings.USERNAME, settings.PASSWORD)
    response = requests.get(settings.BB_API_URL, auth=auth)
    excel_file = settings.EXCEL_OUTPUT_DIRECTORY + 'output.xlsx'

    data = json.loads(response.text)
    projects = data['values']
    GetNestedURL(projects)
   
    projects_df = pd.DataFrame.from_dict(projects)
    projects_df.to_excel(excel_file, sheet_name='Bitbucket Projects')
    # output the project repositories to sheets within an Excel workbook
    for item in projects:
        project_df = GetRepos(item['key'], auth)
        with pd.ExcelWriter(excel_file, mode='a') as writer:
            project_df.to_excel(writer, sheet_name=item['key'])


main()
    



