#Imports
import json
from googleapiclient import discovery
from google.oauth2 import service_account
from pprint import pprint

#Open json file
f = open('1passwordUsers.json')
data = json.load(f)
entries = len(data)

#Transform data into format suitable for google sheets
transformedData = [[item['id'], item['name'], item['email'], item['type'], item['state'], item['created_at'], item['updated_at'], item['last_auth_at']] for item in data]



#Write to spreadsheet
credentials = service_account.Credentials.from_service_account_file('googlecreds.json')

service = discovery.build('sheets', 'v4', credentials=credentials)
spreadsheet_id = '1bKA92Tv7d026krFFdlvljbuo0kAnufED2CHLD4i4c3E'  # TODO: Update placeholder value.
range_ = '1Password!A2:H' + str(entries + 1)
body = {
    "range" : range_,
    "values" : transformedData
}
request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption= "USER_ENTERED", body=body)
response = request.execute()
pprint(response)
