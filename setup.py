from setuptools import setup, find_packages

setup(
    name='algorithms',
    version='0.1',
    packages=find_packages(),
    package_dir={'': 'src'},
    install_requires=[
        # Add your dependencies here
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            # Add your console scripts here
        ],
    },
    author='Samuel Gómez',
    author_email='sierra-034@proton.me',
    description='A collection of algorithms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/algorithms',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
