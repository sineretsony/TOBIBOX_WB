import svgwrite

# text = "MP_106982_5_202_297_8_7				".strip()
# print(text)
#
# temp_stack = []
# temp = ""
#
# for i in text:
#     if i != "_":
#         temp += i
#     elif i == "_":
#         temp_stack.append(temp)
#         temp = ""
#
# temp_stack.append(temp)
# print(temp_stack)
#
# type_pp = temp_stack[0]
#
#
# # Создаем объект Drawing с указанием размеров холста
# dwg = svgwrite.Drawing(filename=text+".svg", size=('300mm', '210mm'))
#
# # Параметры линии
# line_height = '210mm'  # Высота линии
#
# # Линия
# line = dwg.line(start=('0mm', 0), end=('4mm', line_height), stroke='black')
# line2 = dwg.line(start=('15mm', 0), end=('15mm', line_height), stroke='black')
# line3 = dwg.line(start=('150mm', 0), end=('150mm', line_height), stroke='black')
# line4 = dwg.line(start=('158mm', 0), end=('158mm', line_height), stroke='black')
# line5 = dwg.line(start=('178mm', 0), end=('178mm', line_height), stroke='black')
#
#
# # Добавляем линию в рисунок
# dwg.add(line)
# dwg.add(line2)
# dwg.add(line3)
# dwg.add(line4)
# dwg.add(line5)
#
# # Сохраняем рисунок в файл
# dwg.save()

# import svgwrite
#
# # Создаем SVG-рисунок
# dwg = svgwrite.Drawing('example_line.svg', profile='tiny', size=(282.69, 222.3))
#
# # Рисуем линию
# line = dwg.path(d="M0.5,222.3V9C0.5,4.3,4.3,0.5,9,0.5h273.69", stroke='#e52421', fill='none', stroke_miterlimit=10, stroke_width=0.99)
#
# # Добавляем линию на рисунок
# dwg.add(line)
#
# # Сохраняем рисунок в файл
# dwg.saveas('example_line.svg')
#

import svgwrite
import json

# mi = 2.834646
#
# width = 100
# height = 100
# depth = 5
#
# cub = {'info_doc': {'w': width+10, 'h': (height*2)+10+(depth*2), 'color_cut': 'e30613', 'color_crease': '67b438', 'name': 'otkrutka'},
#        'cut': f"M0,0 L0,{120*mi}",
#        'crease': f"M0,0 L0,{120*mi}"}
#
#
# dwg = svgwrite.Drawing(f'{cub["info_doc"]["name"]}.svg', profile='tiny', size=(f"{cub['info_doc']['w']}mm", f"{cub['info_doc']['h']}mm"))
# line1 = dwg.add(dwg.path(d=cub['cut'], stroke=f'#{cub["info_doc"]["color_cut"]}', fill='none', stroke_miterlimit=10, stroke_width=0.99))
#
# dwg.add(line1)
# dwg.saveas(f'{cub["info_doc"]["name"]}.svg')
#
# f = 'creasing'


# тест 2

# import svgwrite
# import json
#
# # static data
# unit_of_millimeters = 2.834646
# safe_field = 2
#
# # input data
# w = 210
# h = 148
# d = 5
#
# # convert data in "unit_of_millimeters"
# width = w * unit_of_millimeters
# height = h * unit_of_millimeters
# depth = d * unit_of_millimeters
# sf = safe_field * unit_of_millimeters
#
# # operational data
# document_write = {'document_info': {'name': 'postcard',
#                                     'cut_color': 'e30613',
#                                     'creasing_color': '26fc00',
#                                     'safe_field': 5},
#
#                   'document_size': {'width': w + safe_field + safe_field, 'height': (h * 2) + safe_field + safe_field + d},
#
#                   'cut_line': f"M{sf},{sf} L{width + sf},{sf}" # 1
#                               f"M{width + sf },{sf} L{width + sf},{width + sf}" # 2
#                               f"M{width + sf}, {height + sf} L{width + sf}, {height + sf + depth}" # 3
#                               f"M{width + sf}, {height + sf + depth} L{width + sf}, {height + height + sf + depth}" # 4
#                               f"M{width + sf}, {height + height + sf + depth} L{sf},{height + height + sf + depth}" # 5
#                               f"M{sf},{height + height + sf + depth} L{sf}, {height + sf + depth}" # 6
#                               f"M{sf}, {height + sf + depth} L{sf}, {height + sf}" # 7
#                               f"M{sf}, {height + sf} L{sf},{sf}", # 8
#
#                   'crease_line': f"M{sf}, {height + sf} L{width + sf}, {height + sf}"
#                                  f"M{sf}, {height + sf + depth} L{width + sf}, {height + sf + depth}"}
#
#
#
# document = svgwrite.Drawing(f'{document_write["document_info"]["name"]}.svg', profile='tiny', size=(f"{document_write['document_size']['width']}mm",
#                                   f"{document_write['document_size']['height']}mm"))
#
# cut_line = document.add(document.path(d=document_write['cut_line'], stroke=f'#{document_write["document_info"]["cut_color"]}', fill='none', stroke_miterlimit=10, stroke_width=0.99))
# crease_line = document.add(document.path(d=document_write['crease_line'], stroke=f'#{document_write["document_info"]["creasing_color"]}', fill='none', stroke_miterlimit=10, stroke_width=0.99))
# document.saveas(f'{document_write["document_info"]["name"]}.svg')


def create_vector_document(w, h, d, example):
    import svgwrite
    import json

    # static data
    unit_of_millimeters = 2.834646
    safe_field = 2

    # input data and convert in "unit_of_millimeters"
    width = w * unit_of_millimeters
    height = h * unit_of_millimeters
    depth = d * unit_of_millimeters
    sf = safe_field * unit_of_millimeters

    with open(f'{example}.json', 'r') as json_file:
        doc_write = json.load(json_file)

    document = svgwrite.Drawing(
        f'{doc_write["document_info"]["name"]}.svg', profile='tiny',
        size=(f"{doc_write['document_size']['width']}mm",
              f"{doc_write['document_size']['height']}mm"))

    cut_line = document.add(document.path(d=doc_write['cut_line'],
                                          stroke=f'#{doc_write["document_info"]["cut_color"]}',
                                          fill='none', stroke_miterlimit=10,
                                          stroke_width=0.99))
    crease_line = document.add(document.path(d=doc_write['crease_line'],
                                             stroke=f'#{doc_write["document_info"]["creasing_color"]}',
                                             fill='none', stroke_miterlimit=10,
                                             stroke_width=0.99))
    document.saveas(f'{doc_write["document_info"]["name"]}.svg')
