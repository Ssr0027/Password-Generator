from setuptools import setup

APP = ['PASS.py']  
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pyperclip'],  
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
