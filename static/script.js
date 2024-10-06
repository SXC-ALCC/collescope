const apiBaseUrl = "https://collescope.vercel.app/colleges";
let colleges = []; 

document.addEventListener("DOMContentLoaded", fetchColleges);

function fetchColleges() {
  fetch(apiBaseUrl)
    .then((response) => response.json())
    .then((data) => {
      colleges = data;
      populateLocationFilter(data);  
      displayColleges(data);        
    })
    .catch((error) => console.error("Error fetching data:", error));
}

function populateLocationFilter(colleges) {
  const locationFilter = document.getElementById("locationFilter");
  const locations = new Set();

  colleges.forEach(college => {
    locations.add(college.location); 
  });

  locations.forEach(location => {
    const option = document.createElement("option");
    option.value = location;
    option.textContent = location;
    locationFilter.appendChild(option);
  });
}

function displayColleges(colleges) {
  const container = document.getElementById("cards-container");
  container.innerHTML = "";

  colleges.forEach((college) => {
    const card = document.createElement("div");
    card.classList.add("card");

    card.innerHTML = `
      <div>
        <h3>${college.name}</h3>
        <p><strong>Location:</strong> ${college.location}</p>
        <p><a href="${college.website}" target="_blank">Visit Website</a></p>
      </div>
      <img src="${college.logo}">
    `;

    container.appendChild(card);
  });
}

function searchCollege() {
  const searchInput = document.getElementById("searchInput").value.toLowerCase();

  const filteredColleges = colleges.filter(college => {
    return college.name.toLowerCase().includes(searchInput);
  });

  displayColleges(filteredColleges); 
}

function filterByLocation() {
  const selectedLocation = document.getElementById("locationFilter").value;

  if (selectedLocation === "all") {
    displayColleges(colleges); 
  } else {
    const filteredColleges = colleges.filter(college => college.location.toLowerCase() === selectedLocation.toLowerCase());
    displayColleges(filteredColleges);
  }
}
