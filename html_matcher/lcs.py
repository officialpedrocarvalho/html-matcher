import difflib
from io import StringIO

import lxml.html

from similarity import Similarity
from utils import html_to_json_improved, json_to_array


class LongestCommonSequence(Similarity):

    def get_tags(self, doc):
        tags = list()

        for el in doc.getroot().iter():
            if isinstance(el, lxml.html.HtmlElement):
                tags.append(el.tag)

        return tags

    def similarity(self, page1, page2):
        try:
            document_1 = lxml.html.parse(StringIO(page1))
            document_2 = lxml.html.parse(StringIO(page2))
        except Exception as e:
            return 0

        tags1 = self.get_tags(document_1)
        tags2 = self.get_tags(document_2)
        diff = difflib.SequenceMatcher()
        diff.set_seq1(tags1)
        diff.set_seq2(tags2)

        return diff.ratio()


class LongestCommonSequenceOptimized(LongestCommonSequence):

    def get_tags(self, doc):
        json = html_to_json_improved(doc.find('body'))
        return json_to_array(json, "tag", "children")

    # def get_classes(self, html):
    #     document = lxml.html.parse(StringIO(html))
    #     json = html_to_json_improved(document.find('body'))
    #     return json_to_array(json, "classes", "children")
