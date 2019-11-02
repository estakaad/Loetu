import feedparser
import requests
import re
from configparser import ConfigParser
from bs4 import BeautifulSoup

config_parser = ConfigParser()
config_parser.read('config.ini')
api = config_parser.get('Blogger API', 'API_KEY')
blog_id = config_parser.get('Blogger API', 'blog_id')
feed_file = config_parser.get('Blogger API', 'feed_file')


class Post:
    def __init__(self, id, author, title, content, date_published):
        self.id = id
        self.author = author
        self.title = title
        self.content = content
        self.date_published = date_published


#Returns 200 if a post is published.
def check_if_post_is_published(blog_id, post_id, api_key):
    url = 'https://www.googleapis.com/blogger/v3/blogs/' + blog_id + '/posts/' + post_id + '?key=' + api_key
    r = requests.get(url)
    return r.status_code == 200


#Parse Atom feed exported from Blogger to create objects of published posts.
def parse_feed(file):
    feed = feedparser.parse(file)
    feed_entries = feed.entries

    posts = []

    for entry in feed_entries:
        if re.search(r'[eE]sta', entry.author):
            if entry.category != 'http://schemas.google.com/blogger/2008/kind#comment':
                id = re.search(r'\d*$', entry.id).group(0)
                if check_if_post_is_published(blog_id, id, api):
                    content = entry.content[0].get('value', default = '')
                    post = Post(entry.id, entry.author, entry.title, content, entry.published)
                    posts.append(post)
    return posts


#Clean post content of HTML. First remove all quotes, then remove HTML tags.
def remove_html_from_content(posts):
    for post in posts:
        soup = BeautifulSoup(post.content, 'lxml')
        quotes = soup.find_all('blockquote')
        for quote in quotes:
            quote.decompose()
        post.content = soup.text
    return posts


posts = parse_feed(feed_file)

clean_posts = remove_html_from_content(posts)