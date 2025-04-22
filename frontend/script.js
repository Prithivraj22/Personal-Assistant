const micBtn = document.getElementById("mic-btn");
const responseDiv = document.getElementById("response");

micBtn.addEventListener("click", async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  const mediaRecorder = new MediaRecorder(stream);
  const chunks = [];

  mediaRecorder.ondataavailable = e => chunks.push(e.data);
  mediaRecorder.onstop = async () => {
    const blob = new Blob(chunks, { type: 'audio/wav' });
    const formData = new FormData();
    formData.append("file", blob, "voice.wav");

    const res = await fetch("http://localhost:5000/speech-to-text", {
      method: "POST",
      body: formData
    });
    const { text } = await res.json();
    responseDiv.textContent = `You said: ${text}`;

    const mlRes = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });
    const mlData = await mlRes.json();
    responseDiv.textContent += `\n${mlData.response}`;
  };

  mediaRecorder.start();
  setTimeout(() => mediaRecorder.stop(), 4000); // record for 4 seconds
});
