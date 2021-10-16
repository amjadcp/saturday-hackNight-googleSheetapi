# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from pprint import pprint

# scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

# creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

# client = gspread.authorize(creds)

# sheet = client.open("Saturday HackNight Sheet").sheet1  # Open the spreadhseet

# data = sheet.get_all_records()  # Get a list of all records

# numRows = sheet.row_count  # Get the number of rows in the sheet
# pprint(data)
import requests
import json
api = 'https://script.google.com/macros/s/AKfycbzDO751w195jyuqifBm3lUuAMgcD-0A72fBEF5y_zQMB-u-yIf0twn6WSi4jKCwOfOppg/exec'

print(requests.get(api).json())

print(requests.get(api).json())
