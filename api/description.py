from flask import Flask, Response, jsonify, request
from github import Github
	
# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv
 
# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')
 
# Load file from the path.
load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def catch_all(path):

    user = "ReubenMathew"
    pwd = secret_key = os.getenv('github_pass')

    repo_name = request.args.get('repo')

    g = Github(user, pwd)
    repos = {}
    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        repos[repo.name] = repo.description
    # print(repos)
    print("Description Request Successful")
    if(repo_name):
        return jsonify(result = repos[repo_name])
    else:
        return json.dumps({'success':True, 'dataAvailable' : False}), 200, {'ContentType':'application/json'}


if __name__ == "__main__":
    app.run()
