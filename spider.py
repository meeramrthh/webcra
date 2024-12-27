from urllib.request import urlopen #connect webpages from py
from link_finder import LinkFinder
from general import *


class Spider:

    # Class Variables (shared among all instances/spiders)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''         #text file to save (harddrive)
    crawled_file = ''
    queue = set()       #waiting list (ram)
    crawled = set()     #crawled list

    def __init__(self):
        