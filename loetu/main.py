import preprocessing
from configparser import ConfigParser


config_parser = ConfigParser()
config_parser.read('config.ini')
feed_file = config_parser.get('Blogger API', 'feed_file')
json_file = config_parser.get('Blogger API', 'json_file')

#Parse feed.
feed = preprocessing.parse_feed(feed_file)

#Clean content.
clean_feed = preprocessing.remove_html_from_content(feed)

#Serialize dictionary of posts to JSON.
preprocessing.serialize_to_json(clean_feed, json_file)