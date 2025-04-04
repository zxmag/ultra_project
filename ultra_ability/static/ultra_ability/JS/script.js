// Dynamically switch bewtween Hamburger icon and X icon by toggling the menu visibility ( "show") and icon state ( "active" )
const hamburger = document.getElementById('hamburger');
const menu = document.getElementById('menu');

hamburger.addEventListener('click', () => {
    menu.classList.toggle('show');
    hamburger.classList.toggle('active');

    // This is for Accessibility enhancement( for visually-impaired users)
    const isExpanded = hamburger.getAttribute("aria-expanded") === "true";
    hamburger.setAttribute("aria-expanded", !isExpanded);
    menu.hidden = isExpanded; // Show or hide the menu
    hamburger.setAttribute("aria-label", isExpanded ? "Open hamburger menu" : "Close hamburger menu");
});

