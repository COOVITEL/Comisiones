// Obtén todos los elementos con la clase "nav-link"
var navLinks = document.getElementsByClassName("nav-link");

// Agrega un evento de escucha a cada elemento
for (var i = 0; i < navLinks.length; i++) {
  navLinks[i].addEventListener("click", function() {
    // Remueve la clase "active" de todos los elementos
    for (var j = 0; j < navLinks.length; j++) {
      navLinks[j].classList.remove("active");
    }
    // Agrega la clase "active" al elemento que fue clickeado
    this.classList.add("active");
    console.log("test")
  });
}
