from setuptools import setup

def readme():
    try:
        with open("README.rst") as f:
            return f.read()
    except IOError:
        pass


setup(
    name="swagger2markdown",
    version="0.1.0",
    url="https://github.com/moigagoo/swagger2markdown",
    download_url="https://pypi.org/project/swagger2markdown",
    license="MIT",
    author="Konstantin Molchanov",
    author_email="moigagoo@live.com",
    description="Converter from Swagger to Markdown.",
    long_description=readme(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ],
    py_modules=["swagger2markdown.swagger2markdown"],
    packages=["swagger2markdown"],
    package_dir={"swagger2markdown": "."},
    package_data={"swagger2markdown": ["swagger.md.j2"]},
    platforms="any",
    install_requires=["Jinja2", "requests"],
    entry_points={
        "console_scripts": [
            "swagger2markdown=swagger2markdown.swagger2markdown:main"
        ]
    }
)
