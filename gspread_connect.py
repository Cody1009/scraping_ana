import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


def save_to_gsheet():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('scrapingTraicy-57f3281cf682.json', scope)
    google_client = gspread.authorize(credentials)
    data = pd.read_csv('./output.csv')
    print(data)
    google_client.import_csv('1arQR2I_933DNrL7Lc034Ogu2Q2TOkOwEd61Lv-LdlbA', data)
