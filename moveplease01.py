#!/usr/bin/env python3
import shutil
import os


def main():
    # force to work/change to listed directory
    os.chdir('/home/student/mycode/')

    # move file/folder, if destination is a folder, moves to destination
    shutil.move('raynor.obj', 'ceph_storage/')

    # prompt user for a new name for the kerrigan.obj file
    xname = input('What is the new name for kerrigan.obj? ')

    # rename file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main()

