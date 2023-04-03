import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import DropdownMenu from "./components/dropdown";
import { SearchResultsList } from "./components/SearchResultsList";

function App() {
  const [results, setResults] = useState([]);
  const [weather, setWeather] = useState([]);

  return (
    <div className="main">
      <h1>Nova Scotia Museum and Weather Search</h1>
      <p>
        Pick from this list of NS towns to see if they have any Museums, and see
        the current Weather!
      </p>
      <DropdownMenu setResults={setResults} setWeather={setWeather} />
      <SearchResultsList
        className="results-list"
        results={results}
        weather={weather}
        location={location}
      />
    </div>
  );
}

export default App;
