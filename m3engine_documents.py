from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

docapi = "https://127.0.0.1" #This will change


@app.route('/api/v1/document/add',methods=['POST'])
def add():

    # Receive data from UI
    mydata = request.form # Put POST request data in a dictionary
    print mydata
    #Data Transformation - TBA based on what UI sends us

    # Send data to document
    uri = "/api/v1/document/add" #This might change depending on what the document guys do
    url = docapi + uri

    #response = requests.post(uri, data=mydata)
    #obj = json.loads(response.content)

    code = 500

    try:
        print "sending POST containing: " + str(mydata) + " to:" + url
    except ValueError:
        response = "FAIL"
        code = 401
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(mydata), code


@app.route('/api/v1/document/searchbyid',methods=['GET'])
def searchbyid():

    print 'BZLAJ'
    # Receive data from UI
    mydata = request.args # Put GET request data in a dictionary
    print mydata
    #Data Transformation - TBA based on what UI sends us

    handlerid = mydata['handlerid']

    # Send data to document
    uri = "/api/v1/document/searchbyid" #This might change depending on what the document guys do
    url = docapi + uri

    #response = requests.get(uri, params=mydata)
    #obj = json.loads(response.content)

    # Fake Return Document Data
    view_response = {'documentid': '1234', 'handlerid': handlerid, 'dogid': '1011', 'imageurl': 'https://ecs/image.png'}

    # Fake Response
    try:
        print "sending GET containing: " + str(view_response) + " to:" + url
    except ValueError:
        response = "FAIL"
        code = 400
        print response
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(view_response), code


@app.route('/api/v1/document/searchbystatus',methods=['GET'])
def searchbystatus():

    print 'BZLAJ'
    # Receive data from UI
    mydata = request.args # Put GET request data in a dictionary
    print mydata
    #Data Transformation - TBA based on what UI sends us

    mystatus = mydata['status']

    # Send data to document
    uri = "/api/v1/document/searchbystatus" #This might change depending on what the document guys do
    url = docapi + uri

    #response = requests.get(uri, params=mydata)
    #obj = json.loads(response.content)

    # Fake Return Document Data - this will be a list of dictionaries
    view_response = {'status' : mystatus, 'documentid': '1234', 'handlerid': '5678', 'dogid': '1011', 'imageurl': 'https://ecs/image.png'}, \
                    {'status' : mystatus, 'documentid': '1235', 'handlerid': '5679', 'dogid': '1012', 'imageurl': 'https://ecs/image2.png'}

    # Fake Response
    try:
        print "sending GET containing: " + str(view_response) + " to:" + url
    except ValueError:
        response = "FAIL"
        code = 400
        print response
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(view_response), code



@app.route('/api/v1/document/changestatus',methods=['GET'])
def changestatus():

    print 'BZLAJ'
    # Receive data from UI
    mydata = request.args # Put GET request data in a dictionary

    #Data Transformation - TBA based on what UI sends us

    mydocumentid = mydata['documentid']
    mynewstatus = mydata['status']

    # Send data to document
    uri = "/api/v1/document/changestatus" #This might change depending on what the document guys do
    url = docapi + uri

    #response = requests.get(uri, params=mydata)
    #obj = json.loads(response.content)

    # Fake Return Document Data - this will be a list of dictionaries
    view_response = {'status' : mynewstatus, 'documentid': mydocumentid, 'handlerid': '5678', 'dogid': '1011', 'imageurl': 'https://ecs/image.png'}, \

    # Fake Response
    try:
        print "sending GET containing: " + str(view_response) + " to:" + url
    except ValueError:
        response = "FAIL"
        code = 400
        print response
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(view_response), code

@app.route('/api/v1/document/deletedocument',methods=['DELETE'])
def deletedocument():

    mydata = request.form  # Put GET request data in a dictionary
    print mydata

    # Data Transformation - TBA based on what UI sends us
    mydocumentid = mydata['documentid']

    # Send data to document
    uri = "/api/v1/document/deletedocument" #This might change depending on what the document guys do
    url = docapi + uri

    #response = requests.get(uri, params=mydata)
    #obj = json.loads(response.content)

    # Fake Return Document Data - this will be a list of dictionaries
    #view_response = {'status' : mynewstatus, 'documentid': mydocumentid, 'handlerid': '5678', 'dogid': '1011', 'imageurl': 'https://ecs/image.png'}, \
    # Just returninung SUCCESS/FAIL

    # Fake Response
    response = ""
    try:
        print "sending data to "+ url
    except ValueError:
        response = "FAIL"
        code = 400
        print response
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(response), code



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5030')))
