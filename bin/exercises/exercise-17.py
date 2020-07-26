

# Now that you know the tool works, it’s time to build it for distribution. Build a wheel for the package and use
# it to install the hr tool on your system.
#
# Note: This package doesn’t support Python 2, so it is not a “universal” package.



# Extra metadata file:
#
# MANIFEST.in

    include README.rst
    recursive-include tests *.py

# Using the pipenv shell, this is the command that you would run to build the wheel:

    (h4-YsGEiW1S) $ python setup.py bdist_wheel

# Lastly, here’s how you would install this wheel for the root user to be able to use (run from project directory):

    $ sudo pip3.6 install --upgrade dist/hr-0.1.0-py3-none-any.whl

