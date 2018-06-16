# VMware vSphere Python SDK, pyvmomi
# Simple script to get vCenter server product details

from pyVim.connect import SmartConnect
import ssl

s = ssl.SSLContext(ssl.PROTOCOL_SSLv23)  # For VC 6.5/6.0 s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

si = SmartConnect(host="qa-dur-vc-1.datadomain.com", user="user_name", pwd="password", sslContext=s)
datacenter = si.content.rootFolder.childEntity[0]

print("Product Name:", datacenter)
# print("Product Build:", aboutInfo.build)
# print("Product Unique Id:", aboutInfo.instanceUuid)
# print("Product Version:", aboutInfo.version)
# print("Product Base OS:", aboutInfo.osType)
# print("Product vendor:", aboutInfo.vendor)


x = datacenter.vmFolder.childEntity[4]

vm_datastore =x.childEntity[1].datastore[0].name

print("datastore name is:", vm_datastore)
