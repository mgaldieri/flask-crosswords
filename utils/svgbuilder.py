__author__ = 'mgaldieri'

import math
import os
from zipfile import ZipFile

import svgwrite


def generate(data, max_size=800, dirname='svg', empty='-'):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    doc_size = str(max_size) + 'px', str(max_size) + 'px'
    svg_xwrd = svgwrite.Drawing(filename=os.path.join(dirname, 'xwords_grid.svg'), size=doc_size, debug=True)
    svg_ans = svgwrite.Drawing(filename=os.path.join(dirname, 'xwords_answers.svg'), size=doc_size, debug=True)

    g_width = math.floor(float(max_size) / len(data[0]))
    g_height = math.floor(float(max_size) / len(data))
    # x_offset = math.floor(float(g_width)/10)
    offset = math.floor(float(g_height) / 10)
    font_size = math.floor(max([g_width, g_height]) * 0.8)
    font_size_min = math.floor(max([g_width, g_height]) * 0.3)

    # create groups
    xwrd_grid_g = svg_xwrd.add(svg_xwrd.g(id='xwrd_grid_g'))
    xwrd_num_b = svg_xwrd.add(svg_xwrd.g(id='xwrd_num_b'))

    ans_grid_g = svg_ans.add(svg_ans.g(id='ans_grid_g'))
    ans_char_g = svg_ans.add(svg_ans.g(id='ans_char_g'))

    clues = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col]['value'] != empty:
                # generate empty grid
                xwrd_grid_g.add(svg_xwrd.rect(insert=(g_width * col, g_height * row),
                                              size=(str(g_width) + 'px', str(g_height) + 'px'),
                                              stroke_width=1,
                                              stroke='black',
                                              fill='rgb(255,255,255)'))
                if 'number' in data[row][col]:
                    xwrd_num_b.add(svg_xwrd.text(str(data[row][col]['number']),
                                                 insert=((g_width * col) + (2*offset),
                                                         (g_height * row) + font_size_min),
                                                 font_size=str(font_size_min) + 'px',
                                                 font_family='Arial',
                                                 text_anchor='middle'))
                    clues.append((data[row][col]['number'], data[row][col]['clue']))
                # generate answer grid
                ans_grid_g.add(svg_ans.rect(insert=(g_width * col, g_height * row),
                                            size=(str(g_width) + 'px', str(g_height) + 'px'),
                                            stroke_width=1,
                                            stroke='black',
                                            fill='white'))
                ans_char_g.add(svg_ans.text(data[row][col]['value'],
                                            insert=((g_width * col) + (g_width / 2),
                                                    (g_height * row) + font_size),
                                            font_size=str(font_size) + 'px',
                                            font_family='Arial',
                                            text_anchor='middle'))

    svg_xwrd.save()
    svg_ans.save()
    with open(os.path.join(dirname, 'xwords_clues.txt'), 'w') as txt_f:
        for clue in sorted(clues, key=lambda x: x[0]):
            txt_f.write('%d - %s\n' % (clue[0], clue[1].encode('utf-8')))

    with ZipFile(dirname + '.zip', 'w') as zf:
        for dir, subdirs, files in os.walk(dirname):
            zf.write(dir)
            for file in files:
                zf.write(os.path.join(dir, file))
                os.remove(os.path.join(dir, file))
            os.removedirs(dir)


            # with open('cross_data.pickle', 'rb') as f:
            # data = pickle.load(f)
            #
            # pprint(data)
            # # print len(data)
            # generate(data)