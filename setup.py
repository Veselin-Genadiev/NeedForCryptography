from distutils.core import setup


setup_info = {'name': 'NeedForCryptography',
              'version': '1.05',
              'description': 'Python cryptographic tools and ciphers',
              'author': 'Veselin Genadiev',
              'author_email': 'genadiev.veselin@gmail.com',
              'url': 'https://github.com/Veselin-Genadiev/NeedForCryptography',
              'packages': ['crypto', 'crypto.tools', 'crypto.symmetric',
                           'crypto.asymmetric'],
              'classifiers': [
                  'Development Status :: 4 - Beta',
                  'Environment :: Console',
                  'Environment :: Web Environment',
                  'Intended Audience :: End Users/Desktop',
                  'Intended Audience :: Developers',
                  'Intended Audience :: System Administrators',
                  'License :: OSI Approved ::'
                  ' Python Software Foundation License',
                  'Operating System :: MacOS :: MacOS X',
                  'Operating System :: POSIX',
                  'Programming Language :: Python',
                  'Topic :: Communications :: Email',
                  'Topic :: Office/Business',
                  'Topic :: Software Development :: Bug Tracking',
              ],
              }

setup(**setup_info)
