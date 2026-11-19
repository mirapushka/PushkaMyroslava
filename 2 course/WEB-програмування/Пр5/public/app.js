const form = document.getElementById('task-form');
const input = document.getElementById('task-input');
const list = document.getElementById('task-list');

async function loadTasks() {
  const response = await fetch('/api/tasks');
  const tasks = await response.json();

  list.innerHTML = ''; 
  tasks.forEach(task => {
    const li = document.createElement('li');
    li.textContent = task.title;

    const delBtn = document.createElement('button');
    delBtn.textContent = 'Видалити';
    delBtn.className = 'delete-btn';
    delBtn.onclick = () => deleteTask(task.id);

    li.appendChild(delBtn);
    list.appendChild(li);
  });
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const title = input.value;

  await fetch('/api/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title })
  });

  input.value = '';
  loadTasks(); 
});

async function deleteTask(id) {
  await fetch(`/api/tasks/${id}`, {
    method: 'DELETE'
  });

  loadTasks(); 
}

loadTasks();