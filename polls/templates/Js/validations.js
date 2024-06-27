// Función de autoejecución para encapsular el código y evitar conflictos globales
(function () {
    'use strict';

    var form = document.getElementById('registrationForm');

    form.addEventListener('submit', function (event) {
        var username = document.getElementById('username').value;
        var firstName = document.getElementById('firstName').value;
        var lastName = document.getElementById('lastName').value;

        if (!isValidUsername(username)) {
            alert('El usuario debe contener al menos una letra y un número.');
            event.preventDefault();
            event.stopPropagation();
        }

        if (!isValidName(firstName) || !isValidName(lastName)) {
            alert('El primer nombre y los apellidos deben tener al menos 2 letras.');
            event.preventDefault();
            event.stopPropagation();
        }

    });

    function isValidUsername(username) {
        var containsLetter = /[a-zA-Z]/.test(username);
        var containsNumber = /\d/.test(username);
        return containsLetter && containsNumber;
    }

    function isValidName(name) {
        return /^[a-zA-Z]{2,}$/.test(name);
    }

})();

  