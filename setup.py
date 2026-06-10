from setuptools import find_packages, setup

from typing import List

HYPEN_DOT_E = "-e ."

def get_requirements(file_path :str)  -> List[str] :

    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace( "\n", "")  for req in requirements]

        if HYPEN_DOT_E in requirements :
            requirements.remove(HYPEN_DOT_E)
            
    return requirements






setup(
name = "mlproject", 
version = "0.0.1", 
author = "Poladas James",
author_email="pjames7469@aol.com", 
packages = find_packages(),
install_requires=["pandas", "numpy", "seaborn"]
)