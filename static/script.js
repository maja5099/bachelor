document.addEventListener("DOMContentLoaded", function () {
  // Button style and dynamic templates
  const buttons = document.querySelectorAll(".secondary_button");

  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      buttons.forEach((btn) =>
        btn.classList.remove("secondary_button_selected")
      );
      this.classList.add("secondary_button_selected");
      const templateName = this.getAttribute("data-template");

      // Handles menu item with no template
      if (templateName) {
        loadTemplate(templateName);
      } else {
        console.log("No template associated with this button.");
      }
    });
  });

  // First button selected by default
  if (buttons.length > 0) {
    buttons[0].classList.add("secondary_button_selected");
    loadTemplate(buttons[0].getAttribute("data-template"));
  }

  // Load templates dynamically
  function loadTemplate(templateName) {
    fetch(`/profile/${templateName}`)
      .then((response) => response.text())
      .then((html) => {
        document.getElementById("profile_content").innerHTML = html;
      })
      .catch((error) => console.error("Error loading template:", error));
  }

  // Toggle pop up
  const togglePopup = () => {
    const popup = document.getElementById("logout_popup");
    if (popup) popup.classList.toggle("object_hidden");
  };

  // Open pop up button
  const openButton = document.getElementById("open_logout_pop_up");
  if (openButton) {
    openButton.addEventListener("click", function () {
      const popup = document.getElementById("logout_popup");
      if (popup) popup.classList.remove("object_hidden");
    });
  }

  // Close pop up button
  const closeButton = document.getElementById("close_logout_pop_up");
  if (closeButton) {
    closeButton.addEventListener("click", function () {
      const popup = document.getElementById("logout_popup");
      if (popup) popup.classList.add("object_hidden");
    });
  }
});

// ##############################
// SIGNUP.HTML
async function signUp() {
  const first_name = document.querySelector("input[name='first_name']").value;
  const last_name = document.querySelector("input[name='last_name']").value;
  const email = document.querySelector("input[name='email']").value;
  const phone = document.querySelector("input[name='phone']").value;
  const username = document.querySelector("input[name='username']").value;
  const password = document.querySelector("input[name='password']").value;
  const website_name = document.querySelector(
    "input[name='website_name']"
  ).value;
  const website_url = document.querySelector("input[name='website_url']").value;
  console.log("this is the username", username);

  const formData = new FormData();

  formData.append("first_name", first_name);
  formData.append("last_name", last_name);
  formData.append("email", email);
  formData.append("phone", phone);
  formData.append("username", username);
  formData.append("password", password);
  formData.append("website_name", website_name);
  formData.append("website_url", website_url);

  for (const value of formData.values()) {
    console.log(value);
  }

  const response = await fetch("/signup", {
    method: "POST",
    body: formData,
  });
  const data = await response.json();
  console.log("This is the right username", username);
  console.log("This is the data", data);
}

// ##############################
// LOGIN.HTML
async function login(event) {
  event.preventDefault();
  const username = document.querySelector("input[name='username']").value;
  const password = document.querySelector("input[name='password']").value;

  const formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);

  const response = await fetch("/login", {
    method: "POST",
    body: formData,
  });
  const data = await response.json();

  if (data.error) {
    document.getElementById("error_message").innerText = data.error;
    document.getElementById("form_input_error_message").style.display = "flex";
  } else {
    console.log("Login successful");
    window.location.href = "/";
  }
}

// ##############################
// MESSAGES.HTML
$(document).ready(function () {
  $("#sendMessageButton").click(function () {
    var formData = new FormData($("#contactForm")[0]);
    $.ajax({
      url: "/send_message",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        $("#messageSent").text(response.info).show();
        $("#contactForm")[0].reset();
      },
      error: function (xhr, status, error) {
        var response = JSON.parse(xhr.responseText);
        alert("Der opstod en fejl: " + response.info);
      },
    });
  });
});

// ##############################
// CUSTOMER_CLIPCARDS.HTML
function buyClipcard(clipcardType, clipcardPrice) {
  window.location.href = "/buy_clipcard/" + clipcardType + "/" + clipcardPrice;
}

document.querySelectorAll(".buy-button").forEach((button) => {
  button.addEventListener("click", function () {
    var clipcardType = this.getAttribute("data-clipcard-type");
    var clipcardPrice = this.getAttribute("data-clipcard-price");
    buyClipcard(clipcardType, clipcardPrice);
  });
});

// ##############################
// ADMIN_MESSAGES.HTML
function deleteMessage(button) {
  var messageId = button.getAttribute("data-message-id");
  fetch("/delete_message", {
    method: "DELETE",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: "message_id=" + messageId,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.info === "Message deleted.") {
        var messageDiv = button.closest("div");
        messageDiv.parentNode.removeChild(messageDiv);
      } else {
        alert(data.info);
      }
    })
    .catch((error) => console.error("Error:", error));
}

// ##############################
// ADMIN_CLIPCARDS.HTML
document.querySelectorAll(".delete-button").forEach((button) => {
  button.addEventListener("click", function () {
    var clipcardId = this.getAttribute("data-clipcard-id");
    deleteClipcard(clipcardId);
  });
});

function deleteClipcard(clipcardId) {
  fetch("/delete_clipcard/" + clipcardId, {
    method: "DELETE",
  })
    .then((response) => {
      if (response.ok) {
        var clipcardElement = document.getElementById("clipcard_" + clipcardId);
        if (clipcardElement) {
          clipcardElement.remove();
        }
      } else {
        throw new Error("Kunne ikke slette klippekortet.");
      }
    })
    .catch((error) => {
      console.error("Fejl:", error);
      alert("Der opstod en fejl ved sletning af klippekortet.");
    });
}

document.addEventListener("DOMContentLoaded", function () {
  const taskForm = document.getElementById("taskForm");
  if (taskForm) {
    taskForm.addEventListener("submit", function (event) {
      event.preventDefault();

      const form = event.target;
      const formData = new FormData(form);

      fetch("/submit_task", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          const responseMessage = document.getElementById("responseMessage");
          if (data.info) {
            responseMessage.textContent = data.info;
          } else {
            responseMessage.textContent = "Opgaven er blevet registreret.";
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          document.getElementById("responseMessage").textContent =
            "Der opstod en fejl.";
        });
    });
  }
});

// ##############################
// PASSWORD_FIELD.TPL
function pwd_visibility_toggle() {
  var input = document.getElementById("password_input");
  var icons = document.querySelectorAll("#visibility_button .visibility_icon");
  input.type = input.type === "password" ? "text" : "password";
  icons.forEach(function (icon) {
    icon.classList.toggle("object_hidden");
  });
}

document.addEventListener("DOMContentLoaded", function () {
  var visibilityButton = document.getElementById("visibility_button");
  if (visibilityButton) {
    visibilityButton.addEventListener("click", pwd_visibility_toggle);
  }
});
