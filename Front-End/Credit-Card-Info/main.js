document.addEventListener("DOMContentLoaded", (event) => {
  const requiredInputs = document.querySelectorAll(".required");

  requiredInputs.forEach((item) => {
    const firstChild = item.children[0];
    const secondChild = item.children[1];
    let hasInput = false;

    firstChild.addEventListener("input", function () {
      if (this.value !== "") {
        hasInput = true;
        // Remove classes
        secondChild.classList.remove("required-text");
        this.classList.remove("required-input");
      } else if (hasInput) {
        // Add classes
        secondChild.classList.add("required-text");
        this.classList.add("required-input");
      }
    });
  });
});
