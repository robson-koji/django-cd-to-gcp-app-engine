
This is just to test a pull from **GCP (Google Cloud Platform)** trigered from a git commit, to auto deploy on a App Engine instance. 

Configure the pipeline on **Google Cloud Build**:

https://console.cloud.google.com/cloud-build/

The main goal was:

* Dev (any one) commits to GitHub
* On the commit message, developers tags a specific dev/test environment on GCP to deploy
* GCP Cloud Build  triggers the event and pulls Git repository
* Deploy to the environment specified on the second step.


This is a very hacky solution, and the bash "parsing" on the Cloud Build side doesn't work as expected.
There are other ways to achive this, using Git tag, which has another purpose.  And it can also be done using GitHub actions
