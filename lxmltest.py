from lxml import etree
from io import StringIO, BytesIO
import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

parser = etree.XMLParser(remove_blank_text=True, remove_comments=True)

tree = etree.parse("simulatorData.xml",parser)
root = tree.getroot()
buy = root[0]
sell = root[1]

etree.SubElement(buy, "stock")
etree.SubElement(buy[0], "name")
etree.SubElement(buy[0], "datetime")
etree.SubElement(buy[0], "price")
buy[0][0].text = "NIO"
buy[0][1].text = now
buy[0][2].text = "12.67"

etree.SubElement(sell, "stock")
etree.SubElement(sell[0], "name")
etree.SubElement(sell[0], "datetime")
etree.SubElement(sell[0], "price")
sell[0][0].text = "NIO"
sell[0][1].text = now
sell[0][2].text = "12.67"

filestuff = etree.tostring(tree, pretty_print=True, encoding='unicode')

file = open("simulatorData.xml", "w")
file.write(filestuff)