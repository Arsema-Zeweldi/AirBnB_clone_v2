#!/usr/bin/python3
"""Fabric script that distributes an archive to your webservers"""


from datetime import datetime
from fabric.api import *
import os


env.hosts = ["3.236.83.160", "3.239.10.168"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """distributes an arche to your web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    fullFile = archive_path.split("/")[-1]
    folder = fullFile.split(".")[0]

    if run("rm -rf /data/web_static/releases/{}/".
           format(folder)).failed is True:
        print("Deleting folder with archive(if already exists) failed")
        return False

    if run("mkdir -p /data/web_static/releases/{}/".
           format(folder)).failed is True:
        print("Creating new archive folder failed")
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(fullFile, folder)).failed is True:
        print("Uncompressing archive to failed")
        return False

    if run("rm /tmp/{}".format(fullFile)).failed is True:
        print("Deleting archive from /tmp/ directory dailed")
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".
           format(folder, folder)).failed is True:
        print("Moving content to archive folder before deletion failed")
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(folder)).failed is True:
        print("Deleting web_static folder failed")
        return False

    if run("rm -rf /data/web_static/current").failed is True:
        print("Deleting 'current' folder failed")
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(folder)).failed is True:
        print("Creating new symbolic link to new code version failed")
        return False

    print("New version deployed!")
    return True
