from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='my',
      description='My Python utilities',
      author='Laszlo Treszkai',
      author_email='laszlo.treszkai@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/treszkai/my',
      version='1.0.0',
      packages=['my'],
      classifiers=[
              "Programming Language :: Python :: 3",
              "License :: OSI Approved :: MIT License",
              "Operating System :: OS Independent",
      ],
      license='MIT',
      )
