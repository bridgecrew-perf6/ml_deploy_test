## Deploying a Python Flask application to AWS Lambda With Serverless Framework and CircleCI

#### the tools which will be using:
- Python 3.6 or above (the best language ever!)
- Flask 1.1.2
- NodeJS 12.X (For Serverless Framework)
- Serverless Framework
- AWS CLI
- Circle-CI
- AWS Lambda


#### How to run the project:

1. pip install virtualenv
2. virtualenv .env
3. source .env/Scripts/activate
4. pip install -r requirements.txt
5. AWS CLI installing and configuring: `https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html`
6. npm init
7. npm install -g serverless
8. deploy theserverless app in Lambda:
 	1. need to install the plugins required for the Flask application in the context of Serverless Framework: `npm install serverless-wsgi serverless-python-requirements --save-dev`
 	2. create the Serverless configuration: 'serverless.yml'
 		- name: Any name you want to give for your serverless function
		- app: This can be anything based on your file name and Flask app name 
		- runtime: This could be any version of Python in which your application is written in
		- region: The AWS region in which your Lambda function needs to get created.
		- check validate YAML: `https://codebeautify.org/yaml-validator`
 	3. run one command to deploy this to Lambda: 'sls deploy'

9. CircleCI:
	- Login to `https://circleci.com/signup/` and click on either Sign up using GitHub or BitBucket.
	- select based on which project you need to set up the CI/CD.
	- go to your project in CircleCI and add the deployment environment setup as environment variables: Project Setting->Environment Variables: `http://slss.io/aws-creds-setup`
		- `AWS_ACCESS_KEY_ID`
		- `AWS_DEFAULT_REGION`
		- `AWS_SECRECT_ACCESS_KEY`




