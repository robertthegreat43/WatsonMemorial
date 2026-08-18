console.log("JS START");

function getCookie(name) {
    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");

        for (let cookie of cookies) {
            cookie = cookie.trim();

            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}

const csrftoken = getCookie("csrftoken");

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("chatForm");
    const input = document.getElementById("chat-input");
    const chatWindow = document.getElementById("chat-window");

    if (!form || !input || !chatWindow) {
        console.error("Chat form, input, or chat window was not found.");
        return;
    }

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const msg = input.value.trim();

        if (!msg) {
            return;
        }

        chatWindow.innerHTML += `<p><strong>You:</strong> ${msg}</p>`;
        input.value = "";

        const formData = new FormData();
        formData.append("message", msg);

        try {
            const response = await fetch("/api/biblechat/", {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken
                },
                body: formData
            });

            const data = await response.json();

            if (!response.ok) {
                chatWindow.innerHTML += `<p><strong>Pastor:</strong> Something went wrong.</p>`;
                console.error(data);
                return;
            }

            if (data.reply) {
                chatWindow.innerHTML += `<p><strong>Pastor:</strong><i> ${data.reply}</i></p>`;
            } else if (data.error) {
                chatWindow.innerHTML += `<p><strong>Pastor:</strong> ${data.error}</p>`;
            } else {
                chatWindow.innerHTML += `<p><strong>Pastor:</strong> No reply was returned.</p>`;
            }

            chatWindow.scrollTop = chatWindow.scrollHeight;

        } catch (error) {
            console.error(error);
            chatWindow.innerHTML += `<p><strong>AI:</strong> Could not connect to the server.</p>`;
        }
    });
});