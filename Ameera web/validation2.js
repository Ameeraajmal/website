function validateForm() {
    var firstName = document.getElementById("first_name").value;
    var lastName = document.getElementById("last_name").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm_password").value;
    var gender = document.querySelector('input[name="gender"]:checked');
    var country = document.getElementById("country").value;
    var hobbies = document.querySelectorAll('input[name="hobbies"]:checked');

    if (firstName === "" || lastName === "" || email === "" || password === "" || confirmPassword === "" || !gender || country === "" || hobbies.length === 0) {
        alert("Please fill out all the required fields and select at least one hobby.");
        return false;
    }

    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }
}
