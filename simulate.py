from lxml import etree
from io import StringIO, BytesIO
import datetime
import sys
def CreateXML():
    try:
        file = open("simulatorData.xml", "r")
        file.close
    except:
        print("Initializing files")
        file = open("simulatorData.xml", "w")
        file.write("""<?xml version="1.0" encoding="UTF-8"?>
<transactions>
    <buy>
<!--    <stock>
            <name>NIO</name>
            <datetime>2020-03-17 18:04:51</datetime>
            <price>2.10</price>
        </stock>
        <currency>
            <name>USD/CHF</name>
            <datetime>2020-03-17 18:04:51</datetime>
            <price></price>
        </currency>
    -->
    </buy>

    <sell>
<!--    <stock>
            <name>NIO</name>
            <datetime>2020-03-17 18:04:51</datetime>
            <price>2.88</price>
        </stock>
        <currency>
            <name>USD/CHF</name>
            <datetime>2020-03-17 18:04:51</datetime>
            <price>2.88</price>
        </currency>-->
    </sell>
</transactions>""")
        file.close()

    if file:
        return(True)
    else:
        sys.exit("File \"simulateData\" failed to open. Error 1")
        return(False)

def SimulateBuy(stock):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print (now)


SimulateBuy('NIO')

CreateXML()