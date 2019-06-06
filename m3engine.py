import os
import uuid
from flask import Flask, jsonify, request
import m3engine_dog
import m3engine_handler
import m3engine_documents

app = Flask(__name__)
# Main module to import the Dog, Handler, and Document Management workflows

#Ucomment for unit testing
if __name__ == "__main__":
      app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', '5000')), threaded=True)
