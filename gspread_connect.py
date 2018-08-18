import gspread
from oauth2client.service_account import ServiceAccountCredentials



def save_to_gsheet(data):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('scrapingTraicy-57f3281cf682.json', scope)
    google_client = gspread.authorize(credentials)
    google_client.import_csv('1arQR2I_933DNrL7Lc034Ogu2Q2TOkOwEd61Lv-LdlbA', data)
