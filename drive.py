from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_drive_service():
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    SERVICE_ACCOUNT_FILE = 'gen-lang-client-0122174196-2656196bc430.json'  # Update with the correct path
    
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    service = build('drive', 'v3', credentials=credentials)
    return service

def list_video_files(folder_id):
    service = get_drive_service()
    query = f"'{folder_id}' in parents and mimeType contains 'video/'"
    files = []
    page_token = None

    while True:
        results = service.files().list(
            q=query,
            spaces='drive',
            fields="nextPageToken, files(id, name, mimeType)",
            pageToken=page_token,
            includeItemsFromAllDrives=True,
            supportsAllDrives=True
        ).execute()
        items = results.get('files', [])
        files.extend(items)
        page_token = results.get('nextPageToken')
        if not page_token:
            break

    return files
