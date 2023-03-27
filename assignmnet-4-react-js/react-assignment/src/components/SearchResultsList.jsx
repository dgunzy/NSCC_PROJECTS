import React from "react";
import { SearchResult } from "./SearchResult";

export const SearchResultsList = ({ results }) => {
  if (results.length < 1) {
    return (
      <div className="results-list">
        <p>Nothing matches your search!</p>
      </div>
    );
  }
  return (
    <div className="results-list">
      {results.map((result, id) => {
        return <SearchResult result={result} key={id} />;
      })}
    </div>
  );
};
