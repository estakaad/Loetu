import feedparser
import requests
import re
from bs4 import BeautifulSoup
import json
from configparser import ConfigParser


config_parser = ConfigParser()
config_parser.read('config.ini')
api = config_parser.get('Blogger API', 'API_KEY')
blog_id = config_parser.get('Blogger API', 'blog_id')


#Returns 200 if a post is published.
def check_if_post_is_published(blog_id, post_id, api_key):
    url = 'https://www.googleapis.com/blogger/v3/blogs/' + blog_id + '/posts/' + post_id + '?key=' + api_key
    r = requests.get(url)
    return r.status_code == 200


#Parse Atom feed exported from Blogger to create a nested dictionary of posts.
def parse_feed(file):
    feed = feedparser.parse(file)
    feed_entries = feed.entries

    posts = {}

    for entry in feed_entries:
        if re.search(r'[eE]sta', entry.author):
            if entry.category != 'http://schemas.google.com/blogger/2008/kind#comment':
                id = re.search(r'\d*$', entry.id).group(0)
                if check_if_post_is_published(blog_id, id, api):
                    content = entry.content[0].get('value', default = '')
                    posts[id] = {}
                    posts[id]['author'] = 'Esta'
                    posts[id]['title'] = entry.title
                    posts[id]['published'] = entry.published
                    posts[id]['content'] = content
    return posts


#Remove quotes from text. But is it really always necessary? They are quotes, not original content,
#but they are still an integral part of the post content.
def remove_quotes_from_content(posts):
    for id in posts:
        soup = BeautifulSoup(posts[id]['content'], 'lxml')
        quotes = soup.find_all('blockquote')
        for quote in quotes:
            quote.decompose()
    return posts


#Clean post content of HTML tags. Returns a dictionary with clean data.
def remove_html_from_content(posts):
    for id in posts:
        soup = BeautifulSoup(posts[id]['content'], 'lxml')
        posts[id]['content'] = soup.text
    return posts


#Serialize dictionary of posts to JSON.
def serialize_to_json(posts, json_file):
    with open(json_file, 'w', encoding='UTF-8') as outfile:
        json.dump(posts, outfile, ensure_ascii=False)


#Deserialize JSON file to a nested dictionary.
def deserialize_to_dict(json_file):
    with open(json_file, encoding='UTF-8') as input:
        return json.load(input)


#Merge the content of all posts to one string.
def merge_content(dict):
    text = ''
    for i in dict.keys():
        post_content = dict[i].get('content')
        text += post_content
    return text