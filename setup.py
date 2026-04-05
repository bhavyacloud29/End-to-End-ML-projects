# Setup.py helps build pur entire ML project as a package. It defines the dependencies and metadata for the project.
# This file is used by pip to install the required packages for the project.
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This Function will return the list of requirements '''
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements




setup(
    name='ml_project',
    version='0.1.0',
    author='Bhavya',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A machine learning project package'
    )








