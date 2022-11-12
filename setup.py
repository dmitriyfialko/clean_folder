from setuptools import setup

setup(name='clean_folder',
      version='1',
      description='Clean folder',
      url='https://github.com/dmitriyfialko/clean_folder.git',
      author='Fialko Dmytro',
      author_email='fialkofskiy@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:start_clean_folder']})

