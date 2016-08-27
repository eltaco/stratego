print "Helo"
import urllib2

req = urllib2.Request('http://cleanranking1.coolpage.biz/cleanranking/')
response = urllib2.urlopen(req)
the_page = req.read()
