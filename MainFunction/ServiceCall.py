import MainFunction
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/MainFunction/*": {"origins": "*"}})
api = Api(app)





class my_API(Resource):
    #SearchText=input("Enter the Item you want to buy - ")
    def get(self,SearchText,ProductPrice):
        #f = open("output.txt","w") #create add file in write mode.
        #f.write('{''data:'+str (sumTwoNumbers.sumTwo(first_number,second_number))+'}')
        #f. close() #closing file object.
        return {'data': (MainFunction.mainFunction(SearchText,ProductPrice))}

api.add_resource(my_API, '/MainFunction/<SearchText>/<ProductPrice>')

if __name__ == '__main__':
     app.run()
