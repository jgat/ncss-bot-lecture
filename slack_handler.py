from webserver import app
from flask import request

@app.route('/slack/ask', methods=['GET', 'POST'])
def slack_handler():
  question = request.values.get('text', '')
  return repr(question)
