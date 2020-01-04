import matplotlib.pyplot
from wordcloud import WordCloud
import numpy as npy
from PIL import Image


def create_wordcloud(str, file_name):
    mask_array = npy.array(Image.open('cloud.png'))
    cloud = WordCloud(background_color = 'white', max_words = 200, mask = mask_array)
    cloud.generate(str)
    cloud.to_file(file_name)