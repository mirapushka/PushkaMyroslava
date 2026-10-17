
const todoInput = document.getElementById('todo-input');
const addBtn = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');
const taskCounter = document.getElementById('task-counter');
const clearCompletedBtn = document.getElementById('clear-completed-btn');
const filterBtns = document.querySelectorAll('.filter-btn');

let tasks = [];
let currentFilter = 'all';

window.addEventListener('DOMContentLoaded', () => {
    const savedTasks = localStorage.getItem('myTasks');
    if (savedTasks) {
        tasks = JSON.parse(savedTasks);
    }
    renderTasks();
});

function saveToLocalStorage() {
    localStorage.setItem('myTasks', JSON.stringify(tasks));
}

function addTask() {
    const text = todoInput.value.trim();
    if (text === '') return; 

    const newTask = {
        id: Date.now(),
        text: text,
        completed: false
    };

    tasks.push(newTask);
    saveToLocalStorage();
    renderTasks();
    todoInput.value = '';
}

addBtn.addEventListener('click', addTask);
todoInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') addTask();
});

function renderTasks() {
    todoList.innerHTML = '';

    const filteredTasks = tasks.filter(task => {
        if (currentFilter === 'active') return !task.completed;
        if (currentFilter === 'completed') return task.completed;
        return true;
    });

    filteredTasks.forEach(task => {
        const li = document.createElement('li');
        if (task.completed) li.classList.add('completed');

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = task.completed;
        checkbox.addEventListener('change', () => toggleTask(task.id));

        const span = document.createElement('span');
        span.textContent = task.text;

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Видалити';
        deleteBtn.classList.add('delete-btn');
        deleteBtn.addEventListener('click', () => deleteTask(task.id));

        li.appendChild(checkbox);
        li.appendChild(span);
        li.appendChild(deleteBtn);
        todoList.appendChild(li);
    });

    updateCounters();
}

function toggleTask(id) {
    tasks = tasks.map(task => 
        task.id === id ? { ...task, completed: !task.completed } : task
    );
    saveToLocalStorage();
    renderTasks();
}

function deleteTask(id) {
    tasks = tasks.filter(task => task.id !== id);
    saveToLocalStorage();
    renderTasks();
}

function updateCounters() {
    const total = tasks.length;
    const active = tasks.filter(t => !t.completed).length;
    taskCounter.textContent = `Усього: ${total} | Не виконано: ${active}`;
}

clearCompletedBtn.addEventListener('click', () => {
    tasks = tasks.filter(t => !t.completed);
    saveToLocalStorage();
    renderTasks();
});

filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.dataset.filter;
        renderTasks();
    });
});