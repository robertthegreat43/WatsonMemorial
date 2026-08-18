async function startRecording() {
    try {
        const response = await fetch('/api/start_recording/', {
            method: 'POST'
        });

        const data = await response.json();
        alert("Recording started: " + data.file);
    } catch (err) {
        console.error(err);
        alert("Error starting recording");
    }
}

async function stopRecording() {
    try {
        const response = await fetch('/api/stop_recording/', {
            method: 'POST'
        });

        const data = await response.json();
        alert("Recording stopped");
    } catch (err) {
        console.error(err);
        alert("Error stopping recording");
    }
}

async function listVideos() {
    try {
        const response = await fetch('/api/videos/');
        const data = await response.json();

        const container = document.getElementById("videoList");
        container.innerHTML = "";

        data.videos.forEach(filename => {
            const btn = document.createElement("button");
            btn.innerText = "Download " + filename;
            btn.onclick = () => downloadVideo(filename);
            container.appendChild(btn);
            container.appendChild(document.createElement("br"));
        });

    } catch (err) {
        console.error(err);
        alert("Error listing videos");
    }
}

function downloadVideo(filename) {
    window.location.href = '/api/download/' + filename;
}
