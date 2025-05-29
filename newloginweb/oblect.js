function sendOTP() {
    let mobile = document.getElementById("mobile").value;
    if(mobile.length == 10) {
        alert("OTP Sent to " + mobile);
    } else {
        alert("Enter a valid 10-digit mobile number");
    }
}