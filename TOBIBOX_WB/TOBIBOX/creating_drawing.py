def create_svg_document(w, h, d, m, sample):
    import svgwrite
    import importlib.util
    import random
    import string

    module_name = sample
    module_path = f'media_files/drawing_templates/{module_name}.py'
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    random_prefix = ''.join(random.choices(string.ascii_lowercase, k=6))

    # static data
    un_milli = 2.834646
    safe_field = 2

    '''Width, height, depth, unit of measurement, safety margins and material (m)'''
    doc_write = module.sample(w, h, d, un_milli, safe_field, m)

    document = svgwrite.Drawing(f'{doc_write["document_info"]["name"]}.svg', profile='tiny', size=(f"{doc_write['document_size']['width']}mm", f"{doc_write['document_size']['height']}mm"))

    cut_line = document.add(document.path(d=doc_write['cut_line'], stroke=f'#{doc_write["document_info"]["cut_color"]}', fill='none', stroke_miterlimit=10, stroke_width=0.99))
    crease_line = document.add(document.path(d=doc_write['crease_line'], stroke=f'#{doc_write["document_info"]["creasing_color"]}', fill='none', stroke_miterlimit=10,stroke_width=0.99))
    document.saveas(f'TOBIBOX/temp_drawing/{doc_write["document_info"]["name"]}_{w}x{h}x{d}mm_{random_prefix}.svg')
    return f'TOBIBOX/temp_drawing/{doc_write["document_info"]["name"]}_{w}x{h}x{d}mm_{random_prefix}.svg'


if __name__ == "__main__":
    create_svg_document(100, 100, 5, 0, 'postcard')





