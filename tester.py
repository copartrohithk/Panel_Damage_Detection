import subprocess

object_location = '/Users/rokokkula/Documents/Panel_Damage_Detection/data/val'  # replace with your object's local path
destination_bucket_name = ' gs://panel_damage_detection/val'  # replace with your bucket name

# Construct the command as a string
command = f'gcloud storage cp {object_location} gs://{destination_bucket_name}'

# Use subprocess to execute the command
subprocess.run(command, shell=True, check=True)