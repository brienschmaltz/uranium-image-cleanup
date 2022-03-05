from setuptools import setup, find_packages


setup(name='uranium-image-cleanup',
      version='0.8.0a1',
      description='Remove labels and text from grayscale uranium photos',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
      ],
      keywords='image processing filtering ',
      package_dir={'': 'src'},
      project_urls={
    'Source': 'https://github.com/brienschmaltz/uranium-image-cleanup'
      },
      author='we need a team-name :D',
      #author_email='schmaltz.6@wright.edu',
      license='MIT',
       install_requires=[
          'tqdm',
          'opencv-python',
          'numpy',
          'pillow'
      ],
      packages=find_packages(where='src'),
      #packages=find_packages(include=['uranium-image-cleanup', 'uranium-image-cleanup.*']),
      #py_modules=["remove_label"],
      python_requires='>=3.6, <4',
      # For example, the following would provide a command called `run` which
      # executes the function `main` from this package when invoked:
      # no idea if this is going to work?
      entry_points={  # Optional
        'console_scripts': [
            'run=uranium_image_cleanup:main',
        ],
      },
      #Potentially add github links
      #Finish read me file
      )