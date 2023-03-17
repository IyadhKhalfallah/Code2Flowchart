import os

GITHUB_ACCESS_TOKEN = 'GITHUB_TOKEN'
OPENAI_API_KEY = 'OPENAI_KEY'

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

from tools.FlowchartGenTool import FlowchartGenTool
from tools.CodeExplanationTool import CodeExplanationTool

TOOLS = [
    {
        'tool': FlowchartGenTool,
        'summary': 'Generates a flowchart from a given context',
        'include': True
    },
{
        'tool': CodeExplanationTool,
        'summary': 'Explains code, in any language.',
        'include': True
    },
]
