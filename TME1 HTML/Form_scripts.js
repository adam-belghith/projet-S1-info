/*----------Exercice 5-------------*/

// fonction appelée lorsque le focus sort du champ de saisie de l'adresse mail
function checkEmail(email) {
  // Recherche d'un "@"
  var atPos = email.value.indexOf("@");
  // Recherche du dernier "."
  var lastDotPos = email.value.lastIndexOf(".");
  // Vérifier qu'il y a bien un "@" suivi d'un "." encadré par au moins un caractère
  if (
    atPos != -1 &&
    atPos < lastDotPos &&
    lastDotPos < email.value.length - 1 &&
    lastDotPos - atPos > 1
  ) {
    // Si la vérification réussie, mettre le texte en vert
    email.style.color = "green";
    return true;
  } else {
    // Si la vérification échoue, mettre le texte en rouge
    email.style.color = "red";
    return false;
  }
}

/*----------Exercice 6-------------*/

function etatNormal(email){
    email.style.color = "black";
}

/*----------Exercice 7-------------*/
// fonction appelée lorsque l'utilisateur valide la saisie du formulaire
function valider() {
  // Vérifier que les champs requis sont bien renseignés
  var champsRequis = document.getElementsByClassName("Required");
  for (let champ of champsRequis) {
    if (champ.value == "" && !checkEmail(champ.name)) {
      alert(champ.name + " requis");
      return;
    }
  }
  // Soumettre le formulaire au serveur
  document.formulaire.submit();
}