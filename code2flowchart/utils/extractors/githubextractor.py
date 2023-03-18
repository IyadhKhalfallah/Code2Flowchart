import os
import requests
from github import Github


g = Github(os.environ['GITHUB_ACCESS_TOKEN'])


def get_github_files(owner, repo):
    repo = g.get_repo(f'{owner}/{repo}')
    contents = repo.get_contents("")

    files_dict = {}

    for content in contents:
        if content.type == "file":
            # Getting the file content using the raw URL
            file_content = requests.get(content.download_url).text
            files_dict[content.name] = file_content

    return files_dict
