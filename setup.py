from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    from the requirements.txt , and it will return a list of 
    libraries,therefor imported list from the typing'''

    requirements=[]  ## this is for libraries requirement from requirements.txt
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() ## in order to read the file line by line
        requirements=[req.replace("\n","")for req in requirements] ## this replace function is use for replace "\n" with "blank space"  while import from requirements.txt

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
   
setup(
name='MachineLearning Project',
version="0.0.1",
author="Samuelvairagar",
author_email="samuelvairagar12@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)