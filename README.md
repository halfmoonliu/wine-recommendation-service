# Deploy A Wine Recommendation Service on Azure
This repo demos how to deploy a web-based wine recommendation service using Azure app service. On the front-end page, **users can input their preference, mood, or intended occasion** and **get recommendati**ons of wines** for their mood and **a link for wine shopping**.

## Executive Summary for Actionable Insights
A proof-of-concept of a new **customer engaging feature** is demonstrated below. The user can input their **feelings, thoughts, or events experienced recently** and **get recommendations of wines** and a **link for wine shopping**. The next **actions items** should include the following:
1. **Design user interface**: Invite the desinger team to make an interface suitable for this feature.
2. **Deploy the feature**: **Incorporate this feature to wine company website**.
3. **Collect and analyze data** for further actions: **conversion** rate can be used to assess feature effectiveness. Results on user behavior analysis can be used for **future sales compaign audience targetting** (e.g. who tends to use feature, what kinds of prompt triggers more purchase, etc.)

## Feature Walkthrough 
1. A small box is present for users to input their thought or feeling. If the box is left blank when the submit button is hit, **the page will just reload**.

<img width="571" alt="Empty_URL" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/b26c0b9c-ec04-4d41-890a-bf316dc321df">


2. An example input of feeling, which would be a prompt to the **Chat GPT API** for **wine recommendation**.<br>

<img width="570" alt="Input_URL" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/c6bc9852-a54f-4539-a538-28767a771686">

3. After hitting the button, the user would be redirected to page of **wine recommendation**, with **a link to the company's website**.<br>

<img width="609" alt="Response_URL" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/38222606-1233-4c83-9d5a-0a6d8ca5cc6b">


Below is an overview of the repository:
   
1. **Main functions for querying on Dataset**
   <br>a. _main.py_: The main program building the **flask function**, that does the following:
      <br>i.   Build the home page for users to input feelings (*home()*).
      <br>ii.  Send the input as **prompt to** ***OPEN AI API*** to **get wine recommendation** (_request_rep_).
      <br>iii. **Parse ChatGPT response into readable wine products** (_parse_wine_)
   <br>b. _./templates_: Webpage template used.
       <br>i. _home.html_:  The **homepage for users to input feelings**.
       <br>ii. _response.html_:  The **response page** for **displaying recommeded wines and link for shopping**.
      
2. **Github actions setup for continuous integration**
  <br>c. _.github/workflows/main.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

3. **Other files for development environment settings**
  <br>d. _.devcontainer_: set up the environment for development.
  <br>e. _.gitignore_: specify file names to ignore.
  <br>f. _requirements.txt_: list required packages for the project.

4. **Description of the project**
   <br>g. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with example output and code snippets.
