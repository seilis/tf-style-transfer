from setuptools import setup

with open("README.md") as readme:
    long_description = readme.read()


setup(
    name = "tf-style-transfer",
    packages=["tfstyletransfer"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "tf-style-transfer = tfstyletransfer.entry_points:main"
        ]
    },
)
