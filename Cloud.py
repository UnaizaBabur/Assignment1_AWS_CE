from flask import Flask
import requests
import boto3
import json

app = Flask(__name__)

@app.route('/')
def home():
    try:
        url = "https://app.ticketmaster.com/discovery/v2/events.json"
        params = {"apikey": "Ists66E03pLmPM43h35iVuqdDDVXUYEQ", "size": 6}
        
        response = requests.get(url, params=params)
        data = response.json()

        # Upload events data to S3
        s3 = boto3.client('s3')
        bucket_name = 'unievent-data-12345'   # CHANGE to your bucket name
        
        s3.put_object(
            Bucket=bucket_name,
            Key='events.json',
            Body=json.dumps(data)
        )

        if '_embedded' not in data:
            return "<h1>No events found.</h1>"

        events = data['_embedded']['events']

        output = """
        <html>
        <head>
        <title>UniEvent Portal</title>
        <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            margin: 0;
            padding: 0;
        }

        .header {
            background-color: #002147;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
        }

        .container {
            padding: 20px;
        }

        .event-card {
            background-color: white;
            padding: 15px;
            margin: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        .event-title {
            font-size: 22px;
            color: #002147;
            font-weight: bold;
        }

        .event-date {
            color: #e63946;
            font-weight: bold;
        }

        .event-venue {
            color: #2a9d8f;
        }

        .footer {
            background-color: #002147;
            color: white;
            text-align: center;
            padding: 10px;
            margin-top: 20px;
        }
        </style>
        </head>
        <body>

        <div class="header">
        UniEvent – University Event Management System
        </div>

        <div class="container">
        """

        for event in events:
            name = event['name']
            date = event['dates']['start']['localDate']
            venue = event['_embedded']['venues'][0]['name']

            output += f"""
            <div class="event-card">
                <div class="event-title">{name}</div>
                <p class="event-date">Date: {date}</p>
                <p class="event-venue">Venue: {venue}</p>
            </div>
            """

        output += """
        </div>

        <div class="footer">
        UniEvent Cloud System | Hosted on AWS | EC2 + S3 + ELB
        </div>

        </body>
        </html>
        """

        return output

    except Exception as e:
        return f"<h1>Error:</h1><p>{str(e)}</p>"

app.run(host='0.0.0.0', port=80)