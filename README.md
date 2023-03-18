# Code2Flowchart

Code2Flowchart is a Python package that generates a flowchart from a given code in any programming language. With Code2Flowchart, you can easily visualize the control flow of your code and identify any potential issues.

## Usage

To use Code2Flowchart, you will need to set your personal GitHub access token and OpenAI API key as environment variables. Once you have done this, you can run the `main.py` file and update it to be adapted to the GitHub repo you want to generate flowcharts from. The output will be a flowchart for every file you have in your repo.

If you want to directly inject a piece of code instead of giving a repo, you can run `playground.py`, which will run a Streamlit playground to add your code and generate a flowchart from it.

To get started, make sure you have installed all the dependencies by running:

`pip install -r requirements.txt`

## Environment Variables

You will need to set the following environment variables before using Code2Flowchart:

- `GITHUB_ACCESS_TOKEN`: Your GitHub access token, which you can obtain from your GitHub account settings.
- `OPENAI_API_KEY`: Your OpenAI API key, which you can obtain from the OpenAI website.

## Contributing

Contributions are welcome! If you have any suggestions or issues, please open an issue or pull request on the GitHub repo.

## License

Code2Flowchart is licensed under the MIT License. See the `LICENSE` file for more information.