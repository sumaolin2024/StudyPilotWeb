document.addEventListener("DOMContentLoaded", function () {
  const inputs = document.querySelectorAll("input[type=radio]");
  inputs.forEach((input) => {
    input.addEventListener("change", () => {
      input.closest("form")?.classList.add("answered");
    });
  });
});
