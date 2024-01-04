import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


__version__ = '0.0.0'

REPO_NAME = 'MLOpsKidneyDisease'
AUTHOR_USER_NAME = 'skorobogatovamail'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'skorobogatovamail@gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for cnn classification',
    long_description=long_description,
    long_description_content='text/markdown',
    url='https://github.com/skorobogatovamail/MLOpsKidneyDisease',
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)
