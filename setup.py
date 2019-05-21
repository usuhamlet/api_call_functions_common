from distutils.core import setup

setup(
	name='apifunctions',
	version='2019.1',
	description='A common set of functions for calling RESTful/SOAP APIs.',
	author='Robert Holloway',
	packages=['apifunctions'],
	classifiers=[
		'Development Status :: Development',
		'Intended Audience :: Developers',
		'Operation System :: OS Independent',
		'Programming Language :: Python',
	],
	install_requires=[
		'requests',
	]
)