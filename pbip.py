import urllib
a=urllib.urlopen("http://ipecho.net/plain")
ip=a.read()
print "(By 4rSh_d0rk)your public ip address is: ",ip
