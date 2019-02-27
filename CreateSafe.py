import SafePermissions
import requests
from getpass import getpass

PVWABaseURL = "pvwabaseURL"

LogonUrl = 'https://%s/PasswordVault/WebServices/auth/Cyberark/CyberArkAuthenticationService.svc/Logon' % PVWABaseURL
SafeCreationUrl = 'https://%s/PasswordVault/WebServices/PIMServices.svc/Safes' % PVWABaseURL
AddSafeMemberUrl = 'https://%s/PasswordVault/WebServices/PIMServices.svc/Safes/Members' % PVWABaseURL
Logoffurl = 'https://%s/PasswordVault/WebServices/auth/Cyberark/CyberArkAuthenticationService.svc/Logoff' % PVWABaseURL

PayLoad = {}

#STEP:1     AUTHENTICATE TO VAULT TO RECEIVE TOKEN.

userid = input("\nEnter Vault UserName: ")
passwd = getpass(prompt=('Enter the Vault user "%s" Password: ' % userid))

AuthPayload = ("{\r\n  \"username\":\"%s\",\r\n  \"password\":\"%s\",\r\n  \"useRadiusAuthentication\":\"false\",\r\n  \"connectionNumber\":\"1\"\r\n}" % (userid, passwd))
AuthHeaders = {'Content-Type': 'application/json'}
AuthResponse = requests.request('POST', LogonUrl, headers=AuthHeaders, data=AuthPayload, allow_redirects=False, verify=True)

AuthToken = AuthResponse.text[24:204]
Tokenheaders = {'Authorization': "%s" % AuthToken, 'Content-Type': 'application/json'}

#STEP:2     SAFE CREATION FROM THE TOKEN RECEIVED, WITH DATA FROM INPUT FILE.

with open("SafeList_SI.txt") as SafeList:
    for line in SafeList:
        line = line.strip().split(',')
        SafePayload = ("{\n  \"safe\":\n  {\n    \"SafeName\":\"%s\",\n    \"Description\":\"Personal_User_Safe\",\n    \"OLACEnabled\":false,\n    \"ManagingCPM\":\"PasswordManager\",\n    \"NumberofVersionsRetention\":5,\n    \"NumberofDaysRetention\":7\n  }\n}" % line[0])

        SafeCreationresponse = requests.request('POST', SafeCreationUrl, headers=Tokenheaders, data=SafePayload, allow_redirects=False, verify=True)
        print("\nSafe '%s' Creation : HTTP" % line[0], SafeCreationresponse)

#STEP:3     ADD THE SAFE MEMBERS TO THE SAFES CREATED.

        VaultAdminResponse = requests.request('POST', (AddSafeMemberUrl[:-7]+line[0]+AddSafeMemberUrl[-8:]), headers=Tokenheaders, data=SafePermissions.SafeMember("Vault Admins"), allow_redirects=False, verify=True)
        print("Adding Vault Admin on safe '%s' : HTTP" % line[0], VaultAdminResponse)

        AdministratorResponse = requests.request('POST', (AddSafeMemberUrl[:-7]+line[0]+AddSafeMemberUrl[-8:]), headers=Tokenheaders, data=SafePermissions.SafeMember("Administrator"), allow_redirects=False, verify=True)
        print("Adding Administrator  on safe '%s' : HTTP" % line[0], AdministratorResponse)

        A9IdResponse = requests.request('POST', (AddSafeMemberUrl[:-7]+line[0]+AddSafeMemberUrl[-8:]), headers=Tokenheaders, data=SafePermissions.ADMember(line[1]), allow_redirects=False, verify=True)
        print("Adding A9 user '%s' on safe '%s' : HTTP" % (line[1], line[0]), A9IdResponse)

#STEP:4     REMOVE THE SAFE_MEMBERSHIP OF THE VAULT USER, THAT WAS USED TO THE CREATE  THE SAFES.

        SafeMemberDeleteresponse = requests.request('DELETE', (AddSafeMemberUrl[:-7]+line[0]+AddSafeMemberUrl[-8:]+"/"+userid), headers=Tokenheaders, data=PayLoad, allow_redirects=False, verify=True)
        print("Removing user '%s' on safe '%s' : HTTP" % (userid, line[0]), SafeMemberDeleteresponse)

#STEP:5     LOGOFF FROM VAULT.

LogOffresponse = requests.request('POST', Logoffurl, headers=Tokenheaders, data=PayLoad, allow_redirects=False, verify=True)
