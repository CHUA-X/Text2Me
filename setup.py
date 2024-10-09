import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Text2Me",
    version="0.0.1",
    author="CHUA某人",
    author_email="chua-x@outlook.com",
    description="text2me ——通过Twilio发消息给自己手机",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CHUA-X/Text2Me",
    packages=setuptools.find_packages(where='./src'),
    package_dir={"": "src"},
    keyword=['Python', 'python', 'Twilio'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)
