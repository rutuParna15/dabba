function validateForm() {
    let firstName = document.getElementById('firstName').value;
    let middleName = document.getElementById('middleName').value;
    let lastName = document.getElementById('lastName').value;
    let email = document.getElementById('email').value;
    let mobileNo = document.getElementById('mobileNo').value;
    let aadhaar = document.getElementById('aadhaar').value;
    let password = document.getElementById('password').value;
    let retypePassword = document.getElementById('retypePassword').value;

    let nameRegex = /^[a-zA-Z]+$/;
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    let mobileNoRegex = /^[0-9]{10}$/;
    let aadhaarRegex = /^[0-9]{12}$/;
    let passwordRegex = /^[a-zA-Z0-9!@#$%^&*]{8,16}$/;

    if (!nameRegex.test(firstName) || !nameRegex.test(middleName) || !nameRegex.test(lastName)) {
        alert('Invalid name. Only alphabets are allowed.');
        return false;
    }

    if (!emailRegex.test(email)) {
        alert('Invalid email format.');
        return false;
    }

    if (!mobileNoRegex.test(mobileNo)) {
        alert('Invalid mobile number. It should be a 10-digit number.');
        return false;
    }

    if (!aadhaarRegex.test(aadhaar)) {
        alert('Invalid Aadhaar number. It should be a 12-digit number.');
        return false;
    }

    if (!passwordRegex.test(password)) {
        alert('Password should be 8-16 characters long and include letters, numbers, and special characters.');
        return false;
    }

    if (password !== retypePassword) {
        alert('Passwords do not match.');
        return false;
    }

    alert('Form submitted successfully!');
    return true;
}
