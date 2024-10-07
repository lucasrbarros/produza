from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Função que retorna o link do Google Drive para o usuário
def get_drive_link(username):
    # Autenticação e criação do serviço Google Drive
    creds = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/drive.readonly'])
    service = build('drive', 'v3', credentials=creds)

    # Aqui você poderia consultar um arquivo ou pasta no Google Drive associado ao usuário
    folder_id = "your_google_drive_folder_id_for_" + username  # Pasta do cliente no Google Drive

    # Gerar o link da pasta
    drive_link = f"https://drive.google.com/drive/folders/{folder_id}"
    return drive_link
