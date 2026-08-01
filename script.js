const currentYear = new Date().getFullYear();
let currentYearTxt = document.getElementsByClassName('currentYear');

Array.from(currentYearTxt).forEach(e => e.textContent = currentYear);