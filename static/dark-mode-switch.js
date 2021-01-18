const navbar = document.querySelector('.navbar');
const darkSwitch = document.getElementById('darkSwitch');
window.addEventListener('load', () => {
    if (darkSwitch) {
        initTheme();
        darkSwitch.addEventListener('change', () => {
            resetTheme();
        });
    }
});

/**
 * Summary: function that adds or removes the attribute 'data-theme' depending if
 * the switch is 'on' or 'off'.
 *
 * Description: initTheme is a function that uses localStorage from JavaScript DOM,
 * to store the value of the HTML switch. If the switch was already switched to
 * 'on' it will set an HTML attribute to the body named: 'data-theme' to a 'dark'
 * value. If it is the first time opening the page, or if the switch was off the
 * 'data-theme' attribute will not be set.
 * @return {void}
 */
function initTheme() {
    const darkThemeSelected =
        localStorage.getItem('darkSwitch') !== null &&
        localStorage.getItem('darkSwitch') === 'dark';
    darkSwitch.checked = darkThemeSelected;
    if (darkThemeSelected) {
        document.body.setAttribute('data-theme', 'dark');
        navbar.classList.remove('navbar-light');
        navbar.classList.add('navbar-dark');
    } else {
        document.body.removeAttribute('data-theme');
        navbar.classList.remove('navbar-dark');
        navbar.classList.add('navbar-light');
    }
}

/**
 * Summary: resetTheme checks if the switch is 'on' or 'off' and if it is toggled
 * on it will set the HTML attribute 'data-theme' to dark so the dark-theme CSS is
 * applied.
 * @return {void}
 */
function resetTheme() {
    if (darkSwitch.checked) {
        document.body.setAttribute('data-theme', 'dark');
        localStorage.setItem('darkSwitch', 'dark');
        navbar.classList.remove('navbar-light');
        navbar.classList.add('navbar-dark');
    } else {
        document.body.removeAttribute('data-theme');
        localStorage.removeItem('darkSwitch');
        navbar.classList.remove('navbar-dark');
        navbar.classList.add('navbar-light');
    }
}
