# pip install zeep
from zeep import Client, Settings
import zeep

settings = Settings(strict=False, xml_huge_tree=True, raw_response=True)
client = Client('http://www.soapclient.com/xml/soapresponder.wsdl', settings=settings)
print(client.service.Method1('Demo', 'Demo2').content)

