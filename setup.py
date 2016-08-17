from setuptools import setup
setup(
    name='django-goflow',
    version='custom',
    description='Fork of a fork of the workflow management for the Django web framework',
    author='Erik Simorre',
    author_email='goflow@alwaysdata.net',
    url='http://goflow.nowhere.com',
    packages=['goflow','goflow.apptools','goflow.runtime','goflow.workflow'],
    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)




