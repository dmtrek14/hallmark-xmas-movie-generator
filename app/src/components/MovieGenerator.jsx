
//import { useState } from 'preact/hooks';
import {useState} from 'react'

const MovieGenerator = () => {
     const [movieTitle, setMovieTitle] = useState(null);
     const [movieSummary, setMovieSummary] = useState(null);

    
    const getMovie = async () => { 
        //title
        const responseTitle = await fetch('../movieTitles.json');
        const dataTitle = await responseTitle.json();
        const titleLength = dataTitle.length;
        const randTitle = Math.floor(Math.random() * (titleLength));

        //summary
        const responseSummary = await fetch('../movieSummaries.json');
        const dataSummary = await responseSummary.json();
        const summaryLength = dataSummary.length;
        const randSummary = Math.floor(Math.random() * (summaryLength));

        setMovieTitle(dataTitle[randTitle]);
        setMovieSummary(dataSummary[randSummary]);

    }

    return (
       <div className="movie">
        <button role="button" className="darkmode-toggle" onClick={getMovie} >Generate Hallmark Christmas Movie</button>
        <div className="movie-title box margin-16">
            {movieTitle} 
        </div>
        <div className="movie-summary box margin-16">
           {movieSummary}
        </div>
       </div>
    )

}

export default MovieGenerator