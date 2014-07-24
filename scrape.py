from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests
from time import sleep # be nice
from os.path import isfile
 
BASE_URL = "http://www.brainyquote.com/quotes/topics/"

#topics =  ["Motivational", "Inspirational", "Positive", "Love", "Life", "Success", "Happiness", "Wisdom", "Smile", "Friendship", "Change", "Work", "Leadership", "Education", "Experience", "Failure", "Fitness", "Funny", "Future", "Good", "Great", "Health", "History", "Hope", "Humor", "Imagination", "Intelligence", "Knowledge", "Learning", "Peace", "Poetry", "Power", "Respect", "Science", "Smile", "Society", "Strength", "Teacher", "Thankful", "Trust"]

#do less topics just for test
topics = ["Motivational", "Inspirational"]
quote = ""
author = ""
line = ""
boxes = []

def get_quotes(soup, topic, file):
	boxes = soup.find_all("div", {"class" : "masonryitem boxy bqQt bqShare"})
	for b in boxes:
		quote = b.find("a", {"title" : "view quote"}) 
		author = b.find("a", {"title" : "view author"}) 
		line = (str(quote.get_text()) + "\t" + str(author.get_text()) + "\t" + topic +"\n")
		f.write( line.encode('utf-8') )

def make_url(topic, num):
	return BASE_URL + "topic_" + topic + str("" if num == 1 else num) + ".html"

def get_page_count(soup):
	pages_box = soup.find("div", {"class" : "pagination bqNPgn pagination-small"})
	pages_links = map(lambda p: p.get_text(), pages_box.find_all("a"))
	return int(pages_links[-2])

if __name__ == '__main__':
	for topic in topics:
		filename = topic + '.txt'
		if not (isfile(filename)):
			f = open(topic + '.txt', 'w')
			page_soup = BeautifulSoup(requests.get( make_url(topic, 1) ).text)
			page_count = get_page_count(page_soup)
			for num in range(1, page_count+1):
				print("Writing page " + str(num) + " of " + topic)
				new_soup = BeautifulSoup(requests.get( make_url(topic, num) ).text)
				get_quotes(new_soup, topic, f)
				sleep(1)
		else:
			print("Already pulled data for " + topic)