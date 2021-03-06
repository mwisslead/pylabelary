from __future__ import print_function

from unittest import TestCase

import labelary

class TestNumberLabels(TestCase):
    def test_png_4(self):
        test_label = '^XA^PR2^LRY^LH30,30^Fo),0^GB400,300,300^FS^FO20,10^AF^FDZEBRA^FS^FO20,60' \
                     '^B3,,40^FDAAA001^FS^PF50^FO20,160^AF^FDSLEW EXAMPLE^FS^XZ^XA^PH^XZ^XA^PR2,6' \
                     '^F020,10^AF^FDZEBRA^FS^F020,60^B3,,40^FDAAA001^FS^PFO20,160^AF' \
                     '^FDSLEW EXAMPLE^FS^XZ^XA^LH30,30^FO20,10^AD^FDZEBRA^FS^FO20,60^B3^FDAAA001' \
                     '^FS^XZ'
        labels = labelary.zpl2_to_png(test_label)
        self.assertTrue(len(labels) == 4)

    def test_png_1(self):
        test_label = '^XA^PR2^LRY^LH30,30^Fo),0^GB400,300,300^FS^FO20,10^AF^FDZEBRA^FS^FO20,60' \
                     '^B3,,40^FDAAA001^FS^PF50^FO20,160^AF^FDSLEW EXAMPLE^FS^XZ^XA^PH^XZ^XA^PR2,6' \
                     '^F020,10^AF^FDZEBRA^FS^F020,60^B3,,40^FDAAA001^FS^PFO20,160^AF' \
                     '^FDSLEW EXAMPLE^FS^XZ^XA^LH30,30^FO20,10^AD^FDZEBRA^FS^FO20,60^B3^FDAAA001' \
                     '^FS^XZ'
        labels = labelary.zpl2_to_png(test_label, index=1)
        self.assertTrue(len(labels) == 1)

    def test_pdf_4(self):
        test_label = '^XA^PR2^LRY^LH30,30^Fo),0^GB400,300,300^FS^FO20,10^AF^FDZEBRA^FS^FO20,60' \
                     '^B3,,40^FDAAA001^FS^PF50^FO20,160^AF^FDSLEW EXAMPLE^FS^XZ^XA^PH^XZ^XA^PR2,6' \
                     '^F020,10^AF^FDZEBRA^FS^F020,60^B3,,40^FDAAA001^FS^PFO20,160^AF' \
                     '^FDSLEW EXAMPLE^FS^XZ^XA^LH30,30^FO20,10^AD^FDZEBRA^FS^FO20,60^B3^FDAAA001' \
                     '^FS^XZ'
        labels = labelary.zpl2_to_pdf(test_label)
        self.assertTrue(len(labels) == 1)

    def test_pdf_1(self):
        test_label = '^XA^PR2^LRY^LH30,30^Fo),0^GB400,300,300^FS^FO20,10^AF^FDZEBRA^FS^FO20,60' \
                     '^B3,,40^FDAAA001^FS^PF50^FO20,160^AF^FDSLEW EXAMPLE^FS^XZ^XA^PH^XZ^XA^PR2,6' \
                     '^F020,10^AF^FDZEBRA^FS^F020,60^B3,,40^FDAAA001^FS^PFO20,160^AF' \
                     '^FDSLEW EXAMPLE^FS^XZ^XA^LH30,30^FO20,10^AD^FDZEBRA^FS^FO20,60^B3^FDAAA001' \
                     '^FS^XZ'
        labels = labelary.zpl2_to_pdf(test_label, index=1)
        self.assertTrue(len(labels) == 1)
