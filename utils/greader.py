__author__ = 'mgaldieri'

from Crypto.Cipher import AES
import gspread, base64, pickle


def read_spread(url, creds):
    gc = gspread.login(creds['user'], creds['pass'])
    worksheet = gc.open_by_url(url).sheet1
    terms, clues = worksheet.col_values(1), worksheet.col_values(2)

    return zip(terms, clues)


# cypher = AES.new('', AES.MODE_CBC, 'This is an IV456')
# with open('cypy', 'rb') as f:
#     pwd = pickle.load(f)
# dec_pwd = cypher.decrypt(pwd)

#
# url = 'https://docs.google.com/spreadsheets/d/16TrnvphEN64ETajNEjlprTKwh6h2vo_mAVqsVwtpduU/edit#gid=0'
# creds = {'user': 'mgaldieri', 'pass': dec_pwd}
#print read_spread(url, creds)