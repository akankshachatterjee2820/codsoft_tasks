function checkAnswer(answer) {

    const result = document.getElementById("result");

    if (answer === "verify") {

        result.textContent =
            "Correct! Verify the request through a trusted channel.";

    } else {

        result.textContent =
            "Not recommended. Do not click suspicious links immediately.";
    }
}