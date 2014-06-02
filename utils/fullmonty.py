__author__ = 'mgaldieri'
import pickle

from Crypto.Cipher import AES

import greader
import crosswordsgen
import svgbuilder


minigrid = {'dirname': 'xwords_mini',
            'grid_size': 17,
            'svg_size': 400}
mediumgrid = {'dirname': 'xwords_med',
              'grid_size': 25,
              'svg_size': 600}
largegrid = {'dirname': 'xwords_large',
             'grid_size': 0,
             'svg_size': 800}

sizes = [minigrid, mediumgrid, largegrid]

cypher = AES.new('', AES.MODE_CBC, 'This is an IV456')
with open('cypy', 'rb') as f:
    pwd = pickle.load(f)
dec_pwd = cypher.decrypt(pwd)

url = 'https://docs.google.com/spreadsheets/d/16TrnvphEN64ETajNEjlprTKwh6h2vo_mAVqsVwtpduU/edit#gid=0'
creds = {'user': 'mgaldieri', 'pass': dec_pwd}

for size in sizes:
    wordlist = greader.read_spread(url, creds)
    xdata = crosswordsgen.generate(wordlist=wordlist,
                                   width=size['grid_size'],
                                   height=size['grid_size'])
    svgbuilder.generate(xdata, dirname=size['dirname'])
