# Deploy A Wine Recommendation Service on Azure
This repo demos how to deploy a web-based wine recommendation service using Azure app service. On the front-end page, **users can input their preference, mood, or intended occasion** and **get recommendati**ons of wines** for their mood and **a link for wine shopping**.

## Executive Summary for Actionable Insights
A proof-of-concept of a new **customer engaging feature** is demonstrated below. The user can input their **feelings, thoughts, or events experienced recently** and **get recommendations of wines** and a **link for wine shopping**. The next **actions items** should include the following:
1. **Design user interface**: Invite the desinger team to make an interface suitable for this feature.
2. **Deploy the feature**: **Incorporate this feature to wine company website**.
3. **Collect and analyze data** for further actions: **conversion** rate can be used to assess feature effectiveness. Results on user behavior analysis can be used for **future sales compaign audience targetting** (e.g. who tends to use feature, what kinds of prompt triggers more purchase, etc.)

## Feature Walkthrough 
1. A small box is present for users to input their thought or feeling. If the box is left blank when the submit button is hit, **the page will just reload**.

<img width="230" alt="Empty" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/16a39bff-537f-46c6-a840-f6bf0f237c66">

2. An example input of feeling, which would be a prompt to the **Chat GPT API** for **wine recommendation**.<br>

<img width="230" alt="Input" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/06bdf660-aa83-4e30-8ecc-172f96acba69">

3. After hitting the button, the user would be redirected to page of **wine recommendation**, with **a link to the company's website**.<br>

<img width="337" alt="Response" src="https://github.com/halfmoonliu/wine-recommendation-service/assets/46064664/aa3b5045-a60f-42d2-9202-33d4be78c800">

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
