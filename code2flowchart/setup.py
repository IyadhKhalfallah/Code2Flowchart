from setuptools import find_packages, setup
setup(
    name='code2flowchart',
    packages=find_packages(include=['code2flowchart']),
    version='0.1.0',
    description='Transform your code to a simple explanatory flowchart.',
    author='Iyadh Khalfallah',
    license='MIT',
    install_requires=['langchain', 'Pillow', 'PyGithub', 'requests', 'setuptools', 'streamlit'],
)
