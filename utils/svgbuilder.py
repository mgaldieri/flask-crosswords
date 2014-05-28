__author__ = 'mgaldieri'

import svgwrite, math, pickle
from pprint import pprint


def generate(size, data, empty='-'):
    doc_size = str(size[0]) + 'px', str(size[1]) + 'px'
    svg_xwrd = svgwrite.Drawing(filename='xwords_grid.svg', size=doc_size, debug=True)
    svg_ans = svgwrite.Drawing(filename='xwords_answers.svg', size=doc_size, debug=True)

    g_width = math.floor(float(size[0]) / len(data[0]))
    g_height = math.floor(float(size[1]) / len(data))
    # x_offset = math.floor(float(g_width)/10)
    offset = math.floor(float(g_height) / 10)
    font_size = math.floor(max([g_width, g_height]) * 0.8)
    font_size_min = math.floor(max([g_width, g_height]) * 0.2)

    clues = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col]['value'] != empty:
                # generate empty grid
                svg_xwrd.add(svg_xwrd.rect(insert=(g_width * col, g_height * row),
                                           size=(str(g_width) + 'px', str(g_height) + 'px'),
                                           stroke_width=1,
                                           stroke='black',
                                           fill='white'))
                if 'number' in data[row][col]:
                    svg_xwrd.add(svg_xwrd.text(str(data[row][col]['number']),
                                               insert=((g_width * col) + 1.5 * offset, (g_height * row) + 2 * offset),
                                               font_size=str(font_size_min) + 'px',
                                               font_family='Arial',
                                               text_anchor='middle'))
                    clues.append((data[row][col]['number'], data[row][col]['clue']))
                # generate answer grid
                svg_ans.add(svg_ans.rect(insert=(g_width * col, g_height * row),
                                         size=(str(g_width) + 'px', str(g_height) + 'px'),
                                         stroke_width=1,
                                         stroke='black',
                                         fill='white'))
                svg_ans.add(svg_ans.text(data[row][col]['value'],
                                         insert=((g_width * col) + (g_width / 2),
                                                 (g_height * row) + g_height / 2 + (g_height - font_size + offset)),
                                         font_size=str(font_size) + 'px',
                                         font_family='Arial',
                                         text_anchor='middle'))

    svg_xwrd.save()
    svg_ans.save()
    with open('xwords_clues.txt', 'w') as file:
        for clue in clues:
            file.write('%d - %s\n' % (clue[0], clue[1]))


with open('cross_data.pickle', 'rb') as f:
    data = pickle.load(f)

pprint(data)
# print len(data)
generate((800, 800), data)