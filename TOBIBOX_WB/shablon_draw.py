# тест
def sample(w, h, d, um, sff, m):
    """Width, height, depth, unit of measurement, safety margins and materials"""
    # static data
    unit_of_millimeters = um
    safe_field = sff

    # convert data in "unit_of_millimeters"
    width = w * unit_of_millimeters
    height = h * unit_of_millimeters
    depth = d * unit_of_millimeters
    sf = safe_field * unit_of_millimeters
    # material
    mat = m

    # operational data
    document_write = {'document_info': {'name': 'postcard',
                                        'cut_color': 'e30613', # red
                                        'creasing_color': '26fc00'}, # green

                      'document_size': {'width': w + safe_field + safe_field,
                                        'height': (h * 2) + safe_field + safe_field + d},

                      'cut_line': f"M{sf},{sf}, {sf}, {height} L{width + sf},{sf}",

                      'crease_line': f"M{sf}, {height + sf} L{width + sf}, {height + sf}"}
    return document_write


def create_svg_document(w, h, d, m, sample):
    import svgwrite
    import random
    import string

    random_prefix = ''.join(random.choices(string.ascii_lowercase, k=6))

    # static data
    un_milli = 2.834646
    safe_field = 2

    '''Width, height, depth, unit of measurement, safety margins and material (m)'''
    doc_write = sample(w, h, d, un_milli, safe_field, m)

    document = svgwrite.Drawing(f'{doc_write["document_info"]["name"]}.svg', profile='tiny', size=(f"{doc_write['document_size']['width']}mm", f"{doc_write['document_size']['height']}mm"))

    cut_line = document.add(document.path(d=doc_write['cut_line'], stroke=f'#{doc_write["document_info"]["cut_color"]}', fill='none', stroke_miterlimit=10, stroke_width=0.99))
    crease_line = document.add(document.path(d=doc_write['crease_line'], stroke=f'#{doc_write["document_info"]["creasing_color"]}', fill='none', stroke_miterlimit=10,stroke_width=0.99))
    document.saveas(f'{doc_write["document_info"]["name"]}_{w}x{h}x{d}mm.svg')




if __name__ == "__main__":
    create_svg_document(100, 100, 5, 0, sample)





