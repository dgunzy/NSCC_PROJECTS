import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";

function DropdownMenu({ setResults, setWeather, setLocation }) {
  async function callMuseumApi(town) {
    await fetch(
      "https://data.novascotia.ca/resource/f84a-3hfv.json?town=" + town
    )
      .then((response) => response.json())
      .then((json) => {
        const results = json.filter((entry) => {
          return entry.site;
        });

        setResults(results);
      });
  }
  async function callWeatherApi(town) {
    await fetch(
      "http://api.weatherapi.com/v1/current.json?key=4ca5db1890dd4699985141522233103&q=" +
        town +
        "&aqi=no"
    )
      .then((response) => response.json())
      .then((json) => {
        const weather = Object.entries(json);
        setWeather(weather);
      });
  }

  window.addEventListener("click", (e) => {
    if (e.target.id == "0") {
      callMuseumApi(e.target.title);

      callWeatherApi(e.target.name);
    }
  });
  return (
    <div className="left">
      <DropdownButton id="dropdown-basic-button" title="   NS Town List  ">
        <Dropdown.Item id="0" name="B0K%201V0" title="Balmoral%20Mills">
          Balmoral Mills
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0W%201E0" title="Barrington">
          Barrington
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B4V%203X9" title="Bridgewater">
          Bridgewater
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0K%201V0" title="Denmark">
          Denmark
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0S%201A0" title="Granville%20Ferry">
          Granville Ferry
        </Dropdown.Item>
        <Dropdown.Item id="0" name="Halifax" title="Halifax">
          Halifax
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B2C%201A" title="Iona">
          Iona
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0T%201K0" title="Liverpool">
          Liverpool
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0J%202C0" title="Lunenburg">
          Lunenburg
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0N%201T0" title="Maitland%20">
          Maitland
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0N%201Z0" title="Mount%20Uniacke%20">
          Mount Uniacke
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0J%202M0" title="New%20Ross%20">
          New Ross
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0J%201W0" title="Oyster%20Pond%20">
          Oyster Pond
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0M%201S0" title="Parrsboro">
          Parrsboro
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0K%201H0" title="Pictou">
          Pictou
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0T%201W0" title="Shelburne">
          Shelburne
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0J%203C0" title="Sherbrooke">
          Sherbrooke
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0K%201S0" title="Stellarton%20">
          Stellarton
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0W%202C0" title="West%20Pubnico">
          West Pubnico
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0N%202T0" title="Windsor%20">
          Windsor
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B0P%201T0" title="Wolfville">
          Wolfville
        </Dropdown.Item>
        <Dropdown.Item id="0" name="B5A%201G9" title="Yarmouth">
          Yarmouth
        </Dropdown.Item>
      </DropdownButton>
    </div>
  );
}

export default DropdownMenu;
