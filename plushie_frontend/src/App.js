import logo from './logo.svg';
import './App.css';

function App() {
  const playMusic = async (callId) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/call/${callId}`);
      const data = await response.text();
    } catch (error) {
      console.error('Error playing music:', error);
    }
  };
  return (
    <div className="App">
      <header className="App-header">
          <div className="wrapper">
            <button onClick={() => playMusic(0)}>0</button>
            <button onClick={() => playMusic(1)}>1</button>
            <button onClick={() => playMusic(2)}>2</button>
            <button onClick={() => playMusic(3)}>3</button>
          </div>
        </header>
    </div>
  );
}

export default App;
