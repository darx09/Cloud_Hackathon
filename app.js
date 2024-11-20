const form = document.getElementById('dataForm');
const resultDiv = document.getElementById('result');
const fetchDataBtn = document.getElementById('fetchData');
const dataList = document.getElementById('dataList');

// Submit data to the server
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const dataInput = document.getElementById('dataInput').value;

    const response = await fetch('/save', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data: dataInput }),
    });

    const result = await response.json();
    resultDiv.textContent = result.message || result.error;
});

// Fetch all data from the server
fetchDataBtn.addEventListener('click', async () => {
    const response = await fetch('/data');
    const data = await response.json();

    dataList.innerHTML = ''; // Clear the list
    data.forEach(([id, info]) => {
        const li = document.createElement('li');
        li.textContent = `${id}: ${info}`;
        dataList.appendChild(li);
    });
});
