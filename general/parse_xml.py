import xmltodict, json

import general.parsers

# import xml.etree.ElementTree as ET
# #
# root = ET.parse('returned_soap.xml').getroot()
# print(root)
# rootinside = ET.fromstring
#
# # # soapitems = []
# for item in root.findall('Data/UserActivityBriefResult'):
#     print(item)

obj = general.parsers.parse("""
<employees>
	<employee>
  		<name>Dave</name>
        <role>Sale Assistant</role>
        <age>34</age>
    </employee>
</employees>
""")
# print(json.dumps(obj))
# print(obj["employees"]["employee"]['name'])

with open('sample.xml', 'r') as my_xml_file:
    obj2 = general.parsers.parse(my_xml_file.read())
# print(json.dumps(obj2))

with open('returned_soap3.xml') as my_soap_file:
    obj3 = general.parsers.parse(my_soap_file.read())
# print(json.dumps(obj3))
# print(json.dumps(obj3, indent=4, separators=(',', ': ')))
abc = obj3["soap:Envelope"]["soap:Body"]["GetAllUserCompletedActivityInfoByCompleteDateResponse"][
    "GetAllUserCompletedActivityInfoByCompleteDateResult"]["Data"]["UserActivityBriefResult"]

# print("*********************")
print(json.dumps(abc, indent=4, separators=(',', ': ')))
# users = json.dumps(abc)

print(f"Type of abc = {type(abc)}")
if isinstance(abc, dict):
    print("gelen: collections.OrderedDict")
    print(abc["USER_CODE"])
    print(abc["ACTIVITY_INTEGRATION_CODE"])
elif isinstance(abc, list):
    print("gelen: list")
    for item in abc:
        print(item["USER_CODE"])
        #print(
         #   f'ED_LEARNING_LMS_USER_INFO check for item: {item["USER_CODE"]} - {item["ACTIVITY_INTEGRATION_CODE"]} - {item["ACTIVITY_COMPLETE_STATUS"]}')

# for item in abc:
#     # print(obj3["soap:Envelope"]["soap:Body"]["GetAllUserCompletedActivityInfoByCompleteDateResponse"][
#     #           "GetAllUserCompletedActivityInfoByCompleteDateResult"]["Data"]["UserActivityBriefResult"][0]["USER_CODE"])
#
#     print(item["USER_CODE"])
#     # print(f'ED_LEARNING_LMS_USER_INFO check for item: {item["USER_CODE"]} - {item["ACTIVITY_INTEGRATION_CODE"]} - {item["ACTIVITY_COMPLETE_STATUS"]}')
#     print("************")
