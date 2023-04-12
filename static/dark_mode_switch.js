(function() {
  let darkSwitch = document.getElementById("darkSwitch");
  if (darkSwitch) {
    darkSwitch.addEventListener("change", function(event) {
      resetTheme();
    });
    function initTheme() {
      let darkThemeSelected =
        localStorage.getItem("darkSwitch") !== null &&
        localStorage.getItem("darkSwitch") === "dark";
      darkSwitch.checked = darkThemeSelected;
      if (darkThemeSelected) {
        document.documentElement.setAttribute("data-bs-theme", "dark")
        document.getElementsByTagName('nav')[0].classList.toggle("navbar-dark bg-dark")

      }
      else {
        document.documentElement.removeAttribute("data-bs-theme")
        document.getElementsByTagName('nav')[0].classList.toggle("navbar-dark bg-dark")
      }

    }
    function resetTheme() {
      if (darkSwitch.checked) {
        document.documentElement.setAttribute("data-bs-theme", "dark");
        localStorage.setItem("darkSwitch", "dark");
        document.getElementsByTagName('nav')[0].classList.add("navbar-dark bg-dark")
      } else {
        document.documentElement.setAttribute("data-bs-theme", "light");
        localStorage.removeItem("darkSwitch");
        document.getElementsByTagName('nav')[0].classList.remove("navbar-dark bg-dark")
      }
    }
  }
})();