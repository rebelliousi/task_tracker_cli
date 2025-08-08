import sys
import os
import json
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
    now=datetime.now().isoformat
    task={
        'id':task_id,
        'description':description,
        'status':'todo',
        'createdAt':now,
        'updatedAt':now,
        
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'task added succesfully Id: {task_id}')


if __name__=='__main__':
    args=sys.argv
    if len(args)<2:
        print('usage command [argument]')
    if args[1]=='add':
        if len(args)<3:
            print('usage:python3 task.py add description')
        else:
            description=' '.join(args[2:])
            add_tasks(description)
        



Traceback (most recent call last):
  File "/home/rebellious/task-tracker-cli/challenge.py", line 48, in <module>
    add_tasks(description)
  File "/home/rebellious/task-tracker-cli/challenge.py", line 34, in add_tasks
    tasks.append(task)
AttributeError: 'NoneType' object has no attribute 'append'