import os
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI
from templates.prompt import flowchart_template


llm = OpenAI(temperature=0)

prompt = flowchart_template(
"""

def get_github_content_by_file(owner, repo_name):

    def get_file_contents(content_file):
        contents = content_file.content.decode(content_file.encoding)
        return contents

    def get_folder_contents(folder):
        contents = folder.get_contents()
        file_contents_dict = {}
        for content in contents:
            if content.type == "file":
                file_contents_dict[content.path] = get_file_contents(content)
            elif content.type == "dir":
                folder_contents = get_folder_contents(content)
                file_contents_dict.update(folder_contents)
        return file_contents_dict

    g = Github()
    repo = g.get_repo(f"{owner}/{repo_name}")
    contents = repo.get_contents("")
    file_contents = get_folder_contents(contents)

    dict_code = dict()
    for file_name, content in file_contents.items():
        dict_code[file_name] = content
    
    return dict_code
""")
print(llm(prompt))
    