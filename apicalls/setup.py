from distutils.core import setup

setup(
	name='apicalls',
	version='2019.1',
	description='A common set up functions for calling RESTful APIs.',
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