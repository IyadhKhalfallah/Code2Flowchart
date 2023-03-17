# Import things that are needed generically
import os
from langchain.llms import OpenAI
from utils.mermaid import generate_flowchart
from templates.prompt import flowchart_template


llm = OpenAI(temperature=0)

tools = [
    Tool(
        name="Generate flowchart",
        func=lambda n: generate_flowchart(n),
        description="useful for when you need to explain the code and generate a flowchart from it"
    )
]

agent = initialize_agent(tools, llm, agent="conversational-react-description", verbose=True)

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

res = llm(prompt)
generate_flowchart(res.replace('```', ''))
#
#
# agent.run(prompt)
