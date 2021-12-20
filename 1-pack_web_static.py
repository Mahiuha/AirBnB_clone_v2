#!/usr/bin/python3
""" Compress before sending. """
from fabric.api import *
from datetime import datetime
from os import path


def do_pack():
    """do_pack method generates a .tgz archive."""
    datime = datetime.now().strftime("%Y%m%d%H%M%S")
    pth = "versions/web_static_" + datime + ".tgz"

    try:
        if path.exists("versions") is False:
            local("mkdir versions")
        local("tar -zcvf {} web_static".format(pth))
        return pth
    except:
        return None
