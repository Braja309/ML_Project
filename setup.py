from setuptools import setup,find_packages
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
def get_requirements_list()->List[str]:
    """
    This function is going to return list of requirements 
    mentioed in requirement.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name="Housing_Predictor",
    version="0.0.2",
    author="Braja",
    description="This is Housing Price Predictor model",
    packages=find_packages(),#["housing"]
    install_requires = get_requirements_list()
)

#if __name__=="__main__":
#    print(get_requirements_list())
