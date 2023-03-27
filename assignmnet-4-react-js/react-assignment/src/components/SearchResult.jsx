import React from "react";
import "./SearchResult.css";

export const SearchResult = ({ result }) => {
  return (
    <div className="search-result">
      {result.disease +
        " Had " +
        result.number_of_cases +
        " cases in " +
        result.year +
        ". The count per 100,000 population is " +
        result.rate_per_100_000_population +
        "."}
    </div>
  );
};
