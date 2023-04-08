(function() {
  let darkSwitch = document.getElementById("darkSwitch");
  if (darkSwitch) {
    initTheme();
    darkSwitch.addEventListener("change", function(event) {
      resetTheme();
    });
    function initTheme() {
      let darkThemeSelected =
        localStorage.getItem("darkSwitch") !== null &&
        localStorage.getItem("darkSwitch") === "dark";
      darkSwitch.checked = darkThemeSelected;
      darkThemeSelected
        ? document.documentElement.setAttribute("data-bs-theme", "dark")
        : document.documentElement.removeAttribute("data-bs-theme");
    }
    function resetTheme() {
      if (darkSwitch.checked) {
        document.documentElement.setAttribute("data-bs-theme", "dark");
        localStorage.setItem("darkSwitch", "dark");
      } else {
        document.documentElement.setAttribute("data-bs-theme", "light");
        localStorage.removeItem("darkSwitch");
      }
    }
  }
})();