from setuptools import setup, find_packages
from  typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
	requirements=[]
	with open(file_path) as file_obj:
		requirements=file_obj.readlines()
		[req.replace("\n","") for req in requirements]
		if HYPEN_E_DOT in requirements:
			requirements.remove(HYPEN_E_DOT)
	return requirements

setup(name="RegressionProject",  #name is user defined pakage name
    version="0.0.1",  #version is user defined version
    author="Seemanshu Shukla",
    author_email="seemanshu.shukla11@gmail.com",
    packages=find_packages(), #this will automatically find all the packages within project(built by placing __init__.py in the respective folders.) and place in packages variable.
    install_requires=["pandas","numpy","flask"] #here we need to mention all the pythonc install needed for this package. We have data injection, data preprocessing etc which will need pandas, numpy etc.
    )