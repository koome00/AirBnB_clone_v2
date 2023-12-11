#!/usr/bin/python3
""""
 -Fabric script (based on the file 1-pack_web_static.py) that distributes an
  archive to your web servers, using the function deploy
 -Prototype:
    def deploy():
    def do_pack():
    def do_deploy(archive_path):
    def do_clean
"""

from fabric.api import local, env, put, run
from time import strftime
import os.path
env.hosts = ["100.26.156.173", "54.157.184.250"]


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


def deploy():
    """
    distributes archives to web servers
    """
    path = do_pack()
    if path:
        deployed = do_deploy(path)
        return deployed
    else:
        return False


def do_clean(number=0):
    """
    deletes out-of-date archives
    """
    if number == 0:
        number = 1
    with cd.local('./versions'):
            local("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
            xargs -d '\n' rm".format(1 + number))
    with cd('/data/web_static/releases/'):
            run("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
            xargs -d '\n' rm".format(1 + number))