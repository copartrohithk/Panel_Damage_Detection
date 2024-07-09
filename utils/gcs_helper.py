import glob
from google.cloud import storage
import os
GCS_CLIENT = storage.Client()

def upload_local_directory_to_gcs(local_path, bucket, gcs_path):
    assert os.path.isdir(local_path)
    bucket = GCS_CLIENT.get_bucket(bucket)
    for local_file in glob.glob(local_path + '/**'):
        if not os.path.isfile(local_file):
           upload_local_directory_to_gcs(local_file, bucket, gcs_path + "/" + os.path.basename(local_file))
        else:
           remote_path = os.path.join(gcs_path, local_file[1 + len(local_path):])
           blob = bucket.blob(remote_path)
           blob.upload_from_filename(local_file)


upload_local_directory_to_gcs('/Users/rokokkula/Documents/Panel_Damage_Detection/data/Damage_labels/val/labels'
                              ,'panel_damage_detection', 'damage_labels/val/labels')