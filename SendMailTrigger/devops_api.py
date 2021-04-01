import os
import requests
import logging

# See link down below to generate your Private Access Token
AZURE_DEVOPS_PAT = 'yjimnwnt2qftgjb5dripkmpokxyh4quuelujltl3jaypqpahclra'
url = 'https://dev.azure.com/santhoshkdhana/Leukemia Classification/_apis/wit/workitems/$issue?api-version=5.1'


def create_issue(title_text:str):
    """Create a new issue for the particular image that wasn't be detect by the ML model

    Args:
        title_text (str): title of the new issue
    """
    data = [
    {
    "op": "add",
    "path": "/fields/System.Title",
    "value": f"{title_text}"
    }
    ]

    r = requests.post(url, json=data, 
        headers={'Content-Type': 'application/json-patch+json'},
        auth=('', AZURE_DEVOPS_PAT))

    logging.info("Successfully created new work item")