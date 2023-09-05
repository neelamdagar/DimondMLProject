from setuptools import find_packages,setup
from typing import List

hypen="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if hypen in requirements:
            requirements.remove(hypen)
        return requirements
setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Neelam',
    author_email="neelamdagar988@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)