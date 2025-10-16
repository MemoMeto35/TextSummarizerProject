import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "TextSummarizerProject"
AUTHOR_USER_NAME = "MemoMeto35"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "t.a.metwally35@mail.com"

setuptools.setup(
    name=SRC_REPO,  
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarization project python package for NLP App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MemoMeto35/TextSummarizerProject", 
    package_dir={"":"src"},

    packages=setuptools.find_packages(where = "src")
)