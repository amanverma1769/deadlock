Deadlock Prevention & Detection Toolkit
A web-based application developed using Flask that allows users to:

Check for Safe States using the Banker's Algorithm.

Detect Deadlocks in resource allocation systems.

Visualize Resource Allocation Graphs for better understanding.

Features
Safe State Checker: Determine if the system is in a safe state and obtain the safe sequence.

Deadlock Detection: Identify processes involved in a deadlock situation.

Resource Allocation Graph: Visual representation of processes, resources, allocations, and requests.

 Technologies Used
Backend: Python, Flask

Frontend: HTML, Tailwind CSS, JavaScript

Visualization: NetworkX, Matplotlib

Others: NumPy

📁 Project Structure
cpp
Copy
Edit
├── app.py
├── logic.py
├── templates/
│   └── index.html
├── static/
│   └── graph.png
├── requirements.txt
└── README.md
app.py: Main Flask application.

logic.py: Contains core logic for safe state checking, deadlock detection, and graph drawing.

templates/index.html: Frontend interface.

static/graph.png: Generated resource allocation graph.

requirements.txt: Python dependencies.

README.md: Project documentation.

