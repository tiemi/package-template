from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processador_imagem",
    version="0.0.1",
    author="Uiliam bomfim",
    author_email="wf3@outlook.com.br",
    description="pacote de processamento de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UiliamBomfim/package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)