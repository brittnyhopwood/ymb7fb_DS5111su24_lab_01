from setuptools import setup, find_packages

setup(
    name="ymb7fb_DS5111su24_lab_01",  # Your package name
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List any dependencies here
    ],
    entry_points={
        "console_scripts": [
            # Example: 'your-command=your_module:main',
        ],
    },
)
