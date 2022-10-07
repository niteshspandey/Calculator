from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pandas as pd
import sqlite3

app = Flask(__name__)   

@app.route('/',methods=['GET'])     
@cross_origin()
def homePage():
    return render_template("pages/form.html")

@app.route('/calculate',methods=['POST','GET'])   
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            feet1   =int(request.form['feet1'])
            inches1 =int(request.form['inches1'])
            feet2   =int(request.form['feet2'])
            inches2 =int(request.form['inches2'])
            rate =int(request.form['rate'])
            print(f'value of feet1 {feet1} and value of feet2 {feet2} value of inches1 {inches1} and inches2 in {inches2}')
            result=0
            if feet1==0 and inches1!=0 and feet2==0 and inches2!=0:
                print('First block')
                int_result=inches1 * inches2
                print('value of int_result is ',int_result)
                result=(int_result/144)
                print('entered values is', result)

            elif inches1==0 and inches2==0 and feet1!=0 and feet2!=0:
                print('2 block')
                int_result=(12*feet1)*(12*feet2)
                result=(int_result/144)
                print('entered values is', result)
            
            elif feet1!=0 and feet2!=0 and inches1!=0 and inches2!=0:
                print('3 block')
                int_result=((12*feet1)+inches1)*((12*feet2)+inches2)
                result=(int_result/144) 
                print('entered values is', result)

            elif feet1!=0 and inches1==0 and feet2!=0 and inches2!=0:
                print('4 block')
                int_result=((feet1*12)*((feet2*12)+inches2))
                result=(int_result/144)
                print('entered values is', result)

            elif feet1!=0 and inches1!=0 and feet2!=0 and inches2==0:
                print('5 block')
                int_result=(((feet1*12)+inches1)*(feet2*12))
                result=(int_result/144)
                print('entered values is', result)
            
            elif feet1!=0 and inches1==0 and feet2==0 and inches2==0:
                print('6 block')
                print('Only feet1',feet1)
                result=feet1
                print('entered values is', result)
            
            elif feet1==0 and inches1==0 and feet2!=0 and inches2==0:
                print('7 block')
                print('Only feet2',feet2)
                result=feet2
                print('entered values is', result)
            
            else:
                pass
        
            return render_template('/pages/result.html',m=round((result*rate),2),n=round((result),2))
        


        except Exception as e:
            print('The Exception message is: ',e)
            return 'Something is wrong.Please try again after some time'
    else:
        return render_template('form.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001, debug=True)
	#app.run(debug=True)