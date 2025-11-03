from setuptools import setup, find_packages


HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    return [req.replace("\n", "") for req in requirements if req.strip() != HYPEN_E_DOT]

setup(
    name="mlproject",
    version="0.0.1",
    author="Muhammed Irfan",
    author_email="malakkalirfan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)