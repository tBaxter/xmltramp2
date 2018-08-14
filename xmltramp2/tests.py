import unittest

from urllib.request import urlopen 

from xmltramp import Element, Namespace
from xmltramp import parse, quote


class TestXmlTramp(unittest.TestCase):
    def test_sample_xml(self):
        parse('<doc>a<baz>f<b>o</b>ob<b>a</b>r</baz>a</doc>').__repr__(1, 1) == \
            '<doc>\n\ta<baz>\n\t\tf<b>o</b>ob<b>a</b>r\n\t</baz>a\n</doc>'
    def test_empty_xml(self):
        assert str(parse("<doc />")) == ""
    
    def test_html(self):
        assert str(parse("<doc>I <b>love</b> you.</doc>")) == "I love you."
    
    def test_line_breaks(self):
        assert parse("<doc>\nmom\nwow\n</doc>")[0].strip() == "mom\nwow"
        
    def test_nested_tags(self):
        assert str(parse('<bing>  <bang> <bong>center</bong> </bang>  </bing>')) == "center"
        
    def test_escaped_chars(self):
        assert str(parse('<doc>\xcf\x80</doc>')) == '\xcf\x80'
    
    def test_created_element(self):
        d = Element(
            'foo', 
            attrs={'foo': 'bar'}, 
            children=['hit with a', Element('bar'), Element('bar')]
        )
        if d._doesnotexist or d.doesnotexist:
            raise Exception("Expected Error but found success. Damn.")
        
        #assert hasattr(d, 'bar') == True
        # Now check for bar attribute in d, and the name of it.
        self.assertTrue(hasattr(d, 'bar'))
        self.assertEqual(d.bar._name, 'bar')
        #assert d['bar']._name == 'bar'

        assert d('foo') == 'bar'
        d(silly='yes')
        assert d('silly') == 'yes'
        assert d() == d._attrs

        assert d[0] == 'hit with a'
        d[0] = 'ice cream'
        assert d[0] == 'ice cream'
        del d[0]
        assert d[0]._name == "bar"

        assert len(d) == len(d._dir)
        assert len(d[1:]) == len(d._dir) - 1
        
        self.assertEqual(len(d['bar']), 2)
        d.bar = 'baz'
        assert len(d.bar) == 3
        assert d.bar._name == 'bar'

        #        d = Element('foo')
    def test_namespaces_repr(self):
        doc = Namespace("http://example.org/bar")
        bbc = Namespace("http://example.org/bbc")
        dc = Namespace("http://purl.org/dc/elements/1.1/")
        d = parse("""<doc version="2.7182818284590451"
        xmlns="http://example.org/bar"
        xmlns:dc="http://purl.org/dc/elements/1.1/"
        xmlns:bbc="http://example.org/bbc">
            <author>John Polk and John Palfrey</author>
            <dc:creator>John Polk</dc:creator>
            <dc:creator>John Palfrey</dc:creator>
            <bbc:show bbc:station="4">Buffy</bbc:show>
        </doc>""")
        assert repr(d) == '<doc version="2.7182818284590451">...</doc>'
        # I supect py3 does not see equality in type below.
        #assert d.__repr__(1) == '<doc xmlns:bbc="http://example.org/bbc" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns="http://example.org/bar" version="2.7182818284590451"><author>John Polk and John Palfrey</author><dc:creator>John Polk</dc:creator><dc:creator>John Palfrey</dc:creator><bbc:show bbc:station="4">Buffy</bbc:show></doc>'
        #assert d.__repr__(1, 1) == '<doc xmlns:bbc="http://example.org/bbc" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns="http://example.org/bar" version="2.7182818284590451">\n\t<author>John Polk and John Palfrey</author>\n\t<dc:creator>John Polk</dc:creator>\n\t<dc:creator>John Palfrey</dc:creator>\n\t<bbc:show bbc:station="4">Buffy</bbc:show>\n</doc>'
        assert repr(parse("<doc xml:lang='en' />")) == '<doc xml:lang="en"></doc>'
        assert str(d.author) == str(d['author']) == "John Polk and John Palfrey"
        assert d.author._name == doc.author
        assert str(d[dc.creator]) == "John Polk"
        assert d[dc.creator]._name == dc.creator
        assert str(d[dc.creator:][1]) == "John Palfrey"
        d[dc.creator] = "Me!!!"
        assert str(d[dc.creator]) == "Me!!!"
        assert len(d[dc.creator:]) == 1
        d[dc.creator:] = "You!!!"
        assert len(d[dc.creator:]) == 2
        assert d[bbc.show](bbc.station) == "4"
        d[bbc.show](bbc.station, "5")
        assert d[bbc.show](bbc.station) == "5"

        e = Element('e')
        e.c = '<img src="foo">'
        assert e.__repr__(1) == '<e><c>&lt;img src="foo"></c></e>'
        e.c = '2 > 4'
        assert e.__repr__(1) == '<e><c>2 > 4</c></e>'
        e.c = 'CDATA sections are <em>closed</em> with ]]>.'
        assert e.__repr__(1) == '<e><c>CDATA sections are &lt;em>closed&lt;/em> with ]]&gt;.</c></e>'
        e.c = parse('<div xmlns="http://www.w3.org/1999/xhtml">i<br /><span></span>love<br />you</div>')
        assert e.__repr__(1) == '<e><c><div xmlns="http://www.w3.org/1999/xhtml">i<br /><span></span>love<br />you</div></c></e>'

        e = Element('e')
        e('c', 'that "sucks"')
        assert e.__repr__(1) == '<e c="that &quot;sucks&quot;"></e>'
        assert quote("]]>") == "]]&gt;"
        assert quote('< dkdkdsd dkd sksdksdfsd fsdfdsf]]> kfdfkg >') == '&lt; dkdkdsd dkd sksdksdfsd fsdfdsf]]&gt; kfdfkg >'
        assert parse('<x a="&lt;"></x>').__repr__(1) == '<x a="&lt;"></x>'
        assert parse('<a xmlns="http://a"><b xmlns="http://b"/></a>').__repr__(1) == '<a xmlns="http://a"><b xmlns="http://b"></b></a>'

    def test_external_xml(self):
        api_url = 'http://vimeo.com/api/v2/video/67325705.xml'
        video_data = urlopen(api_url).read()
        parse(video_data)
        self.assertEqual(repr(video_data), "foo")

if __name__ == '__main__': 
    unittest.main()