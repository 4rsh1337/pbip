import urllib
a=urllib.urlopen("http://ipecho.net/plain")
ip=a.read()
print "your public ip address is: ",ip