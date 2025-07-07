import React, { useState } from 'react';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [name, setName] = useState('');
  const [stage, setStage] = useState('start'); // 'start', 'chat', 'end'

  const handleStart = async () => {
    const response = await fetch('http://localhost:5000/api/start', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, message: input })
    });
    const data = await response.json();
    setMessages([...messages, 
      { sender: 'user', text: input },
      { sender: 'menti', text: data.question }
    ]);
    setStage('chat');
    setInput('');
  };

  const handleSend = async () => {
    const response = await fetch('http://localhost:5000/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input })
    });
    const data = await response.json();
    setMessages([...messages, 
      { sender: 'user', text: input },
      { sender: 'menti', text: data.question }
    ]);
    setInput('');
  };

  return (
    <div className="app">
      {stage === 'start' && (
        <div className="start-screen">
          <input value={name} onChange={(e) => setName(e.target.value)} placeholder="İsminiz" />
          <textarea value={input} onChange={(e) => setInput(e.target.value)} placeholder="Nasıl hissediyorsunuz?" />
          <button onClick={handleStart}>Başla</button>
        </div>
      )}

      {stage === 'chat' && (
        <div className="chat-screen">
          <div className="messages">
            {messages.map((msg, i) => (
              <div key={i} className={`message ${msg.sender}`}>
                {msg.text}
              </div>
            ))}
          </div>
          <textarea value={input} onChange={(e) => setInput(e.target.value)} />
          <button onClick={handleSend}>Gönder</button>
        </div>
      )}
    </div>
  );
}

export default App;