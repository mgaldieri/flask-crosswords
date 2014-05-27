__author__ = 'mgaldieri'

import svgwrite, math, pickle, pprint

def generate(size, data, empty='-'):
    doc_size = str(size[0])+'px', str(size[1])+'px'
    svg_xwrd = svgwrite.Drawing(filename='crosswords_grid.svg', size=doc_size, debug=True)
    svg_ans = svgwrite.Drawing(filename='crosswords_clue.svg', size=doc_size, debug=True)

    g_width = math.floor(float(size[0])/len(data[0]))
    g_height = math.floor(float(size[1])/len(data))
    x_offset = math.floor(float(g_width)/10)
    y_offset = math.floor(float(g_height)/10)
    font_size = math.floor(max([g_width, g_height])*0.8)
    font_size_min = math.floor(max([g_width, g_height])*0.2)

    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] != empty:
                # generate empty grid
                svg_xwrd.add(svg_xwrd.rect(insert=(g_width*col, g_height*row),
                                         size=(str(g_width)+'px', str(g_height)+'px'),
                                         stroke_width=1,
                                         stroke='black',
                                         fill='white'))
                # svg_xwrd.add(svg_xwrd.text())

                # generate answer grid
                svg_ans.add(svg_ans.text(data[row][col],
                                         insert=((g_width*col)+(g_width/2),
                                                 (g_height*row)+g_height/2+(g_height-font_size+y_offset)),
                                         font_size=str(font_size)+'px',
                                         font_family='Arial',
                                         text_anchor='middle'))

    # TODO: generate clue file

    svg_xwrd.save()

with open('cross_data.pickle', 'rb') as f:
    data = pickle.load(f)

generate((800, 800), data)