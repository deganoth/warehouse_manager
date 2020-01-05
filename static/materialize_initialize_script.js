$(document).ready(function() {
            $('.sidenav').sidenav();
            $('.collapsible').collapsible();
            $('.dropdown-trigger').dropdown();
        });

document.getElementById("matfix").addEventListener("click", function(e) {
            e.stopPropagation();
        });