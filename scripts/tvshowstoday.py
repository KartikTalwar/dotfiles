import time
import urllib
import re


class TVShows:

    def __init__(self, shows, cmd=None):
        self.shows   = shows
        self.options = cmd


    def getShow(self, name):
        url  = "http://gomiso.com/m/" + name.lower() + "?teaser=false"
        get  = urllib.urlopen(url).read()
        tvid = self._cut("<span class=\"data_value\">", '</span>', get)[0]

        return (get, tvid)


    def getLatestSeason(self, html):
        url = re.findall("<a(.*?)href=\"(.*?)\">View All Episodes By Season</a>", html)
        return url[0][1] + "?teaser=false"


    def getEpisodeMeta(self, url):
        rez = []
        get = urllib.urlopen(url).read()

        details = [self._strip(i) for i in self._cut("<p class=\'details'>", '</p>', get)]
        title   = [self._cut('>', '</', i)[0] for i in self._cut("<p class=\'title'>", '</p>', get)]
        summary = [self._strip(i) for i in self._cut("<p class=\'description'>", '</p>', get)]

        for i in range(len(details)):
            res = [details[i], title[i], summary[i]]
            rez.append(res)

        return rez


    def parseEpisodes(self, meta):
        rez = []

        for i in meta:
            x = i[0].split(' - ')
            s = x[0].split(', ')[0].split()[1]
            e = x[0].split(', ')[1].split()[1]
            l = "S%02dE%02d - %s [%s]" % (int(s), int(e), i[1], x[1])
            rez.append(l)

        return rez


    def parseShow(self, show):
        rez = {}
        get = self.getShow(show)

        getShowData  = get[0]
        seasonData   = self.getLatestSeason(getShowData)
        episodeData  = self.getEpisodeMeta(seasonData)
        parseEpisode = self.parseEpisodes(episodeData)
        rez[get[1]]  = parseEpisode

        return rez


    def airsToday(self, show):
        today = time.strftime("%m/%d/%Y")
        multi = []

        for k,v in show.iteritems():        
            for i in v:
                date = i.split("[Aired ")[1].split(']')[0]
                if date == today:
                    multi.append( k + " " + i.split(" [Aired ")[0] )
        
        if len(multi) > 0:
            return multi[::-1]

        return None


    def getShowID(self, show):
        if '-' not in show:
            url = "http://gomiso.com/search?count=5&teaser=false&q=" + show
            get = urllib.urlopen(url).read()
            rez = [self._strip(i) for i in self._cut("gomiso.com/m/", '"', get)]

            return rez[0]

        return show


    def parse(self):
        rez = []

        for i in self.shows:
            try:
                name = self.getShowID(i)
                data = self.parseShow(name)
                show = self.airsToday(data)

                if show is not None:
                    rez += show
            except:
                pass

        return rez


    def _cut(self, start, end, data):
        rez = []
        one = data.split(start)

        for i in range(1, len(one)):
            two = one[i].split(end)
            rez.append(two[0])

        return rez


    def _strip(self, data):
        return re.sub('(\n|\r|\t)', '', data)



if __name__ == '__main__':

    fall   = ['doctor who', 'fringe', 'community', 'revolution--2', 'how i met your mother', 
              'parks and recreation', 'the office', 'dexter', 'big bang theory', 'modern family',
              'elementary']
    winter = [ 'sherlock', 'californication', 'game of thrones', 'house of lies']
    spring = ['white collar', 'breaking bad', 'suits', 'the newsroom', 'eureka', 
              'falling skies', 'futurama', 'falling skies']

    shows = fall + winter + spring
    tv    = TVShows(shows)
    today = tv.parse()

    for i in today:
        print i

