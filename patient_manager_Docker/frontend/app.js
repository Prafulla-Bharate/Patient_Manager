// File: app.js
const API_URL = "http://localhost:8000";

const form = document.getElementById("patientForm");
const list = document.getElementById("patientList");

// Load patients when page loads
window.onload = loadPatients;

form.onsubmit = async (e) => {
    e.preventDefault();

    const patient = {
        id: document.getElementById("id").value,
        name: document.getElementById("name").value,
        city: document.getElementById("city").value,
        age: parseInt(document.getElementById("age").value),
        gender: document.getElementById("gender").value,
        height: parseFloat(document.getElementById("height").value),
        weight: parseFloat(document.getElementById("weight").value)
    };

    const response = await fetch(`${API_URL}/create`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(patient)
    });

    if (response.ok) {
        alert("Patient added or updated!");
        form.reset();
        loadPatients();
    } else {
        const res = await response.json();
        alert(`Error: ${res.detail}`);
    }
};

async function loadPatients() {
    const res = await fetch(`${API_URL}/view`);
    const data = await res.json();

    list.innerHTML = data.map(p => `
        <div class="col-md-4">
            <div class="card shadow-sm mb-4">
                <div class="card-body">
                    <h5 class="card-title">${p.name} (${p.id})</h5>
                    <p class="card-text">
                        City: ${p.city}<br>
                        Age: ${p.age}<br>
                        Gender: ${p.gender}<br>
                        Height: ${p.height} m<br>
                        Weight: ${p.weight} kg<br>
                        <strong>BMI:</strong> ${p.bmi} (${p.verdict})
                    </p>
                    <button onclick="editPatient('${p.id}')" class="btn btn-primary btn-sm">Edit</button>
                    <button onclick="deletePatient('${p.id}')" class="btn btn-danger btn-sm ms-2">Delete</button>
                </div>
            </div>
        </div>
    `).join("");
}

async function deletePatient(id) {
    if (!confirm("Are you sure you want to delete this patient?")) return;
    const res = await fetch(`${API_URL}/delete/${id}`, { method: "DELETE" });
    const data = await res.json();
    alert(data.message);
    loadPatients();
}

async function editPatient(id) {
    const res = await fetch(`${API_URL}/patient/${id}`);
    const p = await res.json();

    document.getElementById("id").value = p.id;
    document.getElementById("name").value = p.name;
    document.getElementById("city").value = p.city;
    document.getElementById("age").value = p.age;
    document.getElementById("gender").value = p.gender;
    document.getElementById("height").value = p.height;
    document.getElementById("weight").value = p.weight;
}
