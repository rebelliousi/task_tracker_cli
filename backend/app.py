from flask import Flask,jsonify,request


app=Flask(__name__)

tasks=[]

@app.route('/')

def home():
    return  'task tracker backend api'

@app.route('/tasks',methods=['GET'])

def get_tasks():
    return jsonify(tasks)

@app.route('/tasks',methods=['POST'])

def add_task():
    data=request.get_json()
    task={
        'id':len(tasks)+1,
        'title':data.get('title','no title'),
        'completed':False
    }
    tasks.append(task)
    return jsonify(task),201

@app.route('/tasks/<int:task_id>',methods=['PUT'])
def complete_task(task_id):
 for task in tasks: 
     if task['id']==task_id:
         task['completed']=True
         return jsonify(task) 
 return jsonify({'error':'task not found'}),404  

@app.route('/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    global tasks
    for task in tasks:
        if task['id']==task_id:
         tasks=[task for task in tasks if task['id']!=task_id]
         return jsonify({'message ':f'Task {task_id} deleted succesfully'}),204
    return jsonify({'error':'task not found'}),404
if __name__=='__main__':
    app.run(debug=True)