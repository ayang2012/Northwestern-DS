// establish fixed vars
var tableData = data;
var tbody = d3.select("tbody");

function buildTable(data) {
  // instantiate empty body
  tbody.html("");

  // create and append rows in body
  data.forEach((dataRow) => {
    var row = tbody.append("tr");
    Object.values(dataRow).forEach((val) => {
      var cell = row.append("td");
        cell.text(val);
      }
    );
  });
}

function handleClick() {
  d3.event.preventDefault();
  var date = d3.select("#datetime").property("value");
  let filteredData = tableData;
  if (date) {
    filteredData = filteredData.filter(row => row.datetime === date);
  }

  buildTable(filteredData);
}

// create butoon
d3.selectAll("#filter-btn").on("click", handleClick);

// create table
buildTable(tableData);
