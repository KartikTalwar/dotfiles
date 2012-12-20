## Download files from a page matching a file extension

import BeautifulSoup
import mechanize
import urllib2
import urlparse
import os
import sys


class extDownloader:

    def __init__(self, url, ext):
        self.url = url
        self.ext = ext
        self.browser = mechanize.Browser()
        self.browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) \
                                    Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        self.browser.set_handle_robots(False)


    def findLinks(self):
        get = self.browser.open(self.url).read()
        bs4 = BeautifulSoup.BeautifulSoup(get)

        rez = []

        for i in bs4.findAll('a'):
            link = i['href']
            if not link.startswith('http'):
                rez.append(urlparse.urljoin(url, link))
            else:
                rez.append(link)

        return rez


    def getFiles(self):
        rez = []

        for i in self.findLinks():
            if i.endswith(self.ext):
                rez.append(i)

        return rez


    def download(self):
        for i in self.getFiles():
            self.downloadFile(i)


    def downloadFile(self, url):
        fileName = url.split('/')[-1]

        if os.path.exists(fileName):
            print " " * 10 + " - %s (Already Saved)" % fileName.split('/')[-1]
        else:
            print " " * 10 + " - %s" % fileName.split('/')[-1]

            try:
                self.browser.retrieve(url, fileName, self._progressBar)
            except KeyboardInterrupt:
                if os.path.exists(fileName):
                    os.remove(fileName)
                raise
            except Exception, e:
                err = e
                if os.path.exists(fileName):
                    os.remove(fileName)
                if e.errno == 2:
                    err = "Errno 2 (No such file or directory)"
                print " " * 10 + " X %s - %s" % (fileName.split('/')[-1], err)


    def _progressBar(self, blocknum, bs, size):
        if size > 0:
            if size % bs != 0:
                blockCount = size/bs + 1
            else:
                blockCount = size/bs

            fraction = blocknum*1.0/blockCount
            width    = 50

            stars    = '*' * int(width * fraction)
            spaces   = ' ' * (width - len(stars))
            progress = ' ' * 12 + ' [%s%s] (%s%%)' % (stars, spaces, int(fraction * 100))

            if fraction*100 < 100:
                sys.stdout.write(progress)

                if blocknum < blockCount:
                    sys.stdout.write('\r')
                else:
                    sys.stdout.write('\n')
            else:
                sys.stdout.write(' ' * int(width * 1.5) + '\r')
                sys.stdout.flush()



if __name__ == '__main__':

    url   = 'http://physics1.uwaterloo.ca/phys363/'
    ext   = 'pdf' # could be any extension
    start = extDownloader(url, ext)

    start.download()


