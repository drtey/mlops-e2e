import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    

__version__ = 0.0

REPO_NAME = "mlops-e2e"
AUTHOR_USERNAME = "drtey"
SRC_REPO="mlopsE2E"


setuptools.setup(
    name=f"{REPO_NAME}-{AUTHOR_USERNAME}",
    version=__version__,
    author=AUTHOR_USERNAME,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)