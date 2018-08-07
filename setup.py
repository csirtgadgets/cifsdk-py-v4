import os
from setuptools import setup, find_packages
import versioneer
import sys

if sys.version_info < (3, 4):
    print("\n")
    print("This requires python 3.5 or higher")
    print("\n")
    raise SystemExit

# vagrant doesn't appreciate hard-linking
if os.environ.get('USER') == 'vagrant' or os.path.isdir('/vagrant'):
    del os.link

# https://www.pydanny.com/python-dot-py-tricks.html
if sys.argv[-1] == 'test':
    test_requirements = [
        'pytest',
        'coverage',
        'pytest_cov',
    ]
    try:
        modules = map(__import__, test_requirements)
    except ImportError as e:
        err_msg = e.message.replace("No module named ", "")
        msg = "%s is not installed. Install your test requirements." % err_msg
        raise ImportError(msg)
    r = os.system('py.test test -v --cov=cif --cov-fail-under=35')
    if r == 0:
        sys.exit()
    else:
        raise RuntimeError('tests failed')

setup(
    name="verbose-robot-sdk-py",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="CIFv4 Python SDK",
    long_description="",
    url="https://github.com/csirtgadgets/verbose-robot-sdk-py",
    license='MPL2',
    classifiers=[
               "Topic :: System :: Networking",
               "Programming Language :: Python",
               ],
    keywords=['security'],
    author="Wes Young",
    author_email="wes@csirtgadgets.com",
    packages=find_packages(),
    install_requires=[
        'SQLAlchemy',
        'ujson',
        'msgpack',
        'tornado',
        'csirtg_indicator>=2.0a2,<3.0'
    ],
    scripts=[],
    entry_points={
        'console_scripts': [
            'cif=cifsdk.cli:main',
            'cif-tokens=cifsdk.tokens:main',
            'cif-firehose=cifsdk.client.ws:main'
        ]
    },
)
