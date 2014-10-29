'''
Created on Ago 28, 2014

@author: Aitor Gómez Goiri <aitor.gomez@deusto.es>

To install/reinstall/uninstall the project and its dependencies using pip:
     pip install ./
     pip install ./ --upgrade
     pip uninstall pynist800108
'''
from setuptools import setup, find_packages

setup(name="pynist800108",
      version="0.1",
      description="Python implementation of Nist SP 800-108 KDF in Counter Mode",
      #long_description = "",
      author = "Aitor Gomez-Goiri",
      author_email = "aitor.gomez@deusto.es",
      maintainer = "Aitor Gomez-Goiri",
      maintainer_email = "aitor.gomez@deusto.es",
      url = "https://github.com/gomezgoiri/pyNist800-108",
      #download_url = "https://github.com/gomezgoiri/pyNist800-108/zipball/master",
      #license = "http://www.apache.org/licenses/LICENSE-2.0",
      platforms = ["any"],
      package_dir = {
        '': 'src',
      },
      packages = ["kdf"],
      # packages = find_packages('src'),  # include all packages under src
      # install_requires = ['REQ1', 'REQ2'],
      # entry_points = {}
      keywords = "security lightweight sensor gateway authentication authorization iot things python",
)