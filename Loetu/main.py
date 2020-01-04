import preprocessing
from configparser import ConfigParser
#import analyze
#import visualize


config_parser = ConfigParser()
config_parser.read('config.ini')
#feed_file = config_parser.get('Blogger API', 'feed_file')
json_file = config_parser.get('Blogger API', 'json_file')

#Parse feed.
#feed = preprocessing.parse_feed(feed_file)

#Clean content.
#clean_feed = preprocessing.remove_html_from_content(feed)

#Serialize dictionary of posts to JSON.
#preprocessing.serialize_to_json(clean_feed, json_file)

dict = preprocessing.deserialize_to_dict(json_file)

text = preprocessing.merge_content(dict)

print(text)

#tokenized_text = analyze.tokenize(text)

#subst = ''

#for s in analyze.get_list_of_subst(tokenized_text):
#    subst += s + ' '

#visualize.create_wordcloud(subst, 'cloud_subs.png')

#verbs = ''

#for v in analyze.get_list_of_verbs(tokenized_text):
#    verbs += v + ' '

#visualize.create_wordcloud(verbs, 'cloud_verb.png')

#adjs = ''

#for adj in analyze.get_list_of_adj(tokenized_text):
#    adjs += adj + ' '

#visualize.create_wordcloud(adj, 'cloud_adj.png')