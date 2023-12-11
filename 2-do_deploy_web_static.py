#!/usr/bin/python3
"""
 -Fabric script (based on the file 1-pack_web_static.py) that distributes
  an archive to your web serversusing the function do_deploy:
 -Prototype: def do_deploy(archive_path):
"""

from fabric.api import env, put, run
import os.path
env.hosts = ["100.26.156.173", "54.157.184.250"]


def do_deploy(archive_path):
    """
    Deploy archive to web servers
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(filename, path_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        return True
    except:
        return False
