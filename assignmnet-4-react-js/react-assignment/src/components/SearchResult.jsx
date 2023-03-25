import React from "react";
import "./SearchResult.css";

export const SearchResult = ({ result }) => {
  return (
    <div className="search-result">
      {result.disease +
        " " +
        result.year +
        " count per 100,000 " +
        result.rate_per_100_000_population}
    </div>
  );
};
