import { useState, useEffect } from "react";
import Quote from './Quote';

const QuoteContainer = () => {
    const [quote, setQuote] = useState({});
    const fetchQuote = async () => {
        try {
            const response = await fetch('https://programming-quotesapi.vercel.app/api/random');
            if (response.ok) {
                const data = await response.json();
                setQuote({ text: data.quote, author: data.author });
            } else {
                console.error('Error fetching quote:', response.status);
            }
        } catch (error) {
            console.error('Error fetching quote:', error);
        }
    };

    useEffect(() => {
        fetchQuote();
    }, []);

    const handleKeyDown = (event) => {
        if (event.key === "Space" || event.key === " " || event.key === "Enter"){
            fetchQuote();
        }
    }

    return (
        <div className="h-full flex justify-center items-center" onKeyDown={handleKeyDown} tabIndex={0}>
            {quote.text && quote.author ? <Quote text={quote.text} author={quote.author} /> : <Quote text="Loading..." author="Loading..." />}
        </div>
	);
}

export default QuoteContainer