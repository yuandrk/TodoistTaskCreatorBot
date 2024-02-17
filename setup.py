from setuptools import find_packages, setup

setup(
    name="teledoist",
    version="0.0.1",  # Use semantic versioning https://semver.org/
    author="Yuandrk",
    author_email="yurii.andriuk@gmail.com",
    description="Create Todoist tasks through Telegram bot",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yuandrk/teledoist",
    packages=find_packages(where="src"),  # Assuming your code is in src/ folder
    package_dir={"": "src"},  # Tell setuptools packages are under src
    install_requires=[
        "requests>=2.25.1,<3",
        "pyTelegramBotAPI>=3.7.6,<4",
        # Add other dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum version requirement of the package
    entry_points={
        "console_scripts": [
            "your-script-name=your_module:main_function",  # If you want to make your project executable from the command line
        ],
    },
)
