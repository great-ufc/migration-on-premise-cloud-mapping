import React, { useState, useRef, useEffect } from "react";
import "./App.css";

interface Message {
  sender: "user" | "ai";
  text: string;
  sources?: string[];
}

const App: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
    if (input.trim()) {
      const userMessage: Message = { sender: "user", text: input.trim() };
      setMessages((prevMessages) => [...prevMessages, userMessage]);
      setInput("");
      setLoading(true);
      setError("");

      try {
        const response = await fetch("http://localhost:8000/question/ask", {
          method: "POST",
          mode: 'cors',
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ question: input.trim() }),
        });

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        const data = await response.json();
        const aiMessage: Message = {
          sender: "ai",
          text: data.response,
          sources: data.sources,
        };

        setMessages((prevMessages) => [...prevMessages, aiMessage]);
      } catch (error) {
        console.error("Error:", error);
        setError("Failed to communicate with the server. Please try again.");
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-window">
        {messages.map((msg, index) => (
          <div key={index} className={`chat-message ${msg.sender}`}>
            <div className="sender">
              {msg.sender === "user" ? "You" : "Bot"}
            </div>
            <div className="message-text">{msg.text}</div>
            {msg.sources && (
              <div className="sources">
                <div className="sources-header">Sources: </div>
                {msg.sources.map((source, idx) => (
                  <span key={idx} className="source-tag">
                    {source}
                  </span>
                ))}
              </div>
            )}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      {error && <div className="error-message">{error}</div>}
      <div className="chat-input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && !loading && handleSend()}
          disabled={loading}
        />
        <button onClick={handleSend} disabled={loading}>
          {loading ? "Loading..." : "Send"}
        </button>
      </div>
    </div>
  );
};

export default App;
