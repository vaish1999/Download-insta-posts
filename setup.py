import setuptools
from os import path
this_directory = path.abspath(path.dirname("__file__"))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
  name = 'pyinsta',         
  #packages = ['pyinsta'],   
  version = '0.1',      
  license='GPL 2.0',        
  description = "This package will help you download your favourite celebrity post and also any of your friend's profile picture.",   
  author = 'Vaishakh Nargund',                  
  author_email = 'vaishakh.nargund1999@gmail.com', 
  long_description=long_description,
  long_description_content_type="text/markdown",     
  url = 'https://github.com/vaish1999/Download-insta-posts',  
  download_url = 'https://github.com/vaish1999/Download-insta-posts/archive/v1.0.tar.gz',   
  keywords = ['instagram', 'download', 'profile','picture','post','python'],   
  packages=setuptools.find_packages(),
  install_requires=[
        'beautifulsoup4',
        'Pillow'
    ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',    
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)', 
  ],
  python_requires='>=3.7',
)
