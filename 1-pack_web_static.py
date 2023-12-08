#!/usr/bin/python3
"""
 -Fabric script that generates a .tgz archive from the contents of the
  web_static folder of AirBnB Clone repo, using the function do_pack
 -Prototype: def do_pack():
"""

from fabric.api import local
from time import strftime


def do_pack():
    """
    generates a tar archive of webstatic
    """
    time_stamp = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        tar_file = "versions/web_static_{}.tgz".format(time_stamp)
        local("tar -cvzf {} web_static".format(tar_file))
        return tar_file
    except:
        return None
