import {useState} from 'react'
import './App.css'

type SentimentResponse = {
    result: string
};

function App() {
    const [apiData, setApiData] = useState<SentimentResponse | null>(null)
    const [textInput, setTextInput] = useState('')

    const handleSubmit = () => {
        fetch('http://localhost:5000/api/text-sentiment', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({text: textInput}),
        })
            .then(response => response.json())
            .then(result => setApiData(result))
    };

  return (
    <>
        <h1>Text Sentiment Analysis</h1>
        <div>{apiData?.result || 'Awaiting input'}</div>
        <textarea value={textInput} onChange={(e) => setTextInput(e.target.value)} onFocus={() => setApiData(null)} />
        <button onClick={handleSubmit}>Submit</button>
    </>
  )
}

export default App
