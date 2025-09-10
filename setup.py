import setuptools

with open("README.md" , "r" , encoding="utf-8") as f:
    load_discreption = f.read()

__versiom__ = "0.0.0"

REPO_NAME = "Text-Sumarizer"
AUTHOR_USE_NAME = "Deepak-Byte"
SRC_REPO = "Text Summarizer"
AUTHOR_EMIAL = "deepakkpasi@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__versiom__,
    author=AUTHOR_USE_NAME,
    author_email=AUTHOR_EMIAL,
    description="A project for end 2 end ml",
    long_description=load_discreption,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USE_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USE_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
