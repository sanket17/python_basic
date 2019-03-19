# main file that calls module

from ImpPackage import impPackage
from ImpPackage.subPackage import subpackage

impPackage.imp_package_func()
subpackage.sub_package_func()

if __name__ == '__main__':
    print('This module is runned')
else:
    print('This  module is imported')