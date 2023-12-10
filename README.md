[![Continuous Integration Quality Check](https://github.com/halfmoonliu/wine-recommendation-service/actions/workflows/cicd.yml/badge.svg)](https://github.com/halfmoonliu/wine-recommendation-service/actions/workflows/cicd.yml)

# Deploy A Wine Recommendation Service on Azure
This repo demos how to deploy a web-based wine recommendation service using Azure app service. On the front-end page, **users can input their preference, mood, or intended occasion** and **get recommendations of wines** for their mood and **a link for wine shopping**.

## Executive Summary for Actionable Insights
A proof-of-concept of a new **customer engaging feature** is demonstrated below. The user can input their **feelings, thoughts, or events experienced recently** and **get recommendations of wines** and a **link for wine shopping**. The next **actions items** should include the following:
1. **Design user interface**: Invite the designer team to make an interface suitable for this feature.
2. **Deploy the feature**: **Incorporate this feature to wine company website**.
3. **Collect and analyze data** for further actions: **conversion** rate can be used to assess feature effectiveness. Results on user behavior analysis can be used for **future sales campaign audience targeting** (e.g. who tends to use feature, what kinds of prompt triggers more purchase, etc.)

## Feature Walkthrough 
1. A small box is present for users to input their thought or feeling. If the box is left blank when the submit button is hit, **the page will just reload**.

<img width="571" alt="Empty_URL" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/b26c0b9c-ec04-4d41-890a-bf316dc321df">

2. An example input of feeling, which would be a prompt to the **Chat GPT API** for **wine recommendation**.<br>

<img width="570" alt="Input_URL" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/c6bc9852-a54f-4539-a538-28767a771686">

3. After hitting the button, the user would be redirected to page of **wine recommendation**, with **a link to the company's website**.<br>

<img width="611" alt="Response_URL" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/c6f73995-4177-4ea3-9e33-91a0c7452bb4">

## Upload the Docker image for other to run

After creating an **docker image** for the app, it can be shared (pushed) onto **Docker Hub**, and **people can download the img file to run the app locally** (The docker company has an clear [tutorial](https://docs.docker.com/get-started/04_sharing_app/) for doing exactly that). Below is the code for running the docker image locally.

```
Docker run [image_name]
```
<img width="1123" alt="Dockerhub" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/b00c331b-93f3-493f-9113-b525b8cbf2f7">

## Deploy service on Azure

Once the app is built, we can use the docker file to create a docker image. To deploy the app on Azure, one should create an **Azure Container Registry**, **create a container repo**, **push the docker image onto to repo**, and use **the Azure app service** to deploy the app on Azure.

```
# Build docker image on Azure container registry
docker build -t [RegistryName.azurecr.io]/myapp .

# install homebrew for installing Azure cli (if needed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update && brew install azure-cli

# log in to Azure
az login --tenant 9665bee9-59c7-43dd-b86b-1b15d598b932
az acr login --name [RegistryName]

# push docker image on Azure container repository
docker push [RegistryName.azurecr.io]/myapp
```
Created Container Registry:
<img width="1278" alt="AzureContainerRegistry" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/8967ae5a-44d4-428d-a951-0bc87fe7967b">

Created Container Repository
<img width="1266" alt="AzureContainerRepo" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/6c35e0c9-17bb-4611-a032-7826b161f340">

Deployed Web Service
<img width="1277" alt="AzureAppService" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/5465aba8-a00b-4c16-a988-d26eb719c159">


Below is an overview of the repository:
   
1. **Main functions for querying on Dataset**
   <br>a. _app.py_: The main program building the **flask function**, that does the following:
      <br>i.   Build the home page for users to input feelings (*home()*).
      <br>ii.  Send the input as **prompt to** ***OPEN AI API*** to **get wine recommendation** (_request_rep_).
      <br>iii. **Parse ChatGPT response into readable wine products** (_parse_wine_)
   <br>b. _./templates_: Webpage template used.
       <br>i. _home.html_:  The **homepage for users to input feelings**.
       <br>ii. _response.html_:  The **response page** for **displaying recommended wines and link for shopping**.
   <br>c. _test_app.py_: Test functions for the application.
   
3. **Github actions setup for continuous integration**
  <br>d. _.github/workflows/main.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

4. **Other files for development environment settings**
  <br>e. _.devcontainer_: set up the environment for development.
  <br>f. _.gitignore_: specify file names to ignore.
  <br>g. _requirements.txt_: list required packages for the project.

5. **Description of the project**
   <br>h. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with example output and code snippets.
