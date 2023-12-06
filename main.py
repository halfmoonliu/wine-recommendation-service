
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = OPENAI_API_KEY)

def request_rep(user_input):
    prompt = user_input + ". Can you recommend me 5 wines specifying the wineries?"
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "user", 
     "content": prompt}
    ]
    )
    return completion.choices[0].message.content


def parse_wine(response):
    '''
    This function parses a text response from chatGPT and 
    returns a list of wine names and wineries
    input: a string of chatGPT response
    output: a tuple of (song name, artist name), both are strings
    '''
    sentences = [x.split(" ") for x in response.split("\n")]
    output = ""
    for sent in sentences:        
        split_ind = None        
        if len(sent) <= 1:
            pass
        else:
            for i in range(len(sent)):
                if sent[i] == ":":
                    split_ind = i
                elif sent[i][-1] == ":":
                    split_ind = i
                elif sent[i] == "-":
                    split_ind = i
            
            sentStart = sent[0][:-1]
            
            try:
                sentStart = int(sentStart)
            except:
                split_ind = None
        if split_ind != None:
            output += " ".join(sent[:split_ind]) + "\n"
    return output
    
#prompt = "I just got divorced"
#resp = request_rep(prompt)
#print(resp)
#print(parse_wine(resp))

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":        
        feeling = request.form["feeling"]
        if len(feeling) ==0 :
            return render_template("home.html")
        else:
            GPTresponse = request_rep(feeling)
            answer = parse_wine(GPTresponse)
            return render_template("response.html", gpt_response = answer)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)