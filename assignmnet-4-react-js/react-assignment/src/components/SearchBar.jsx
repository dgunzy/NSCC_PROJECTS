import React, { useState, useRef } from "react";
import { FaSearch } from "react-icons/fa";
import "./SearchBar.css";

export const SearchBar = ({ setResults }) => {
  const inputRef = useRef(null);
  const inputRef2 = useRef(null);
  const [input, setInput] = useState("");
  const [input2, setInput2] = useState("");
  console.log(input);
  const fetchData = () => {
    fetch("https://data.novascotia.ca/resource/mdfn-jkdg.json/")
      .then((response) => response.json())
      .then((json) => {
        const results = json.filter((entry) => {
          return (
            entry.year.toString() == input && entry.number_of_cases == input2
          );
          //  && entry.number_of_cases.includes(value2)
        });

        setResults(results);
      });
  };

  // const handleChange = (value, value2) => {
  //   setInput(value);
  //   setInput2(value2);
  //   fetchData(value, value2);
  // };
  const handleClick = () => {
    setInput(inputRef.current.value);
    setInput2(inputRef2.current.value);

    fetchData();
  };
  return (
    <div className="input-wrapper">
      <FaSearch id="search-icon" />
      <input
        placeholder="Enter a Year.."
        ref={inputRef}
        // value={input}
        // onChange={(e) => handleChange(e.target.value)}
      />
      <input
        placeholder="Enter a Case count"
        ref={inputRef2}
        // value2={input2}
        // onChange={(e) => handleChange(e.target.value2)}
      />
      <button onClick={handleClick}> Search </button>
    </div>
  );
};
