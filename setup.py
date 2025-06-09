from setuptools import setup, find_packages

def read_requirements():
    try:
        with open('requirements.txt', 'r', encoding='utf-8') as f:
            requirements = f.read().splitlines()
        return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    except FileNotFoundError:
        return []

setup(
    name='pydatview',
    version='0.5',
    description='GUI to display tabulated data from files or pandas dataframes',
    url='http://github.com/ebranlard/pyDatView/',
    author='Emmanuel Branlard',
    author_email='lastname@gmail.com',
    license='MIT',
    packages=find_packages(),
    py_modules=['pyDatView'],
    install_requires=read_requirements(),
    zip_safe=False,
    entry_points={
        'gui_scripts': [
            'pydatview = pyDatView:main',
        ],
    }
)
