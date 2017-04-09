'''Conversion functions'''

import requests

def zpl2_convert(zpl, output_type='png', resolution=8, width=4, height=6, index=None):
    '''
    Use Labelary api to convert zpl files to pdf or png files.
    zpl: The ZPL code to render.
    output_type: file type to convert to
    resolution: The desired print density, in dots per millimeter. Valid values are 6, 8, 12,
       and 24.
    width: The label width, in inches. Any numeric value may be used.
    height: The label height, in inches. Any numeric value may be used.
    index: The label index (base 0). Optional for pdf. If not specified return all labels in pdf
    '''

    url = 'http://api.labelary.com/v1/printers/{resolution}/labels/{width}x{height}/'
    if output_type == 'png' or index is not None:
        url += '{index}/'

    url = url.format(resolution=str(resolution) + 'dpmm', width=width, height=height, index=index or 0)

    headers = {
        'Accept': {'pdf': 'application/pdf', 'png': 'image/png'}[output_type.lower()],
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    resp = requests.post(url, data=zpl, headers=headers)
    if resp.status_code == 200 and (output_type == 'pdf' or index is not None):
        return [resp.content]
    elif resp.status_code == 200:
        count = int(resp.headers['x-total-count'])
        labels = [resp.content]
        for i in range(1, count):
            labels += zpl2_convert(zpl, output_type, resolution, width, height, i)
        return labels
    else:
        return []

def zpl2_to_pdf(zpl, index=None):
    '''convert zpl labels to 4x6 pdf with 8dpmm'''
    return zpl2_convert(zpl, 'pdf', index=index)

def zpl2_to_png(zpl, index=None):
    '''convert zpl labels to 4x6 png's with 8dpmm'''
    return zpl2_convert(zpl, index=index)
