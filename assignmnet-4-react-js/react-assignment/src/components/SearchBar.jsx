import React, { useState, useRef, useEffect } from "react";
import { FaSearch } from "react-icons/fa";
import "./SearchBar.css";
const Url = "https://data.novascotia.ca/resource/mdfn-jkdg.json/";
export const SearchBar = ({ setResults }) => {
  const inputRef = useRef(null);
  const inputRef2 = useRef(null);
  const [input, setInput] = useState("");
  const [input2, setInput2] = useState("");

  useEffect(() => {
    fetchData();
  }, [input, input2]);

  async function fetchData() {
    await fetch("https://data.novascotia.ca/resource/mdfn-jkdg.json/")
      .then((response) => response.json())
      .then((json) => {
        const results = json.filter((entry) => {
          return (
            entry.year.toString() == input && entry.number_of_cases == input2
          );
        });

        setResults(results);
      });
  }

  const handleClick = () => {
    setInput(inputRef.current.value);
    setInput2(inputRef2.current.value);
  };
  return (
    <div className="input-wrapper">
      <FaSearch id="search-icon" />
      <input className="input1" placeholder="Enter a Year.." ref={inputRef} />

      <input
        className="input1"
        placeholder="Enter a Case count"
        ref={inputRef2}
      />
      <button onClick={handleClick}>Click To Search!</button>
    </div>
  );
};
