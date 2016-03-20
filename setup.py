# -*- coding: utf-8 -*-

from redirector import __version__
from setuptools import setup, find_packages

setup(name='cappfig',
      version=__version__,
      description="Manage file configurations",
      long_description=open('README.md').read(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
          'Operating System :: POSIX',
      ],
      keywords='',
      author='Pablo Muñoz',
      author_email='pablerass@gmail.com',
      url='https://github.com/pablerass/cappfig',
      license='LGPLv3',
      packages=find_packages(exclude=['test']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[line for line in open('requirements.txt')],
)
