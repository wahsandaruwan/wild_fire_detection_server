const loadBtn = document.querySelector("#load-btn");

loadBtn.addEventListener("click", async () => {
  // Get data
  const response = await getData();

  // Check status
  if (response.status == 0) {
    console.log("hello");
  }
});

// Function for getting data
async function getData() {
  // Get data
  const response = await fetch("http://127.0.0.1:5000/data/read");

  // Convert to json
  const jsonData = await response.json();

  return jsonData;
}
