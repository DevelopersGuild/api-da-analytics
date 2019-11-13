from flask import Flask, render_template, request, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
import os
import pymongo
from dotenv import load_dotenv
load_dotenv()

# Database Setup
database_client = pymongo.MongoClient(os.getenv('MONGO_URI'))
db = database_client.loftly_analytics
submissions_collection = db.submissions_collection
app = Flask(__name__)
# Security Headers from Google Cloud Platform team and custom Content Security Policy to load js from trusted sources.
csp = {
    'default-src': ['\'self\'', '*.bootstrapcdn.com'],
    'script-src':
    ['\'self\'', '*.bootstrapcdn.com', '*.jquery.com', '*.cloudflare.com'],
    'img-src':
    '*'
}
# Talisman Middleware from GCP
talisman = Talisman(app,
                    content_security_policy=csp,
                    content_security_policy_nonce_in=['script-src'])
# Rate Limiter to prevent Abuse of Analytics API.
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["2 per minute", "1 per second"],
)

@app.route('/broad_survey', methods=['GET'])
@limiter.exempt
def broad_survey_route():
    return render_template('broad_survey.html')


@app.route('/thank_you', methods=['GET'])
@limiter.exempt
def thank_you_route():
    return render_template('complete.html')


@app.route('/analytics-log', methods=['POST'])
@limiter.limit("5 per hour")
def analytics_log():
    try:
        payload = {
            "client_ip": request.environ['REMOTE_ADDR'],
            "email": request.form['email'],
            "school": request.form['school'],
            "experience_number": request.form['experience_number'],
            "experience_paragraph": request.form['experience_paragraph'],
            "how_to_improve": request.form['how_to_improve'],
            "interview_ready": request.form['interview_ready']
        }
        submissions_collection.insert_one(payload)
        return redirect('/thank_you')
    except Exception as e:
        print(e)
        return e


if __name__ == "__main__":
    app.run(debug=True)