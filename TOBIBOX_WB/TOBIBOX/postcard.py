def sample(w, h, d, um, sff):
    """Width, height, depth, unit of measurement, safety margins"""
    # static data
    unit_of_millimeters = um
    safe_field = sff

    # convert data in "unit_of_millimeters"
    width = w * unit_of_millimeters
    height = h * unit_of_millimeters
    depth = d * unit_of_millimeters
    sf = safe_field * unit_of_millimeters

    # operational data
    document_write = {'document_info': {'name': 'postcard',
                                        'cut_color': 'e30613', # red
                                        'creasing_color': '26fc00'}, # green

                      'document_size': {'width': w + safe_field + safe_field,
                                        'height': (h * 2) + safe_field + safe_field + d},

                      'cut_line': f"M{sf},{sf} L{width + sf},{sf}"  # 1
                                  f"M{width + sf},{sf} L{width + sf},{height + sf}"  # 2
                                  f"M{width + sf}, {height + sf} L{width + sf}, {height + sf + depth}"  # 3
                                  f"M{width + sf}, {height + sf + depth} L{width + sf}, {height + height + sf + depth}"  # 4
                                  f"M{width + sf}, {height + height + sf + depth} L{sf},{height + height + sf + depth}"  # 5
                                  f"M{sf},{height + height + sf + depth} L{sf}, {height + sf + depth}"  # 6
                                  f"M{sf}, {height + sf + depth} L{sf}, {height + sf}"  # 7
                                  f"M{sf}, {height + sf} L{sf},{sf}",  # 8

                      'crease_line': f"M{sf}, {height + sf} L{width + sf}, {height + sf}"
                                     f"M{sf}, {height + sf + depth} L{width + sf}, {height + sf + depth}"}
    return document_write