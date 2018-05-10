# -*- coding: utf-8 -*-

from . import parser

class xml:
    def __init__(self, xml):
        self._raw_xml = xml

    def parse(self):
        return parser.parser(self._raw_xml).parse()
