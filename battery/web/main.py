# app.py - a minimal flask api using flask_restful
from flask import Flask, request
from flask_restful import Resource, Api
import json
import numpy as np
import datetime as dt

app = Flask(__name__)
api = Api(app)

battery={}

def get_capacity(voltage,current,vcutoff=3.0,delta=60):
    dv=np.gradient(voltage)
    tc0=np.argmax(dv[:]>0) #time step to start charging
    td0=np.argmax(dv[tc0:]<0) #time step to start discharging
    tc1=np.argmax(dv[tc0+td0:]>0)
    ti=tc0+td0
    tf=tc0+td0+tc1
    tcutoff=ti+np.argmax(voltage[ti:]<vcutoff)
    return current[ti:tcutoff].sum()*1000*60/3600

class BatteryHealth(Resource):
    def get(self, id):
        s_out=json.dumps(battery.get(id,{'error':'invalid id'}))
        return battery.get(id,{'error':'invalid id'})

    def post(self, id):
        #print(battery_id)
        #print(request.json)
        #s_in = request.form['data']
        data=request.json['data']
        #print(type(request.json))
        voltage=np.asarray(data['voltage'])
        current=np.asarray(data['current'])
        capacity=get_capacity(voltage,current)
        if capacity:
            battery[id]={
                'capacity':capacity, 
                'last_update':str(dt.datetime.now())
                }
            s_out=json.dumps(battery[id])
            return battery[id]
        else:
            return {'error':'not enough records'}

api.add_resource(BatteryHealth, '/<string:id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)