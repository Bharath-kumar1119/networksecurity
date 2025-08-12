'''
The setup.py is an essential part of packagaing and 
distributing Python Projects. It is used by setuptools
(or disutils in older python versions) to define the configuration 
of your project, such as its metadata, dependenices and more...
'''
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements()->List[str]:
    '''
    This function will return the list of requirements

    '''
    requirements_lst:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            ## Read lines from the file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!= '-e.':
                    requirements_lst.append(requirement)

    except FileNotFoundError:
        print("Requirement.tst not found")
    
    return requirements_lst

### It's a  metadata of our project
setup(
name = "Netwroek Security",
version="0.0.1",
author="Bharath",
author_email="bharath9502kumar@gmail.com",
packages= find_packages(),
install_requires = get_requirements()
)