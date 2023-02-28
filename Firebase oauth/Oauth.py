import firebase_admin
from firebase_admin import credentials
from flask import Flask, request
from firebase_admin import auth

#initialize firebase application 
cred = credentials.Certificate('./glass-hydra-229623-firebase-adminsdk-9a2oy-5533ef8369.json')
firebase_admin.initialize_app(cred)

#Using auth module to introduce google sign in

# Create a user with Google credentials
def create_user_with_google(id_token):
    try:
        # Verify the Google ID token
        decoded_token = auth.verify_id_token(id_token)
        # Get the user ID from the decoded token
        uid = decoded_token['uid']
        # Create a new user with the verified Google ID token
        user = auth.get_user(uid)
        return user
    except auth.InvalidIdTokenError as e:
        print('Invalid ID token:', e)
        return None



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST','PUT'])
def index():
    if request.method == 'POST':
        # Handle POST request here
        return 'Received POST request'
    elif request.method == 'PUT':
        return "Fuck off"
    else:
        # Handle GET request here
        return 'Received GET request'

if __name__ == '__main__':
    app.run()

# Get the Google ID token from the client-side
id_token = request.form['idToken']

# Create a new user with Google credentials
user = create_user_with_google(id_token)

if user is not None:
    # User created successfully
    print('User created:', user.uid)
else:
    # User creation failed
    print('User creation failed.')


