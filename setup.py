from distutils.core import setup


setup_info = {'name': 'NeedForCryptography',
              'description': 'Python cryptographic tools and ciphers',
              'author': 'Veselin Genadiev',
              'author_email': 'genadiev.veselin@gmail.com',
              'url': 'https://www.facebook.com/genadiev.veselin',
              'packages': ['crypto'],
              'package_dir': {'crypto': 'crypto'},
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
                  'Operating System :: Microsoft :: Windows',
                  'Operating System :: POSIX',
                  'Programming Language :: Python',
                  'Topic :: Communications :: Email',
                  'Topic :: Office/Business',
                  'Topic :: Software Development :: Bug Tracking',
              ],
              }


setup(**setup_info)
