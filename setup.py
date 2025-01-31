from setuptools import setup, find_packages

setup(
    name="reki",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    author="Rekimart",
    author_email="support@rekimart.com",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rekimart/rekimart",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
)
