from setuptools import setup, find_packages


__VERSION__ = '0.0.1'

try:
    README = open('README.md').read()
except:
    README = None

try:
    REQUIREMENTS = open('requirements.txt').read()
except:
    REQUIREMENTS = None

setup(
    name='arctic_datiba',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    version=__VERSION__,
    long_description=README,
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    url='https://source.sanoma.com/projects/REUSE/repos/arctic-sanoma/',
    author='Bart Stroeken, Daan Luijten, Tibo Beijen',
    author_email='bart@nu.nl, daniel.luijten@sanoma.com,tibo@nu.nl',
    description="Arctic DaTiBa is a partial data storage interface.",
)
