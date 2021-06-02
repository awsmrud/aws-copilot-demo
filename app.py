from flask import Flask
from flask import jsonify
from flask import request
import boto3

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"
    
ddb = boto3.client('dynamodb', region_name='us-west-2')

@app.route('/assets',methods=['GET'])
def getAssets():
    response = ddb.get_item(Key={'uuid':{'N':'1'},'name':{'S':'abc'}}, TableName='demo-app-test-demo-service-demo-ddb')
    return response['Item']



orders=[
 {
 'id':'1',
 'itemName':'book',
 'itemDesc':'Book on plants',
 'status':'not shipped'
 },
 {
 'id':'2',
 'itemName':'printer',
 'itemDesc':'Dell printer',
 'status':'shipped'
 }
 ]

@app.route('/orders/order',methods=['GET'])
def getAllOrders():
    return jsonify({'orders':orders})

@app.route('/orders/order/<orderId>',methods=['GET'])
def getOrder(orderId):
    ordget = [ order for order in orders if (order['id'] == orderId) ] 
    return jsonify({'order':ordget})


