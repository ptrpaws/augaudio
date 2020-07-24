from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name="augaudio",
    version="1.0.0",
    author="Ellie",
    author_email="e3e@disroot.org",
    description="A simple audio data augmentation package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="ptrpaws",
    project_urls={
        "Bug Tracker": "https://github.com/ptrpaws/augaudio/issues",
        "Source Code": "https://github.com/ptrpaws/augaudio",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
          'numpy >= 1.16.2',
          'librosa >= 0.7.2',
          'numba < 0.50',
          ],
    license="Apache",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
		"Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
		"Topic :: Scientific/Engineering",
    ],
    entry_points={
        "console_scripts": [
            "augaudio=augaudio.cli:main",
        ]
    },
)
