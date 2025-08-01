from flask import Flask,jsonify,request,render_template
import json
import  os

DATA_FILE='data.json'

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE,'r') as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(DATA_FILE,'w') as f:
        json.dump(tasks,f,indent=4)


app=Flask(__name__)

tasks=[]

@app.route('/')

def home():
    return  render_template('index.html')

@app.route('/tasks',methods=['GET'])

def get_tasks():
    tasks=load_tasks()
    return jsonify(tasks)

@app.route('/tasks',methods=['POST'])

def add_task():
    tasks=load_tasks()
    new_tasks=request.get_json()
    task={
        'id':len(tasks)+1,
        'title':new_tasks.get('title','no title'),
        'completed':False
    }
    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task),201

@app.route('/tasks/<int:task_id>',methods=['PUT'])
def complete_task(task_id):
 tasks=load_tasks()
 for task in tasks: 
     if task['id']==task_id:
         task['completed']=True
         save_tasks(tasks)
         return jsonify(task) 

 return jsonify({'error':'task not found'}),404  

@app.route('/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    tasks=load_tasks()
    updated_tasks=[task for task in tasks if task['id']!=task_id]
    
    if len(updated_tasks)==len(tasks):
         return jsonify({'error':'task not found'}),404
     
    save_tasks(updated_tasks)
    return jsonify({'message ':f'Task {task_id} deleted succesfully'}),204
 
if __name__=='__main__':
    app.run(debug=True)