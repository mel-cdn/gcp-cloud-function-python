# GCP Cloud Function | Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Little project to explore deploying a Python Cloud Function to Google Cloud Project.

Expose the Cloud Function through a public endpoint that will be accessible via HTTPS.

## Requirements

1. [Google Cloud Project](https://cloud.google.com/) account
2. Install [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
3. Install [Python](https://www.python.org/)


## Setup the project

```bash
# Clone project
$ git clone https://github.com/mel-cdn/gcp-cloud-function-python.git
$ cd gcp-cloud-function-python
```
## Authenticate Google Cloud CLI
```bash
# Follow instructions to login your GCP account
$ gcloud init
```

## Deploy to Google Cloud Project
```bash
# Deploy using gcloud cli
$ gcloud functions deploy cfn-demo \
  --allow-unauthenticated \
  --entry-point handler \
  --region asia-southeast1 \
  --memory 256Mi \
  --runtime python312 \
  --timeout 90 \
  --min-instances 0 \
  --max-instances 1 \
  --trigger-http

# Review deployment logs. 
# You can also view Cloud Functions here:
# https://console.cloud.google.com/functions

# Test deployment
$ curl https://asia-southeast1-[YOUR-GCP-PROJECT].cloudfunctions.net/cfn-demo
Hello World!
```



## Local run
This step is optional if you want to run the Cloud Function locally for development.

```bash
# Setup Python environment
$ pyenv install 3.12.3
$ pyenv local 3.12.3
$ python -m venv venv

# Activate virtual environment
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Run local server
$ functions-framework --target handler --debug
```
