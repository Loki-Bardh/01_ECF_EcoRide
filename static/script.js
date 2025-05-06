document.addEventListener("DOMContentLoaded", () => {
    console.log("EcoRide JavaScript loaded!");
    // Example: Add interactivity here
});

// Toggle eco-friendly dark mode (save energy!)
document.getElementById('theme-toggle').addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
  });
  
  // CSS Add-on
  .dark-mode {
    background-color: #1A1A1A;
    color: #F0F0F0;
  }
  .dark-mode h1, .dark-mode h2 {
    color: var(--sage); /* Light green in dark mode */
  }
  