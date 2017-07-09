# GCPOC
Google Cloud Proof of Concept

This is a rather simple program, designed solely for the purpose of experimenting with specific technologies:
  * Google Cloud
  * Docker
  * microservices

The underlying languages/systems used were:
  * Python 3 (for the microservices) using Flask/Connexion
  * PHP for the web pages
  * MySQL as the database
  * Apache as the web server

The application is largely unimportant - its a very trivial two page app that displays/adds strings from/to the database. No real effort was made to make the application particularly attractive, well designed, secure, etc... it's just intended to be there in order to work with the other technologies.

The overall system is designed as follows:
  * A docker container of a MySQL database, running on a container-optimized compute instance
  * A firewall that allows for port 80 traffic to come in
  * An autoscaling group for the web tier
  * A health check for the web tier
  * An instance group manager to handle the web tier
  * The instance template that describes a web tier server
  * A load balancer for all servers in the web tier
  * A target pool to contain all the web tier servers
  * A docker container containing a microservice to add strings to the database, running on a container-optimized compute instance
  * A docker container containing a microservice to list strings from the database, running on a container-optimized compute instance

Once the system is stood up, the instance group manager will immediately make two web tier servers, which are docker containers with Apache/PHP and the PHP code, running on a container-optimized compute instance.

The microservices leverage Google Logging and Google Error Reporting, allowing informational and crash data to be read from the Google Console, and metrics to be developed.

The entire stack is codified in a Google Deployment Manager orchestration, allowing for the entire system to be created with one command. In order to set up to do this, the following steps need to be followed:
  * Check out the code from https://github.com/andyakins/GCPOC
  * Have the gcloud CLI installed on your local machine, configured and initialized. In particular, your Project should be selected.
  * Create a Google API Application Credential JSON file for your project. Copy this file to GCPOC/getService/credentials.json AND GCPOC/postService/credentials.json . Failure will do this will cause the microservices to fail due to failed authentication.
  * Change directory to GCPOC/cloud
  * Run the orchestration, where <name> is what you want to name this deployment (like "demo"): gcloud deployment-manager deployments create <name> --config gcpoc.yaml

This should build the entire stack into your Goggle Cloud Project. You can destroy the stack via the GUI or gcloud command.

NOTE: If you want to rebuild/change the project, and use your own versions, you must deploy your Docker containers to DockerHub, and change the name of the dockerImage value(s) in GCPOC/cloud/gcpoc.py to point to your containers. For local deployments of the docker containers, I made a helpful envvars.sh script to set the appropriate environment variables - which must also be passed to the containers upon running. You'll want to create the containers in the following order: database->microservices->frontend.

Things that could still be done (future work):
  * Use the Google Container Engine instead of container-optimized vms
  * Place the microservices under internal load balancers (Backends)
  * Figure out how to get Apache/PHP working under a lighter container (Alpine, instead of Centos)
  * Build out some more monitoring.
  * Generally dive deeper into some of the other Google Cloud features.

But overall I'm pleased with this first foray into Google Cloud and its orchestration.
