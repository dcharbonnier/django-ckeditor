import os.path
from setuptools import setup, find_packages
from subprocess import check_call
from setuptools.command.install import install as _install
from setuptools.command.develop import develop as _develop

def init_submodules():
    check_call(['git', 'submodule', 'init'])
    check_call(['git', 'submodule', 'update'])

def build_ckeditor():
    check_call(['src/ckeditor/static/ckeditor/ckeditor/dev/builder/build.sh'])

class install(_install):
    def run(self):
        init_submodules()
        build_ckeditor()
        _install.run(self)
        
class develop(_develop):
    def run(self):
        init_submodules()
        build_ckeditor()
        _develop.run(self)
   
setup(
    name='django-ckeditor',
    version='4.2.0.1',
    description='Django admin CKEditor integration.',
    long_description=open('README.rst', 'r').read(),
    author='Shaun Sephton',
    author_email='connect@shaunsephton.com',
    url='http://github.com/shaunsephton/django-ckeditor',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'Pillow',
        'lxml',
    ],
    include_package_data=True,
    test_suite="setuptest.setuptest.SetupTestSuite",
    tests_require=[
        'django-setuptest>=0.1.1',
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
    cmdclass={"install": install, "develop": develop},
)
