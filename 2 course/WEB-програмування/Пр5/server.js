const express = require('express');
const Database = require('better-sqlite3');

const app = express();
const db = new Database('tasks.db'); 

app.use(express.json());
app.use(express.static('public'));

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
  )
`);

app.get('/api/tasks', (req, res) => {
  const tasks = db.prepare('SELECT * FROM tasks').all();
  res.json(tasks);
});

app.post('/api/tasks', (req, res) => {
  const { title } = req.body;
  if (!title || title.trim() === '') {
    return res.status(400).json({ error: 'Введіть текст завдання' });
  }

  const info = db.prepare('INSERT INTO tasks (title) VALUES (?)').run(title.trim());
  res.status(201).json({ id: info.lastInsertRowid, title: title.trim() });
});

app.delete('/api/tasks/:id', (req, res) => {
  const { id } = req.params;
  db.prepare('DELETE FROM tasks WHERE id = ?').run(id);
  res.json({ success: true });
});

app.listen(3000, () => {
  console.log('Сервер працює: http://localhost:3000');
});