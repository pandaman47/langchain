from setuptools import setup, find_packages

HYPHEN_E = '-e .'

def get_requirements(file_path:str) -> list[str]:
    """
    This function returns a list of requirements from the given file path.
    """
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
        return requirements
    

setup(
name='langchain-projects',
version='0.0.1',
description='A collection of LangChain projects',
author='Saketh',
packages= find_packages(),
install_requires= get_requirements('requirements.txt'),

)