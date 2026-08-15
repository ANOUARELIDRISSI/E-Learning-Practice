const form = document.querySelector("#ask-form");
const question = document.querySelector("#question");
const answer = document.querySelector("#answer");
const sources = document.querySelector("#sources");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const button = form.querySelector("button");
  button.disabled = true;
  answer.textContent = "Thinking through the documents...";
  sources.innerHTML = "";

  try {
    const response = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: question.value, top_k: 4 }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || "Request failed");
    }

    const data = await response.json();
    answer.textContent = data.answer;
    sources.innerHTML = data.sources
      .map(
        (source) => `
          <article class="source">
            <strong>${source.file} - score ${source.score.toFixed(3)}</strong>
            <span>${source.text}</span>
          </article>
        `
      )
      .join("");
  } catch (error) {
    answer.textContent = error.message;
  } finally {
    button.disabled = false;
  }
});

