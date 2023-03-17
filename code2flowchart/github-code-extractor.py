from github import Github
import requests

from constants import GITHUB_ACCESS_TOKEN

access_token = GITHUB_ACCESS_TOKEN
g = Github(access_token)


repo = g.get_repo('jina-ai/agentchain')
contents = repo.get_contents("")

files_dict = {}

for content in contents:
    if content.type == "file":
        # Getting the file content using the raw URL
        file_content = requests.get(content.download_url).text
        files_dict[content.name] = file_content

print(files_dict)
