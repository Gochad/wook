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
      if (darkThemeSelected) {
        document.documentElement.setAttribute("data-bs-theme", "dark")
        let nav = document.getElementsByTagName('nav')
        nav.classList.add("navbar-dark bg-dark")
      }
      else {
        document.documentElement.removeAttribute("data-bs-theme");
        let nav = document.getElementsByTagName('nav')
        nav.classList.remove("navbar-dark bg-dark")
      }

    }
    function resetTheme() {
      if (darkSwitch.checked) {
        document.documentElement.setAttribute("data-bs-theme", "dark");
        localStorage.setItem("darkSwitch", "dark");
        let nav = document.getElementsByTagName('nav')
        nav.classList.add("navbar-dark bg-dark")
      } else {
        document.documentElement.setAttribute("data-bs-theme", "light");
        localStorage.removeItem("darkSwitch");
        let nav = document.getElementsByTagName('nav')
        nav.classList.remove("navbar-dark bg-dark")
      }
    }
  }
})();