from setuptools import setup, find_packages

setup(
    name="fast-slides",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "jinja2",
        "markdown",
        "pyquery",
        "pygments",
        "lxml",
        "pyyaml",
        "click",
        "watchdog",
    ],
    entry_points={
        "console_scripts": [
            "fast-slides=fast_slides.cli:cli",
        ],
    },
)
