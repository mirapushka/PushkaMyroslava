const API_URL = 'https://6aedaf07a677fe0fc14f4071.mockapi.io/users';

const todoForm = document.getElementById('todo-form');
const todoInput = document.getElementById('todo-input');
const todoList = document.getElementById('todo-list');
const loadingDiv = document.getElementById('loading');
const errorDiv = document.getElementById('error-message');
const submitBtn = document.getElementById('submit-btn');
const totalCountSpan = document.getElementById('total-count');

function setLoading(isLoading) {
    if (isLoading) {
        loadingDiv.classList.remove('hidden');
        submitBtn.disabled = true;
    } else {
        loadingDiv.classList.add('hidden');
        submitBtn.disabled = false;
    }
}

function showError(message) {
    errorDiv.textContent = message;
    errorDiv.classList.remove('hidden');
}

function clearError() {
    errorDiv.textContent = '';
    errorDiv.classList.add('hidden');
}

function updateCounter(count) {
    totalCountSpan.textContent = count;
}

async function fetchTodos() {
    clearError();
    setLoading(true);

    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error('Помилка сервера');
        }

        const todos = await response.json();
        renderTodos(todos);
    } catch (error) {
        showError('Не вдалося завантажити список.');
        console.error(error);
    } finally {
        setLoading(false);
    }
}

function renderTodos(todos) {
    todoList.innerHTML = '';

    todos.forEach(todo => {
        const li = document.createElement('li');
        if (todo.completed) {
            li.classList.add('completed');
        }

        const span = document.createElement('span');
        span.textContent = todo.name;
        span.style.cursor = 'pointer';
        span.addEventListener('click', () => toggleTodoStatus(todo));

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Видалити';
        deleteBtn.classList.add('delete-btn');
        deleteBtn.addEventListener('click', () => deleteTodo(todo.id));

        li.appendChild(span);
        li.appendChild(deleteBtn);
        todoList.appendChild(li);
    });

    updateCounter(todos.length);
}

todoForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const taskText = todoInput.value.trim();
    if (!taskText) return;

    const newTodo = {
        name: taskText,
        completed: false
    };

    clearError();
    setLoading(true);

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newTodo)
        });

        if (!response.ok) {
            throw new Error('Не вдалося додати завдання');
        }

        todoInput.value = '';
        fetchTodos();
    } catch (error) {
        showError('Помилка при додаванні завдання.');
        console.error(error);
        setLoading(false);
    }
});

async function deleteTodo(id) {
    clearError();
    setLoading(true);

    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            throw new Error('Не вдалося видалити завдання');
        }

        fetchTodos();
    } catch (error) {
        showError('Помилка при видаленні завдання.');
        console.error(error);
        setLoading(false);
    }
}

async function toggleTodoStatus(todo) {
    clearError();

    const updatedTodo = {
        ...todo,
        completed: !todo.completed
    };

    try {
        const response = await fetch(`${API_URL}/${todo.id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedTodo)
        });

        if (!response.ok) {
            throw new Error('Не вдалося оновити статус');
        }

        fetchTodos();
    } catch (error) {
        showError('Помилка при оновленні завдання.');
        console.error(error);
    }
}

fetchTodos();