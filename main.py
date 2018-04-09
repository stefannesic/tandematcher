"""
The following software has been copied from the following website:

https://developers.google.com/sheets/api/quickstart/python

I have made modifications to some parts of it 
"""
from __future__ import print_function
import httplib2
import os
import create_log
import dbexec

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
                 university, nationality, subject, hobbies, languages):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.sex = sex
        self.email = email
        self.dateAvailable =dateAvailable
        self.university = university
        self.nationality = nationality
        self.subject = subject
        self.hobbies = hobbies
        self.languages = languages

    def __repr__(self):
        return "<Parrain FN: %s | LN: %s | AGE: %s" \
            "\nSEX: %s| EM: %s| DA: %s\nUNI: %s |" \
            "NA: %s | SU: %s| HO: %s\nLA: %s" % (self.firstName, self.lastName, self.age, self.sex,
                                                 self.email, self.dateAvailable, 
                                                 self.university, self. nationality,
                                                 self.subject, self.hobbies,
                                                 self.languages)

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
    def __repr__(self):
        return "<Filleul FN: %s | LN: %s | AGE: %s" \
    "\nSEX: %s| EM: %s| DA: %s\nNA: %s|CO: %s| UNI: %s" \
    "\nSU: %s| HO: %s" % (self.firstName, self.lastName, self.age, self.sex,
                      self.email, self.dateArrival, self.nationality,
                      self.countryOrigin, self.university, self.subject,
                      self.hobbies)

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
"""
 given a character converts to it's order in the alphabet (A => 0) (B=> 1)
 plus it's offset

 example: 
 charToNum('B') A => -1, B => 0, C => 2, etc.

"""

def charToNum(char, offset):
    offsetVal = ord(offset.lower()) # gets ascii value of the offset
    return ord(char.lower()) - offsetVal

# reads values from row of listed parameters
def listToVal(listParam, row, firstcol, type):
    listVal = []
    for param in listParam:
        if (type == "p"):
            listVal.append(row[charToNum(sheetToParam_p[param], firstcol)])
        elif (type == "f"): 
            listVal.append(row[charToNum(sheetToParam_f[param], firstcol)])
        else:
            create_log.add_err_msg(25, "listToVal", "type can only be an 'f' or 'p'")
    return listVal
        

def main():

    # prompts user if he wants to input manually or from a file

    inputType = 'z'

    while (inputType != 'O' and inputType != 'N'):
        inputType = input('Lecture de fichier? (O pour oui, N pour non) :')

    if (inputType == 'O'):
        fname = input('Donnez le nom du fichier: ')

        # opens file containing spreatsheedID
        
        fileWID = open(fname, 'r')
        
        listID  = fileWID.read().splitlines()

        spreadsheetId_p = listID[0]

        col1_p = listID[1]

        col2_p = listID[2]

        spreadsheetId_f = listID[3]

        col1_f = listID[4]

        col2_f = listID[5]
        
    else:  
        spreadsheetId_P = input('Veuillez entrer l\'identifiant de votre document Google Sheets pour les parrains.'
                                'Vous pourriez le trouver apres le /d/ et avant le /edit de l\'url de votre fichier.'
                                'ID GOOGLE SHEET ICI:')

        col1_p = input('Premiere colonne a lire des parrains (lettre):')
        col2_p = input('Deuxieme colonne a lire des parrains (lettre):')


    

        spreadsheetId_f = input('Veuillez entrer l\'identifiant de votre document Google Sheets pour les filleuls.'
                                'Vous pourriez le trouver apres le /d/ et avant le /edit de l\'url de votre fichier.'
                                'ID GOOGLE SHEET ICI:')

        col1_f = input('Premiere colonne a lire des filleuls (lettre):')
        col2_f = input('Deuxieme colonne a lire des filleuls (lettre):')

    parrainsVal = sheetToList(spreadsheetId_p, col1_p, col2_p)
    filleulsVal = sheetToList(spreadsheetId_f, col1_f, col2_f)
    
    if not parrainsVal:
        create_log.add_err_msg(10, "main",
                               "Aucune donnée trouvée pour le fichier de parrains");
    else:
         for row in parrainsVal:
            counter = 0
            if (len(row) < 14):
                create_log.add_err_msg(11, "main", "Parrain de nom %s " \
                                      "n'a pas bien" \
                            " rempli le formulaire" % row[0])
            else:
                listParam = ['firstName', 'lastName', 'age',
                             'sex', 'email', 'dateAvailable',
                             'university', 'nationality',
                             'subject', 'hobbies',
                             'languages']

       


                # reads values of parameters listed from document
                valParam = listToVal(listParam, row, col1_p, "p")
                parrain = Parrain(valParam[0], valParam[1],
                                  valParam[2], valParam[3],
                                  valParam[4], valParam[5],
                                  valParam[6], valParam[7],
                                  valParam[8], valParam[9],
                                  valParam[10])

                print(repr(parrain))
                print('\n\n\n')
            

    
    if not filleulsVal:
         create_log.add_err_msg(10, "main",
                     "Aucune donnée trouvée pour le fichier de filleuls")
    else:
        for row in filleulsVal:
            counter = 0
            if (len(row) < 16):
                create_log.add_err_msg(11, "main", "Filleul de nom %s " \
                                      "n'a pas bien" \
                            " rempli le formulaire" % row[0])
            else:
                listParam = ['firstName', 'lastName', 'age',
                             'sex', 'email',
                             'dateArrival', 'nationality',
                             'countryOrigin',
                             'university',
                             'subject', 'hobbies']
                            # reads values of parameters listed from document
                valParam = listToVal(listParam, row, col1_f, "f")
                filleul = Filleul(valParam[0], valParam[1],
                                  valParam[2],
                                  valParam[3], valParam[4],
                                  valParam[5],
                                  valParam[6], valParam[7],
                                  valParam[8],
                                  valParam[9], valParam[10])

                print(repr(filleul))
                print('\n\n\n')


if __name__ == '__main__':
    main()


