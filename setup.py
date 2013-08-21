import os.path
from setuptools import setup, find_packages
from subprocess import check_call
from setuptools.command.install import install as _install

def init_submodules():
    check_call(['git', 'submodule', 'init'])
    check_call(['git', 'submodule', 'update'])

def build_ckeditor():
    check_call(['src/ckeditor/static/ckeditor/ckeditor/dev/builder/build.sh'])

def get_source_files():
    for dirname, _, files in os.walk('src/ckeditor/static/ckeditor/ckeditor/_source'):
        for filename in files:
            yield os.path.join('/'.join(dirname.split('/')[1:]), filename)

class install(_install):
    def run(self):
        _install.run(self)
        init_submodules()
        build_ckeditor()
        
setup(
    name='django-ckeditor',
    version='4.0.2',
    description='Django admin CKEditor integration.',
    long_description=open('README.rst', 'r').read(),
    author='Shaun Sephton',
    author_email='connect@shaunsephton.com',
    url='http://github.com/shaunsephton/django-ckeditor',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'Pillow',
    ],
    include_package_data=True,
    exclude_package_data={
        'ckeditor': list(get_source_files()),
    },
    test_suite="setuptest.setuptest.SetupTestSuite",
    tests_require=[
        'django-setuptest>=0.1.1',
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
    cmdclass={"install": install},
)
