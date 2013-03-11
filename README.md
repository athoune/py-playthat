Play that
=========

Ask your VLC slave to play music on your computer.

Use it
------

This code use all the ugliest libraries included in a vanilla Python 2.6, smelly version chosen by Debian :
optparse, urllib, SimpleHTTPServer.
It' painful to code, but there is zero dependency, you just have to drop one file somewhere on your computer.

Original code was made with node, but only bleeding edge developer loves nodejs.

Launch VLC with its HTTP interface on the target :

    vlc -I http --http-host=0.0.0.0

You have to hack VLC hosts file : _/usr/share/vlc/lua/http/.hosts_
VLC http is just broken on Mac, use a Rasperry Pi, it just works.

    ./playthat.py -h

You need some arguments: your ip, vlc ip, and file path.

Check what happens on VLC, with your favorite web browser, on port 8080.


Licence
-------

3 terms BSD, © Mathieu Lecarme
