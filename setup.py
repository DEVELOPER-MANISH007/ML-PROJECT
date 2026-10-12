from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    thi fun will return list of requirement
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj if req.strip()]
        requirements = [req for req in requirements if req != HYPEN_E_DOT]

    return requirements    
    

setup(
    name='mlproject',
    version='0.0.1',
    author='manish',
    author_email='manish8755026341@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt')
    
)