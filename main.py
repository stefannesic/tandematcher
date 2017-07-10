"""
The following software has been copied from the following website:

https://developers.google.com/sheets/api/quickstart/python

I have made modifications to some parts of it 
"""
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

# parrain object contains all useful info about a parrain in a variable

class Parrain:
    def __init__(self, firstName, lastName, age, sex, email, dateAvailable,
                 university, subject, hobbies, languages):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.sex = sex
        self.email = email
        self.dateAvailable =dateAvailable
        self.university = university
        self.subjet = subject
        self.hobbies = hobbies
        self.languages = languages

# filleul object contains all useful info about a filleul in a variable

class Filleul:
    def __init__(self, firstName, lastName, age, sex,
                 email, dateArrival, nationality, countryOrigin,
                 university, subject, hobbies):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.sex = sex
        self.email = email
        self.dateArrival = dateArrival
        self.nationality = nationality
        self.countryOrigin = countryOrigin
        self.university = university
        self.subject = subject
        self.hobbies = hobbies

def get_credentials():
    # verification of API key
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    # connect with credentials
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    # read spreadsheet 
    spreadsheetId = input('Veuillez entrer l\'identifiant de votre document Google Sheets de Parrains.'
                          'Vous pourriez le trouver apres le /d/ et avant le /edit de l\'url de votre fichier.'
                          'ID GOOGLE SHEET ICI:')

    # contain reading to desired columns
    col1 = input('Premiere colonne a lire (lettre):')
    col2 = input('Deuxieme colonne a lire (lettre):')
    rangeName = col1 + ':' + col2
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
         add_err_msg(10, "main", "Aucune donnée trouvée");
    else:
        for row in values:
            for col in row:
                print(col)
            print('\n\n\n')


if __name__ == '__main__':
    main()


