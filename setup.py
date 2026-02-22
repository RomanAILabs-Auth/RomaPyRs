# Copyright (c) 2026 Daniel Harding - RomanAILabs

from setuptools import setup, find_packages

setup(
    name='romapyrs',
    version='1.0.0',
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
    entry_points={
        'console_scripts': [
            'romapyrs = romapyrs.core:main',
        ],
    },
    author='Daniel Harding - RomanAILabs',
    description='RomaPyRs: Transpile Python to Optimized Rust for Exponential Performance',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    include_package_data=True,
)
