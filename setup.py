from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='uranium-image-cleanup',
      version='0.8',
      description='Remove labels and text from grayscale uranium photos',
      classifiers=[
        'Development Status :: 0.8 Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Image Processing :: Filtering',
      ],
      url='https://github.com/brienschmaltz/uranium-image-cleanup',
      author='we need a team-name :D',
      author_email='schmaltz.6@wright.edu | name.2@wright.edu',
      license='MIT',
      packages=['uranium-image-cleanup'],
       install_requires=[
          'tqdm',
          'opencv-python',
          'numpy',
          'pillow'
      ],
      #Potentially add github links
      #Finish read me file
      zip_safe=False)