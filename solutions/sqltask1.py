from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host="localhost",user="root",password="system")
cursor = mydb.cursor()
cursor.execute("create database if not exists api_task")
cursor.execute("use api_task")
cursor.execute("create table if not exists task_sol(name varchar(30),number int)")

@app.route('/insert',methods=['GET','POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into task_sol values(%s,%s)",(name,number))
        mydb.commit()
        return jsonify(str("Successfully inserted"))

@app.route('/update',methods=['GET','Post'])
def update():
    if request.method == 'POST':
        name = request.json['get_name']
        cursor.execute("update task_sol set number=number+1000 where name=(%s)",(name,))
        mydb.commit()
        return jsonify(str('updated successfully'))
if __name__== '__main__':
    app.run()