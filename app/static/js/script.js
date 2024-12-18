document.getElementById('searchForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;
    const response = await fetch(`/locations/nearby?latitude=${latitude}&longitude=${longitude}`);
    const data = await response.json();
    document.getElementById('results').innerHTML = JSON.stringify(data, null, 2);
});
