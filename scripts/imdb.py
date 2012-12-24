#!/usr/bin/python

from xml.etree import ElementTree
import argparse
import urllib
import sys


def retrieveMovie(title):
    title = urllib.quote(title.encode("utf8"))
    URL = "http://www.omdbapi.com/?r=xml&plot=short&t=%s" % title
    xml = ElementTree.parse(urllib.urlopen(URL))
    for A in xml.iter('root'):
        if (A.get('response') == 'False'):
            print "Movie not found!"
            sys.exit()
    xml = xml.getroot()
    printInfo(xml)
    return xml


def movieSearch(title):
    title = urllib.quote(title.encode("utf8"))
    URL = "http://www.omdbapi.com/?r=xml&s=%s" % title
    xml = ElementTree.parse(urllib.urlopen(URL))
    xml = xml.getroot()
    for B in xml.findall('Movie'):
        apicall = retrieveMovie(B.get('Title'))
        printInfo(apicall)
    return xml


def printInfo(xml):
    for B in xml.findall('movie'):
        print "\n%s (%s) | %s/10\r" % (B.get('title'), B.get('year'), B.get('imdbRating'))
        print "%s (%s)\n" % (B.get('released'), B.get('runtime'))
        print "Actors: %s | Director: %s\r" % (B.get('actors'), B.get('director'))
        print "Summary: %s\r" % (B.get('plot'))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Command-Line Interface for the IMdB')

    parser.add_argument("-t", help="Search by title. Return first result")
    parser.add_argument("-s", help="Search and return results")

    args = parser.parse_args()
    choices = ["None"]
    try:
        choices[0] = sys.argv[1]
        title = sys.argv[2]
    except:
        parser.print_usage()
        sys.exit()

    if choices[0] == "-t":
        retrieveMovie(title)
    else:
        movieSearch(title)
