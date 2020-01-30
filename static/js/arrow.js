function arrow(n) {
  var element = document.getElementById("productsTable");
  element.getElementsByTagName("TH")[n].classList.toggle("headerSortUp");
  element.getElementsByTagName("TH")[n].classList.toggle("headerSortDown");
} 