# Nextflow Template for Google Cloud Platfrorm Deployment

This is a template for deploying a Nextflow pipeline on Google Cloud Platform (GCP). It is based on the [Nextflow GCP deployment tutorial](https://www.nextflow.io/docs/latest/google.html), [Nextflow GCP Life Science deployment](https://cloud.google.com/life-sciences/docs/tutorials/nextflow), and the [Nextflow GCP Batch deployment](https://cloud.google.com/batch/docs/nextflow) tutorials.

The template is designed to be used with either your local computer, or the GCP Batch, or GCP Life Sciences APIs. 

## Local PC

Install Nextflow and Docker.

Just clone the repository and run the pipeline with the following command:

```
nextflow run main.nf -profile docker_local --name_1 name1 --name_2 name2 --outDir output_results --code scripts
```

## GCP

To run the pipeline on GCP, you need to create a GCP project: 


```
gcloud projects create PROJECT_ID
```

Then enable billing:
    
```
cloud beta billing projects describe PROJECT_ID
gcloud beta billing accounts describe BILLING_ACCOUNT
```

Enable the GCP Batch API, and create a GCP Storage bucket. 

```
gcloud services enable batch.googleapis.com compute.googleapis.com logging.googleapis.com storage.googleapis.com lifesciences.googleapis.com
```

```
gcloud storage buckets create gs://BUCKET_NAME
```


Then, you need to create a GCP Service Account with the following roles:

```
gcloud iam service-accounts create SA_NAME \
    --description="DESCRIPTION" \
    --display-name="DISPLAY_NAME"

gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:SA_NAME@PROJECT_ID.iam.gserviceaccount.com" \
    --role="ROLE_NAME"

```

Make credentials for the service account:

```
export SERVICE_ACCOUNT_NAME=<name of your service account>
export SERVICE_ACCOUNT_ADDRESS=${SERVICE_ACCOUNT_NAME}@PROJECT_ID.iam.gserviceaccount.com
export SERVICE_ACCOUNT_KEY=${SERVICE_ACCOUNT_NAME}-private-key.json

gcloud iam service-accounts keys create <path to the output json file> --iam-account=${SERVICE_ACCOUNT_ADDRESS} --key-file-type=json ${SERVICE_ACCOUNT_KEY}
export SERVICE_ACCOUNT_KEY_FILE=${PWD}/${SERVICE_ACCOUNT_KEY}
export GOOGLE_APPLICATION_CREDENTIALS=${PWD}/${SERVICE_ACCOUNT_KEY}
```

Install Nextflow:

```
export NXF_VER=23.04.1
export NXF_MODE=google
curl https://get.nextflow.io | bash
```

Change the profile config based on the values you added (such as bucket name).

Run the pipeline:

```
nextflow run main.nf -profile docker_gcp_batch --name_1 name1 --name_2 name2 --outDir output_results --code scripts
```