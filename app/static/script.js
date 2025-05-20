document.addEventListener("DOMContentLoaded", () => {
  const authModal = document.getElementById("authModal");
  const closeAuthModal = document.getElementById("closeAuthModal");

  const showLoginBtn = document.getElementById("showLogin");
  const showRegisterBtn = document.getElementById("showRegister");

  const loginForm = document.getElementById("loginForm");
  const registerForm = document.getElementById("registerForm");

  // Show modal function with optional default form param
  function openModal(defaultForm = "login") {
    authModal.style.display = "block";
    if (defaultForm === "register") {
      showRegisterForm();
    } else {
      showLoginForm();
    }
  }

  // Close modal event
  closeAuthModal.onclick = () => {
    authModal.style.display = "none";
  };

  // Close modal if clicked outside the modal content
  window.onclick = (e) => {
    if (e.target == authModal) {
      authModal.style.display = "none";
    }
  };

  // Show login form and highlight button
  function showLoginForm() {
    loginForm.style.display = "block";
    registerForm.style.display = "none";
    showLoginBtn.classList.add("active");
    showRegisterBtn.classList.remove("active");
  }

  // Show register form and highlight button
  function showRegisterForm() {
    registerForm.style.display = "block";
    loginForm.style.display = "none";
    showRegisterBtn.classList.add("active");
    showLoginBtn.classList.remove("active");
  }

  // Button clicks to switch forms inside modal
  showLoginBtn.onclick = (e) => {
    e.preventDefault();
    showLoginForm();
  };

  showRegisterBtn.onclick = (e) => {
    e.preventDefault();
    showRegisterForm();
  };

  // Attach modal open to all elements with .show-auth-modal class
  document.querySelectorAll(".show-auth-modal").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      // Open register form if element has class .open-register else login
      if (btn.classList.contains("open-register")) {
        openModal("register");
      } else {
        openModal("login");
      }
    });
  });
});
