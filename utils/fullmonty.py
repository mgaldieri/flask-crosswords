__author__ = 'mgaldieri'
import greader, crosswordsgen, svgbuilder, pickle
from Crypto.Cipher import AES
from pprint import pprint

minigrid = {}
mediumgrid = {}
largegrid = {}

cypher = AES.new('', AES.MODE_CBC, 'This is an IV456')
with open('cypy', 'rb') as f:
    pwd = pickle.load(f)
dec_pwd = cypher.decrypt(pwd)

url = 'https://docs.google.com/spreadsheets/d/16TrnvphEN64ETajNEjlprTKwh6h2vo_mAVqsVwtpduU/edit#gid=0'
creds = {'user': 'mgaldieri', 'pass': dec_pwd}

wordlist = greader.read_spread(url, creds)
xdata = crosswordsgen.generate(wordlist=wordlist)
svgbuilder.generate(xdata)