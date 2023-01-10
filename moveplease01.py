#!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/"""

#imports

import shutil
import os

def main():
    os.chdir('/home/student/mycode/') # move into mycode directory
    shutil.move('raynor.obj', 'ceph_storage/') # move raynor.obj to ceph_storage directory
    xname = input('What is the new name for kerrigan.obj? ') # prompt for new file name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # move kerrigan.obj to ceph_storage 
    # directory  w/ new name

main()

