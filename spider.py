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

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod 
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        
    