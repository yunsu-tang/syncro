from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# Path to your service account key file
SERVICE_ACCOUNT_FILE = "credentials.json"
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

# Authenticate and create a Drive service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
drive_service = build("drive", "v3", credentials=credentials)

def upload_to_drive(file_path, file_name, folder_id=None):
    """
    Uploads a file to Google Drive.

    :param file_path: Local path of the file to upload.
    :param file_name: Name for the uploaded file on Drive.
    :param folder_id: Optional. The Drive folder ID where the file should be uploaded.
    :return: The file ID of the uploaded file.
    """
    media = MediaFileUpload(file_path, resumable=True)

    file_metadata = {"name": file_name}
    if folder_id:
        file_metadata["parents"] = [folder_id]

    file = drive_service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    
    print(f"File uploaded successfully. File ID: {file.get('id')}")
    return file.get("id")
