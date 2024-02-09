import setuptools

long_desc = ''
with open("README.md", "r", encoding='utf-8') as f:
    long_desc = f.read()

setuptools.setup(
    name="pyinject",
    version='1.0.0',
    description='Dependency injection package',
    package_dir={"": "pyinject"},
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='Kenneth Ulloa',
    author_email='ulloakenth@gmail.com',
    url='',
    classifiers=[
        "Intended Audience :: Developers",
        "Programing Language :: Python :: 3.11",
        "Topic :: Utilities"
    ],
    python_requires=">=3.10",
    packages=setuptools.find_packages(where="pyinject"),
    include_package_data=True,
    extras_require={
        "dev": ["pytest"]
    }
)