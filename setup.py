import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.FeeWaiverRequest',
      version='1.0.3',
      description=('Fee Waiver Request'),
      long_description='# docassemble.FeeWaiverRequestMc20\r\n\r\nFee Waiver Request\r\n\r\n## Author\r\n* 11/27/24  simplify e-filing language; make addresses display flush with left 1.0.3; language tweaks\r\n* 9/30/24   update cover sheet method and add new user survey 1.0.2\r\n* 8/26/24   small review screen and text fixes 1.0.1\r\n* 8/23/24   Preparing to go live, advance version to 1.0.0\r\nSept 2023   New, from Suffolk Weaver. Brett Harrison of Maverick & Mitchell LLC\r\n\r\n',
      long_description_content_type='text/markdown',
      author='Brett Harrison of Maverick & Mitchell LLC',
      author_email='harrison.brett.m@gmail.com',
      license='The MIT License',
      url='https://michiganlegalhelp.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['docassemble.AssemblyLine>=3.2.0', 'docassemble.GithubFeedbackForm>=0.4.1.1'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/FeeWaiverRequest/', package='docassemble.FeeWaiverRequest'),
     )

