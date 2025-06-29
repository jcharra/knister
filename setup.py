from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['kivy'],
    'iconfile': 'knister.icns',  # Optional: macOS icon file
    'plist': {
        'CFBundleName': 'Knister',
        'CFBundleDisplayName': 'Knister',
        'CFBundleIdentifier': 'de.charra.knister',
        'CFBundleVersion': '1.0.1',
        'CFBundleShortVersionString': '1.0.1',
        'NSHighResolutionCapable': True
    },
}

setup(
    app=APP,
    name='Knister',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)