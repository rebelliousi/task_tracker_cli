import sys
import json
import os
from datetime import datetime


TASKS_FILE='tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE,'r') as f:
        return json.load(f)
        
def save_tasks(tasks):
    with open(TASKS_FILE,'w') as f:
        json.dump(tasks,f,indent=4)

def add_tasks(description):
    tasks=load_tasks()
    task_id=tasks[-1]['id']+1 if tasks else 1
    now=datetime.now().isoformat()
    task={
        'id':task_id,
        'description':description,
         'status':'todo',
         'createdAt':now,
         'updatedAt':now
         }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task addded succesfully (ID:{task_id})')
    
def list_tasks():
    tasks=load_tasks()
    if not tasks:
        print('no tasks found')
        return
    for task in tasks:
        print(f"id:{task['id']},description:{task['description']},status:{task['status']},createdAt:{task['createdAt']},updatedAt:{task['updatedAt']}")

def mark_task_done(task_id):
    tasks=load_tasks()
    found=False
    for task in tasks:
        if task['id']==task_id:
            task['status']='done'
            task['updatedAt']=datetime.now().isoformat()
            found=True
            break
    if found:
        save_tasks(tasks)
        print(f'Task {task_id} markes as done')
    else:
        print(f'Task id {task_id} not found')
    
def delete_task(task_id):
    tasks=load_tasks()
    new_tasks=[task for task in tasks if task['id']!=task_id]
    if len(new_tasks)==len(tasks):
        print(f'task id {task_id} not found')
        
    else:
        save_tasks(new_tasks)
        print(f'task id {task_id } deleted succesfully')
        


if __name__== '__main__':
    args=sys.argv
    if len(args)<2 :
        print('usage: command [arguments]')
    elif args[1]=='add':
      if len(args)<3:
        print('usage: python3 task.py add your description')
      else:
        add_tasks(args[2])
    elif args[1]=='done':
        if len(args)<3:
            print('usage:python3 task.py done task_id')
        else:
            try:
                task_id=int(args[2])
                mark_task_done(task_id)
            except ValueError:
                print('task id mus be a number')
                
    elif args[1]=='delete':
        if len(args)<3:
            print('usage:python3 task.py delete task_id')
        else:
            try:
                task_id=int(args[2])
                delete_task(task_id)
            except ValueError:
                print('task id must be a number')
    elif args[1]=='list':
        list_tasks()