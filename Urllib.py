"""import urllib.request
print(urllib.request.urlopen("http://stackoverflow.com/documentation/"))
response = urllib.request.urlopen("http://stackoverflow.com/documentation/")
print(response.code)"""

# Web scraping with python
# Scraping using the scrapy frame work.
import scrapy
class StackOverflowSpider(scrapy.spider):
    name = 'stackeoverflow'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']
    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield {
                'title': response.css('h1 a::text').extract_first(),
                'votes': response.css('.question .vote-count-post::text').extract_first(),
                'body': response.css('.question .post-text').extract_first(),
                'tags': response.css('.question .post-tag::text').extract(),
                'link': response.url,
            }

# Scraping using Selenium WebDriver.
from selenium import webdriver
browser = webdriver.Firefox() # launch Firefox browser
browser.get('http://stackoverflow.com/questions?sort=votes')
title = browser.find_element_by_css_selector('h1').text
questions = browser.find_elements_by_css_selector('.question-summary') # question list
for question in questions: # iterate over questions
    question_title = question.find_element_by_css_selector('.summary h3 a').text
    question_excerpt = question.find_element_by_css_selector('.summary .excerpt').text
    question_vote = question.find_element_by_css_selector('.stats .vote .votes .vote-countpost').text
    print("%s\n%s\n%s votes\n-----------\n" % (question_title, question_excerpt, question_vote))


# HTML PArsing
from bs4 import BeautifulSoup
data = """
<ul>
    <li class="item">item1</li>
    <li class="item">item2</li>
    <li class="item">item3</li>
</ul>
"""
soup = BeautifulSoup(data, "html.parser")

for item in soup.select("li.item"):
    print(item.get_text())


# Manipulating XML
# Opening and reading using an Element Tree.
import xml.etree.ElementTree as ET
tree = ET.parse("myXMLfile.xml")
root = tree.getroot()

# Create and Build XML Documents.
import xml.etree.ElementTree as ET
comment = ET.Comment('My Comment')
p.append(comment)

# Searching an XML file.
import xml.etree.cElementTree as ET
tree = ET.parse('sample.xml')
tree.findall('Books/Book')
tree.find("Books/Book[Title='The Colour of Magic']") # Searching for a book title 'The Colour of Magic'

