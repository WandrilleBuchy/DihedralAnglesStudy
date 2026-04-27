import boto3, os

s3 = boto3.client("s3",
 endpoint_url="https://minio-simple.lab.groupe-genes.fr",
 aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
 aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
 aws_session_token=os.environ["AWS_SESSION_TOKEN"]
)
# Cle = nom sur S3, Valeur = nom local
dossiers = {
 "DistanceMatrices": "Distance Matrices",
 "HDBSCAN_fits": "HDBSCAN_fits",
 "GeoPCA_fits": "GeoPCA_fits",
 "TSNE_fits": "TSNE_fits",
 "UMAP_fits": "UMAP_fits",
 "Data": "Data",
 "Template": "Template"
}

for s3_dossier, local_dossier in dossiers.items():
    os.makedirs(f"/home/onyxia/work/{local_dossier}", exist_ok=True)
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket="wbuchy-ensai", Prefix=f"DihedralAnglesStudy/{s3_dossier}/"):
        for obj in page.get("Contents", []):
            filename = obj["Key"].split("/")[-1]
            print(f"Downloading {filename}...")
            s3.download_file("wbuchy-ensai", obj["Key"], f"/home/onyxia/work/{local_dossier}/{filename}")

print("Downloading done !")