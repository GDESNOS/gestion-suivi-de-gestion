var currentTab = 0;
showTab(currentTab);

function showTab(n) {
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";

  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }

  fixStepIndicator(n);
}

function nextPrev(n) {
  var x = document.getElementsByClassName("tab");

  if (n == 1 && !validateForm()) return false;

  x[currentTab].style.display = "none";
  currentTab = currentTab + n;

  if (currentTab >= x.length) {
    document.getElementById("regForm").submit();
    return false;
  }

  showTab(currentTab);
}

function validateForm() {
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");

  for (i = 0; i < y.length; i++) {
    // Modification : Ne pas vérifier si le champ est vide
    // Les champs ne sont pas obligatoires
    // Votre logique personnalisée de validation peut être ajoutée ici

    // On peut utiliser par exemple la condition suivante pour exclure les champs vides des vérifications :
    if (y[i].value.trim() === "") {
      continue;
    }

    // On peut ajouter des validations supplémentaires ici pour chaque champ si nécessaire

    // Si une validation échoue, ajouter la classe "invalid" au champ
    y[i].classList.remove("invalid");
  }

  document.getElementsByClassName("step")[currentTab].className += " finish";
  return valid;
}

function fixStepIndicator(n) {
  var i, x = document.getElementsByClassName("step");

  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }

  x[n].className += " active";
}

