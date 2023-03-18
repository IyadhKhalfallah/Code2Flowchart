import streamlit as st

from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.agents import initialize_agent

from code2flowchart.constants import TOOLS
from code2flowchart.utils.flowchart.mermaid import generate_flowchart
from code2flowchart.templates.prompt import flowchart_template


llm = OpenAI(temperature=0)


def generate_output(code):
    llm = OpenAI(temperature=0.9)

    prompt = flowchart_template(
        f"""
        {code}
        """)
    res = llm(prompt)
    return generate_flowchart(res.replace('```', ''))


def run_agent(code):
    tools = [tool['tool']() for tool in TOOLS if tool['include'] is True]

    memory = ConversationBufferMemory(memory_key="chat_history", output_key='output')

    agent = initialize_agent(tools, llm, agent="conversational-react-description", memory=memory, verbose=True)

    prompt = flowchart_template(
            f"""
            {code}
            """)

    agent.run(prompt)
    agent.run("Generate a correct mermaid.js flowchart syntax from the explanation you provided")


def main():
    st.title("Flowchart generator from code")

    # Add a text input box for the Python code
    code = st.text_area("Enter your Python code here:", max_chars=5000)
    # Add a submit button
    if st.button("Run Code"):
        # Run the Python code and display the output
        output = generate_output(code)
        st.image(output, caption="Generated Image", use_column_width=True)


main()
