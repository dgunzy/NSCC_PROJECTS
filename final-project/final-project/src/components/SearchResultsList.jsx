export const SearchResultsList = ({ results, weather }) => {
  if (weather.length > 0) {
    return (
      <div className="results-list">
        {results.map((result, id) => {
          return (
            <div key={result.address}>
              <p>
                {result.site +
                  ", is located in " +
                  result.town +
                  " where the current temperature is " +
                  weather[1][1].temp_c +
                  "c and the conditions are " +
                  weather[1][1].condition.text +
                  "."}
              </p>
            </div>
          );
        })}
      </div>
    );
  }
};
