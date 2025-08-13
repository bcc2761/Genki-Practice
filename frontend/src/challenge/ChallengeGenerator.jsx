import "react"
import {useState, useEffect} from "react"
import {MCQChallenge} from "./MCQChallenge.jsx"

export function ChallengeGenerator() {
    const [challenge, setChallenge] = useState(null)
    const [isLoading, setIsLoading] = useState(false)
    const [error, setError] = useState(null)
    const [chapter, setChapter] = useState("chapter1")
    const [quota, setQuota] = useState(null)

    const fetchQuota = async () => {}

    const generateChallenge = async () => {}

    const getNextResetTime = () => {}

    return <div className="challenge-container">
        <h2>Genki Practice Generator</h2>

        <div className="quota-display">
            <p>Challenges remaining today: {quota?.quota_remaining || 0}</p>
            {quota?.quota_remaining === 0 && (
                <p>Next reset: {0}</p>
            )}
        </div>
        <div className="chapter-selector">
            <label htmlFor="chapter">Select Chapter:</label>
            <select 
                id="chapter" 
                value={chapter} 
                onChange={(e) => setChapter(e.target.value)}
                disabled={isLoading}
            >
                <option value="chapter1">Chapter 1</option>
                <option value="chapter2">Chapter 2</option>
                <option value="chapter3">Chapter 3</option>
                <option value="chapter4">Chapter 4</option>
                <option value="chapter5">Chapter 5</option>
                <option value="chapter6">Chapter 6</option>
                <option value="chapter7">Chapter 7</option>
                <option value="chapter8">Chapter 8</option>
                <option value="chapter9">Chapter 9</option>
                <option value="chapter10">Chapter 10</option>
            </select>
        </div>

        <button 
            onClick={generateChallenge} 
            disabled={isLoading || quota?.quota_remaining === 0}
            className="generate-button"
        >
            {isLoading ? "Generating..." : "Generate Challenge"}
        </button>

        {error && <div className="error-message">
            <p>{error}</p>
        </div>}

        {challenge && <MCQChallenge challenge={challenge}/>}
    </div>
}