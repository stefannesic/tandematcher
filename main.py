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

"""
 Both the parrain and filleul objects with be filled using
 dictionaries that associate their column letters with 
 their actual parameters
 for example B represents the lastName for the filleul sheet
"""

sheetToParam_f = {
    'lastName': 'B',
    'firstName':  'C',
    'age': 'D',
    'sex': 'E',
    'email': 'F',
    'university': 'G',
    'subject': 'H',
    'nationality': 'I',
    'dateArrival': 'N',
    'countryOrigin': 'P',
    'hobbies': 'Q'                
}

sheetToParam_p = {
    'lastName': 'B',
    'firstName':  'C',
    'age': 'D',
    'sex': 'E',
    'email': 'F',
    'university': 'G',
    'nationality': 'H',
    'dateAvailable': 'K',
    'languages': 'I',
    'subject': 'M',
    'hobbies': 'O',
}

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

# given a google sheet id and two column letters, returns the values of the sheet
def sheetToList(sheetid, col1, col2):
    # connect with credentials
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    
    rangeName = col1 + ':' + col2
    result = service.spreadsheets().values().get(
        spreadsheetId=sheetid, range=rangeName).execute()
    values = result.get('values', [])

    return values



def main():

    spreadsheetId = input('Veuillez entrer l\'identifiant de votre document Google Sheets pour les parrains.'
                          'Vous pourriez le trouver apres le /d/ et avant le /edit de l\'url de votre fichier.'
                          'ID GOOGLE SHEET ICI:')

    col1 = input('Premiere colonne a lire des parrains (lettre):')
    col2 = input('Deuxieme colonne a lire des parrains (lettre):')

    
    parrainsVal = sheetToList(spreadsheetId, col1, col2)

    spreadsheetId = input('Veuillez entrer l\'identifiant de votre document Google Sheets pour les filleuls.'
                          'Vous pourriez le trouver apres le /d/ et avant le /edit de l\'url de votre fichier.'
                          'ID GOOGLE SHEET ICI:')

    col1 = input('Premiere colonne a lire des filleuls (lettre):')
    col2 = input('Deuxieme colonne a lire des filleuls (lettre):')

    
    filleulsVal = sheetToList(spreadsheetId, col1, col2)

    
    

    if not parrainsVal:
         add_err_msg(10, "main", "Aucune donnée trouvée pour le fichier de parrains")
    else:
        for row in parrainsVal:
            for col in row:
                print(col)
            print('\n\n\n')

    if not filleulsVal:
         add_err_msg(10, "main", "Aucune donnée trouvée pour le fichier de filleuls")
    else:
        for row in filleulsVal:
            for col in row:
                print(col)
            print('\n\n\n')


if __name__ == '__main__':
    main()


