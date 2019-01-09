from flaskapp import app
from flask import request

@app.route('/slack/debug', methods=['GET', 'POST'])
def lol_bot():
  print('Call to /slack/debug')
  result = ''
  for k, v in request.values.items():
    result += f'{k!r}: {v!r}\n'
  return result

if __name__ == '__main__':
  app.run()
