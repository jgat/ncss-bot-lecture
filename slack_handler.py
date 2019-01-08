from webserver import app
from flask import request

import re

@app.route('/slack/ask', methods=['GET', 'POST'])
def slack_handler():
  question = request.values.get('text', '')
  match = re.match(r'(where|what|when) (is|are) (the|my)? *(.*)', text, re.IGNORECASE)
  if match:
    return f'What is {match.group(4)}?'
  return "I'm not sure I understand..."
