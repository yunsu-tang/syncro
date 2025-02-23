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
