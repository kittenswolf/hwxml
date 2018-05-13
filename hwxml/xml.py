# -*- coding: utf-8 -*-

from . import parser

class xml:
    def __init__(self, xml):
        self._raw_xml = xml
        self._parsed_xml = None

    def parse(self):
        if self._parsed_xml:
            return self._parsed_xml
        else:
            self._parsed_xml = parser.parser(self._raw_xml).parse()
            return self._parsed_xml
