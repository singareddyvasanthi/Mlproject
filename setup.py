from setuptools import find_packages, setup


def get_requirements(file_path:str)-> list:
    '''
    This function eill return the list
    '''
    HYPHEN_DOTENV = '-e'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_DOTENV in requirements:
            requirements.remove(HYPHEN_DOTENV)

setup(
    name='mlproject',
    version='0.0.1',
    author='Vasanthi',
    author_email='vasnathi@gamil.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)