from setuptools import setup
from sigopt.version import VERSION

# keep this in sync with requirements.txt
install_requires=['requests>=2.5.1','simplejson>=3.5.2','six>=1.9.0']

setup(
  name='sigopt',
  version=VERSION,
  description='SigOpt Python API Client',
  author='SigOpt',
  author_email='support@sigopt.com',
  url='https://sigopt.com/',
  packages=['sigopt'],
  install_requires=install_requires,
  classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ]
)
