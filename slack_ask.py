from flaskapp import app
from flask import request

import re

@app.route('/slack/ask', methods=['GET', 'POST'])
def slack_ask_handler():
  question = request.values.get('text', '')
  match = re.match(r'^(where|what|when) (is|are) (the|my)? *(.*?)\??$',
                   question, re.IGNORECASE)
  if match:
    return f'_What_ {match.group(2)} {match.group(4)}?'
  return "I'm not sure I understand..."
