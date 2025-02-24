from google.cloud import storage

def export_to_cloud(local_path: str, bucket_name: str, destination_blob_name: str) -> str:
    """
    Uploads a file to Google Cloud Storage and returns the public URL.

    :param local_path: Path to the local file.
    :param bucket_name: Name of the GCS bucket.
    :param destination_blob_name: Target path in the GCS bucket.
    :return: Public URL of the uploaded file.
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(local_path)

    # Make the file publicly accessible (optional)
    blob.make_public()

    return blob.public_url  # Returns the file's URL

# Example usage:
# file_url = export_to_cloud("path/to/local/file.mp3", "your-bucket-name", "uploads/podcast.mp3")
# print(file_url)

from google.cloud import storage
from datetime import timedelta

def upload_and_generate_signed_url(local_file_path: str, bucket_name: str, destination_blob_name: str):
    """
    Uploads a file to Google Cloud Storage and generates a signed URL for it valid for 24 hours.

    :param local_file_path: Path to the local file to be uploaded.
    :param bucket_name: Name of the Google Cloud Storage bucket.
    :param destination_blob_name: Target blob name in the bucket.
    :return: The signed URL.
    """
    # Initialize a Cloud Storage client
    storage_client = storage.Client()

    # Get the bucket and create the blob reference
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Upload the file to the blob
    blob.upload_from_filename(local_file_path)
    print(f"File {local_file_path} uploaded to {destination_blob_name}.")

    # Generate the signed URL (valid for 24 hours)
    signed_url = blob.generate_signed_url(
        expiration=timedelta(hours=24),  # URL will be valid for 24 hours
        method='GET'  # 'GET' is for read access
    )

    print(f"Signed URL for {destination_blob_name}: {signed_url}")
    return signed_url

# # Example usage:
# local_file_path = 'path/to/local/file.mp3'
# bucket_name = 'syncro_pods'  # Your bucket name
# destination_blob_name = 'uploads/file.mp3'  # The desired object path in GCS

# signed_url = upload_and_generate_signed_url(local_file_path, bucket_name, destination_blob_name)
# print("The file can be accessed at:", signed_url)
