import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybfcontrol",
    version="0.0.1",
    author="bitfly",
    author_email="zhangbitfly@163.com",
    description="some controls for pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhangenter/bf_control",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)