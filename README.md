# pylabelary
Python module for interacting with api.labelary.com

## Usage:
    >>> import labelary
    >>>
    >>> test_label = '^XA^PR2^LRY^LH30,30^Fo),0^GB400,300,300^FS^FO20,10^AF^FDZEBRA^FS^FO20,60' \
    ...              '^B3,,40^FDAAA001^FS^PF50^FO20,160^AF^FDSLEW EXAMPLE^FS^XZ^XA^PH^XZ^XA^PR2,6' \
    ...              '^F020,10^AF^FDZEBRA^FS^F020,60^B3,,40^FDAAA001^FS^PFO20,160^AF' \
    ...              '^FDSLEW EXAMPLE^FS^XZ^XA^LH30,30^FO20,10^AD^FDZEBRA^FS^FO20,60^B3^FDAAA001' \
    ...              '^FS^XZ'
    >>>
    >>> png_labels = labelary.zpl2_to_png(test_label)
    >>>
    >>> for i, label in enumerate(png_labels):
    ...     with open('test_label{}.png'.format(i), 'wb') as fid:
    ...         fid.write(label)
    ...
    >>>
