import { useState } from "react";

import "./App.css";
import { SearchBar } from "./components/SearchBar";
import { SearchResultsList } from "./components/SearchResultsList";

function App() {
  const [results, setResults] = useState([]);
  return (
    <div className="App">
      <h2>Disease Search for NS</h2>
      <p>Enter a number of cases (Typically between 0 and 20): </p>
      <p>Enter a 4 digit year (Between 2005 and 2017): </p>

      <div className="seach-bar-container">
        <SearchBar setResults={setResults} />

        <SearchResultsList results={results} />
      </div>
    </div>
  );
}

export default App;
