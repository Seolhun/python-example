import xml.etree.ElementTree as ET


class LogParser:
    @staticmethod
    def ids_by_message(xml, message):
        root = ET.fromstring(xml)
        result = []
        for r in root.findall('./entry[@id]'):
            for m in r:
                if m.text == message:
                    result.append(int(r.attrib['id']))
        return result


xml = """<?xml version="1.0" encoding="UTF-8"?>
<log>
    <entry id="1">
        <message>Application started</message>
    </entry>
    <entry id="2">
        <message>Application ended</message>
    </entry>
</log>"""
print(LogParser.ids_by_message(xml, 'Application ended'))
