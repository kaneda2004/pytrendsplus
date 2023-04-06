from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="pytrendsplus",
    version="0.1.0",
    description="A Python library to fetch and analyze Google Trends data with additional functionalities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kaneda2004/pytrendsplus",  # Replace with your actual GitHub repository URL
    packages=find_packages(),
    install_requires=[
        "pytrends",
        "matplotlib",
        "pandas",
        "scikit-learn",
        "selenium",
        "numpy",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
