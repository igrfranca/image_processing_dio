from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_dio",
    version="0.0.1",
    author="igor_franca",
    author_email="igrfranca@gmail.com",
    description="Pacote de processamento de imagem",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/igrfranca/image_processing_dio"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)