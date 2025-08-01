
function loadTasks(){
fetch('/tasks')
.then(res=>res.json())
.then(tasks=>{

    const div=document.getElementById('tasks');
    div.innerHTML='';
    tasks.forEach(task=>{
        const p=document.createElement('p')
        p.textContent=`${task.id}, ${task.title}- ${task.completed ? 'completed' : 'waiting'}`;
        
        if (!task.completed){
            const completeBtn=document.createElement('button')
            completeBtn.textContent='Complete'
            completeBtn.style.marginLeft='10px'


            completeBtn.addEventListener('click',()=>{
                fetch(`/tasks/${task.id}`,{
                    method:'PUT',
                })
                .then(res=>{
                  
                    if (res.ok) return res.json()
                    else throw  new Error('cant completed')
                })
                .then(()=>{
                    // location.reload()
                      loadTasks()
                })
                .catch(err=>alert(err.message))


            })

            p.appendChild(completeBtn)
            div.appendChild(p)
        }

        const deleteBtn=document.createElement('button')
        deleteBtn.textContent='delete'
        deleteBtn.style.marginLeft='10px'

        deleteBtn.addEventListener('click',()=>{
            fetch(`/tasks/${task.id}`,{
                method:'DELETE',
            })
            .then(res=>{
                if (res.ok || res.status===204){
                    loadTasks()
                }
                else throw new Error('cannot delete it')
            })
             .catch(err=>alert(err.message))
        })
         p.appendChild(deleteBtn)
    div.appendChild(p)
       
})
   
})

}


document.getElementById('taskForm').addEventListener('submit',function(e){
  e.preventDefault()
 const title=document.getElementById('title').value;

 fetch('/tasks',{
    method:'POST',
    headers:{
        'Content-Type':'application/json'
    },
    body:JSON.stringify({title:title,completed:false})
 })
 .then(res=>res.json())
 .then(newTask=>{
    loadTasks()
    const div=document.getElementById('tasks')
    const p=document.createElement('p')
    p.textContent=`${newTask.id}.${newTask.title}-${newTask.completed ? 'completed':'waitng'}`
    div.appendChild(p)
 })
})


