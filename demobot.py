# Import the flask library
from flask import Flask, request

# Create your web server
app = Flask(__name__)

# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    # Just a simple function that says Hello, World!
    return 'Hello, World!'

@app.route('/greeting', methods=['GET', 'POST'])
def user_greeting():

    # store the value in the get parameter
    name = request.values.get('text')
    return f'Hello {name}'

# Start the web server!
if __name__ == '__main__':
  app.run()
