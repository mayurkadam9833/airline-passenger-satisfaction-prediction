import os 
from typing import List 
from setuptools import setup,find_packages 

# this function read dependencies required for project from requirements.txt 
def get_requirements()-> List[str]: 
    requirements_list:List[str]=[]
    try: 
        with open("requirements.txt","r")as file: 
            lines=file.readlines()
            for line in lines: 
                requirement=line.strip()
                if requirement and requirement != "-e .": 
                    requirements_list.append(requirement)

    except FileNotFoundError: 
        print("requirements.txt not found....")

    return requirements_list 

# setup config for project
setup(
    version="0.0.1", 
    author="Mayur", 
    packages=find_packages(),             # automatically find packages
    install_requires=get_requirements()   # install required packages from requirements.txt
)

