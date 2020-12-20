import sys

version = sys.argv[1]
version_filename = "envutils/version.py"
with open(version_filename, "w") as f:
    f.write("__version__ = '{}'".format(version))

print("Updated to version: {}".format(version))