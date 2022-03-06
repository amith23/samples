from flask import Flask, json

api = Flask(__name__)

@api.route('/test', methods=['GET'])
def get_companies():
  return "hello from test api"

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=80) 
