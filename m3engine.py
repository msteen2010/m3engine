import os
import uuid
import json
import requests
from flask import Flask, jsonify, request

UserID = "Blah"
docapi_server = ""
handlerapi_server = ""
dogapi_server = ""

app = Flask(__name__)

## Check for runtime location
if 'VCAP_SERVICES' in os.environ:
    handlerapi_server = "http://handlers.cfapps.io"
else: 
    handlerapi_server = "http://127.0.0.1:5010"

if 'VCAP_SERVICES' in os.environ:
    dogapi_server = "http://dogs.cfapps.io"
else: 
    dogapi_server = "http://127.0.0.1:5020"

if 'VCAP_SERVICES' in os.environ:
    docapi_server = "https://doco.cfapps.io"
else:
    docapi_server = "http://127.0.0.1:5030"

print("handler_server: %s" % handlerapi_server)
print("docapi_server: %s" % docapi_server)
print("dogapi_server: %s" % dogapi_server)

##
## Status APIs to check on all microservice dependencies
##
## Test Handlers status
@app.route('/api/v1/handler/status',methods=["GET"])
def handlerstatus():
    apiuri = "/api/v1/handler/hstatus"

    handler_status = requests.get(handlerapi_server + apiuri)

    if handlerapi_status:
        response = {'status': "Handlers API returns my ping"}
        code = 200
    else:
        response = {'statuscode': 400}
        code = 400

    return jsonify(response), code

## Test Dogs Microservice status
@app.route('/api/v1/dog/status',methods=["GET"])
def dogstatus():
    apiuri = "/api/v1/dog/status"

    dog_status = requests.get(dogapi_server+apiuri)

    if dogapi_status:
        response = {'status': "Dog API returns my ping"}
        code = 200
    else:
        response = {'statuscode': 400}
        code = 400

    return jsonify(response), code

## Test Docuements Microservice status
@app.route('/api/v1/document/status',methods=["GET"])
def documentstatus():
    apiuri = "/api/v1/doc/status"

    docapi_status = requests.get(docapi_server+apiuri)

    if docapi_status:
        response = {'status': "Document API returns my ping"}
        code = 200
    else:
        response = {'statuscode': 400}
        code = 400

    return jsonify(response), code

## Test self
@app.route('/api/v1/m3estatus', methods=["GET"])
def m3estatus():

    response = {'status': "m3engine API up and running"}
    statuscode = 200

    return jsonify(response),statuscode

# Handler API Calls
#
#
# CRUD Operations
## Call handler create API
@app.route('/api/v1/handler/add',methods=['POST'])
def handler_add():
    apiuri = "/api/v1/create"

    parameters = request.form
##    parameters.to_dict()

    add_response = requests.post(handlerapi_server + apiuri, json=parameters)
    
    if add_response:
        response = {'Result': 'Handler Add - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Handler Add - FAIL'}
        code = 400
        
    return jsonify (response), code

## Call handler read API
@app.route('/api/v1/handler/view',methods=["GET"])
def handler_view():
    apiuri = "/api/v1/read"
    data = request.args
    
    userid = data['userid']
    h_id = data['h_id']
    parameters = {'h_id': h_id}

    handler_response = requests.get(handlerapi_server + apiuri, params=parameters)
    
    if handler_response:
        handler_content = json.loads(handler_response.content)
        response = handler_content
        code = 200
    else:
        response = {'Result': 'Handler View: FAIL'}
        code = 400
    
    return jsonify(response), code

## Call handler update API
@app.route('/api/v1/handler/update',methods=['PUT'])
def handler_update():
    global userid
    global h_id

    apiuri = "/api/v1/update"
    data = request.form

    userid = data['userid']
    h_id = data['h_id']

    parameters = {'h_id':h_id}

    try:
        parameters['h_picture'] = data['h_picture']
    except:
        print("No change to Handler picture")
    try:
        parameters['h_servicedogid'] = data['h_servicedogid']
    except:
        print("No change to Handler service dog")
    try:
        parameters['h_trainerorg'] = data['h_trainerorg']
    except:
        print("No change to Handler organisation")
    print(parameters)
    
    update_response = requests.put(handlerapi_server + apiuri, json=parameters)
    
    if update_response.status_code:
        response = {'Result': 'Handler Update - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Handler Update - FAIL'}
        code = 400
        
    return jsonify (response), code 

## Call handler delete API
@app.route('/api/v1/handler/delete',methods=['DELETE'])
def handler_delete():
    global userid
    global h_id
    
    data = request.form
    
    userid = data['userid']
    h_id = data['h_id']
    parameters = {'h_id':h_id}

    apiuri = "/api/v1/delete"
    
    delete_response = requests.delete(handlerapi_server + apiuri, params=parameters)


    if delete_response:
        response = {'Result': 'Handler Delete - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Handler Delete - FAIL'}
        code = 400
        
    return jsonify (response), code

## Unimplemeted API entries
##@app.route('/api/v1/handler/searchhandlerid',methods=['GET'])
##def searchhandlerid():
##    response = {'Result': 'Not Implemented'}
##    code = 200
##    return jsonify (response), code
##
##@app.route('/api/v1/handler/searchbyname',methods=['GET'])
##def searchbyname():
##    response = {'Result': 'Not Implemented'}
##    code = 200
##    return jsonify (response), code
##
##@app.route('/api/v1/handler/searchbyzip',methods=['GET'])
##def searchbyzip():
##    response = {'Result': 'Not Implemented'}
##    code = 200
##    return jsonify (response), code

# Dog API Calls
#
#
# CRUD Operations
## Call dog create API
@app.route('/api/v1/dog/add',methods=['POST'])
def dog_add():
    apiuri = "/api/v1/createdog"
    parameters = request.form

    add_response = requests.post(dogapi_server + apiuri, json=parameters)

    if add_response:
        response = {'Result': 'Dog Add - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Dog Add - FAIL'}
        code = 400

    return jsonify (response), code

## Call dog view API
@app.route('/api/v1/dog/view',methods=['GET'])
def dog_view():
    apiuri = "/api/v1/readdog"
    data = request.args

    userid = data ['userid']
    regid = data ['sd_regid']
    parameters = {"sd_regid": regid}

    view_response = requests.get(dogapi_server + apiuri, params=parameters)

    view_response = json.loads(view_response.content)

    if view_response:
        response = view_response
        code = 200
    else:
        response = {'Result': 'Dog View: FAIL'}
        code = 400

    return jsonify(response), code

## Call dog update API
@app.route('/api/v1/dog/update',methods=['PUT'])
def dog_update():
    global userid
    global regid

    apiuri = "/api/v1/updatedogs/regstatus"
    data = request.form

    userid = data['userid']
    regid = data['sd_regid']
    parameters = {'sd_regid':regid}

    try:
        parameters['sd_picture'] = data['sd_picture']
    except:
        print("No Change to Dog picture")
    try:
        parameters['sd_regstatus'] = data['sd_regstatus']
    except:
        print("No change to registration data")
    try:
        parameters['sd_expiredate'] = data['sd_expiredate']
    except:
        print("No change to expiry date")
    try:
        parameters['sd_teamstatus'] = data['sd_teamstatus']
    except:
        print("No change to Team Status")
    try:
        parameters['sd_handlerid'] = data['sd_handlerid']
    except:
        print("No change to Handler ID")
    try:
        parameters['sd_vaccstatus'] = data['sd_vaccstatus']
    except:
        print("No Change to Vaccination Status")
    try:
        parameters['sd_vaccexpiredate'] = data['sd_vaccexpiredate']
    except:
        print("No change to Vaccination Expiry")
    try:
        parameters['sd_trainername'] = data['sd_trainername']
    except:
        print("No change to Trainer Name")
    try:
        parameters['sd_trainerorg'] = data['sd_trainerorg']
    except:
        print("No change to Trainer Organisation")

    update_response = requests.put(dogapi_server + apiuri, data=parameters)

    if update_response:
        response = {'Result': 'Dog Update - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Dog Update - FAIL'}
        code = 400

    return jsonify (response), code

## Call dog delete API
@app.route('/api/v1/dog/delete',methods=['DELETE'])
def dog_delete():
    global userid
    global regid

    apiuri = "/api/v1/deletedog"
    data = request.form

    userid = data['userid']
    regid = data['sd_regid']
    parameters = {'sd_regid':regid, 'sd_regstatus': 'False', 'sd_teamstatus': 'Expired'}

    delete_response = requests.delete(dogapi_server + apiuri, data=parameters)

    if delete_response:
        response = {'Result': 'Dog Retire - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Dog Retire - FAIL'}
        code = 400

    return jsonify (response), code

## Unimplemeted API entries
#@app.route('/api/v1/dog/searchdogid',methods=['GET'])
#def searchdogid():
#    response = {'Result': 'Not Implemented'}
#    code = 200
#    return jsonify (response), code
#
#@app.route('/api/v1/dog/searchbyname',methods=['GET'])
#def searchbyname():
#    response = {'Result': 'Not Implemented'}
#    code = 200
#    return jsonify (response), code
#
#@app.route('/api/v1/dog/searchbyzip',methods=['GET'])
#def searchbyzip():
#    response = {'Result': 'Not Implemented'}
#    code = 200
#    return jsonify (response), code
#
#@app.route('/api/v1/dog/searchavailablebyzip',methods=['GET'])
#def searchavailablebyzip():
#    response = {'Result': 'Not Implemented'}
#    code = 200
#    return jsonify (response), code
#
#@app.route('/api/v1/dog/searchvaccination',methods=['GET'])
#def searchvaccination():
#    response = {'Result': 'Not Implemented'}
#    code = 200
#    return jsonify (response), code

# Document API Calls
#
#
#
# CRUD Operations
## Call document create API
@app.route('/api/v1/document/add',methods=['POST'])
def doc_add():
    apiuri = "/api/v1/add"
    # Receive data from UI
    mydata = request.form # Put POST request data in a dictionary

    #Data Transformation - TBA based on what UI sends us

    # Send data to document

    #response = requests.post(uri, data=mydata)
    #obj = json.loads(response.content)

    code = 500

    try:
        print("sending POST containing: " + str(mydata) + " to:" + docapi_server + apiuri)
    except ValueError:
        response = "FAIL"
        code = 401
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(mydata), code

## Call document search API
@app.route('/api/v1/document/searchbyid',methods=['GET'])
def doc_searchbyid():

    apiuri = "/api/v1/searchbyhandlerid"
    # Receive data from UI
    mydata = request.args # Put GET request data in a dictionary
    #Data Transformation - TBA based on what UI sends us

    handlerid = mydata['handlerid']

    # Send data to document
    url = docapi_server + apiuri

    #response = requests.get(docapi_server + apiuri, params=mydata)
    #obj = json.loads(response.content)

    # Fake Return Document Data
    view_response = {'documentid': '1234', 'handlerid': handlerid, 'dogid': '1011', 'imageurl': 'https://ecs/image.png'}

    # Fake Response
    try:
        print("sending GET containing: " + str(view_response) + " to:" + docapi_server + apiuri)
    except ValueError:
        response = "FAIL"
        code = 400
        print(response)
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(view_response), code

# Call document search API
@app.route('/api/v1/document/searchbystatus',methods=['GET'])
def doc_searchbystatus():
    apiuri = "/api/v1/searchbystatus"

    mydata = request.args
    mystatus = mydata['status']

    #response = requests.get(docapi_server + apiuri, params=mydata)
    #obj = json.loads(response.content)

    # Fake Return Document Data - this will be a list of dictionaries
    view_response = {'status' : mystatus, 'documentid': '1234', 'handlerid': '5678', 'dogid': '1011', 'imageurl': 'https://ecs/image.png'}, \
                    {'status' : mystatus, 'documentid': '1235', 'handlerid': '5679', 'dogid': '1012', 'imageurl': 'https://ecs/image2.png'}

    # Fake Response
    try:
        print("sending GET containing: " + str(view_response) + " to:" + docapi_server + apiuri)
    except ValueError:
        response = "FAIL"
        code = 400
        print(response)
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(view_response), code

## Call document update API
@app.route('/api/v1/document/changestatus',methods=['GET'])
def doc_changestatus():
    apiuri = "/api/v1/changestatus"
    mydata = request.args 

    mydocumentid = mydata['documentid']
    mynewstatus = mydata['status']

    #response = requests.get(docapi_server + apiuri, params=mydata)
    #obj = json.loads(response.content)

    # Fake Return Document Data - this will be a list of dictionaries
    view_response = {'status' : mynewstatus, 'documentid': mydocumentid, 'handlerid': '5678', 'dogid': '1011', 'imageurl': 'https://ecs/image.png'}, \

    # Fake Response
    try:
        print("sending GET containing: " + str(view_response) + " to:" + docapi_server + apiuri)
    except ValueError:
        response = "FAIL"
        code = 400
        print(response)
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(view_response), code

## Call document delete API
@app.route('/api/v1/document/deletedocument',methods=['DELETE'])
def doc_deletedocument():
    apiuri = "/api/v1/deletedocument"
    mydata = request.form 

    mydocumentid = mydata['documentid']

    #response = requests.get(docapi_server + apiuri, params=mydata)
    #obj = json.loads(response.content)

    # Fake Return Document Data - this will be a list of dictionaries
    #view_response = {'status' : mynewstatus, 'documentid': mydocumentid, 'handlerid': '5678', 'dogid': '1011', 'imageurl': 'https://ecs/image.png'}, \
    # Just returninung SUCCESS/FAIL

    # Fake Response
    response = ""
    try:
        print("sending data to "+ docapi_server + apiuri)
    except ValueError:
        response = "FAIL"
        code = 400
        print(response)
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(response), code

#Ucomment for unit testing
if __name__ == "__main__":
      app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', '5000')), threaded=True)
