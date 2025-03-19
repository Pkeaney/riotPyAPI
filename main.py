import requests
import json
import os
import secrets
from flask import Flask, request, render_template, session
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

api_key = os.getenv("RIOT_API_KEY")

if api_key:
    print("API key loaded successfully!")
else:
    print("API key is missing.  Please check your .env file.")

@app.route("/", methods=["GET", "POST"])
def home():
    data = None
    error = None
    agent_data = None

    if request.method == "POST":
        region = request.form.get("region", "").strip().lower()
        agent_name = request.form.get("agent", "").strip().lower()

        session["region"] = region
        session["agent_name"] = agent_name

        if region:
            url = f"https://{region}.api.riotgames.com/val/content/v1/contents"
            headers = {"X-Riot-Token": api_key}

            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                full_data = response.json()
                print("Full Data:", full_data["characters"])
                print("agent_name: ", agent_name)
                print("agent_data: ", agent_data)
                for character in full_data.get("characters", []):
                    print("character name: ", character["name"].lower())
                    if character["name"].lower() == agent_name:
                        print("THIS MATCHES THE AGENT NAME!!!")

                if agent_name:
                    for character in full_data.get("characters", []):
                        if character["name"].lower() == agent_name:
                            print(f"{agent_name} is a match")
                            agent_data = character
                            break

                    if agent_data:
                        with open("valorant_content.json","w") as file:
                            json.dump(agent_data, file, indent=4)
                    else:
                        error = f"No agent found for '{agent_name}'"

                else:
                    with open("valorant_content.json", "w") as file:
                        json.dump(full_data, file, indent=4)

                data = full_data

            else:
                error = f"Error: {response.status_code}: {response.text}"

    return render_template("index.html", data=data, agent_data=agent_data, error=error, saved_region=session.get("region", ""), saved_agent=session.get("agent_name", ""))

if __name__ == "__main__":
    app.run(debug=True)
