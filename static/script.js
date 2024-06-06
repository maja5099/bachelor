// ##############################
//      TABLE OF CONTENTS
// PAGES
// - profile.html
// - signup.html
// - login.html
// - customer_messages.html
// - customer_clipcards.html
// - admin_messages.html
// - admin_clipcards.html
// COMPONENTS
// ELEMENTS
// SECTIONS
// UTILITIES
// - password_field.tpl

// ##############################
// PROFILE.HTML
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

      // Update URL with template name
      if (templateName) {
        updateURL(templateName);
        loadTemplate(templateName);
      } else {
        console.log("No template associated with this button.");
      }
    });
  });

  // First button selected by default
  if (buttons.length > 0) {
    buttons[0].classList.add("secondary_button_selected");
    const defaultTemplate = buttons[0].getAttribute("data-template");
    updateURL(defaultTemplate);
    loadTemplate(defaultTemplate);
  }

  // Update URL with template name
  function updateURL(templateName) {
    const newURL = `/profile/${templateName}`;
    window.history.pushState({ templateName }, "", newURL);
  }

  // Load templates dynamically
  function loadTemplate(templateName) {
    console.log(`Fetching template: ${templateName}`);
    fetch(`/profile/${templateName}`)
      .then((response) => {
        console.log(`Response status: ${response.status}`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.text();
      })
      .then((html) => {
        console.log(`Template loaded successfully`);
        document.getElementById("profile_content").innerHTML = html;
      })
      .catch((error) => console.error("Error loading template:", error));
  }

  // Add an event listener to handle back/forward navigation
  window.addEventListener("popstate", (event) => {
    if (event.state && event.state.templateName) {
      loadTemplate(event.state.templateName);
    }
  });

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
// CUSTOMER_MESSAGES.HTML
$(document).ready(function () {
  $("body").on("click", "#sendMessageButton", function () {
    console.log("Send button clicked");
    var formData = new FormData($("#contactForm")[0]);
    $.ajax({
      url: "/send_message",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        console.log("Success response:", response);
        $("#messageSent").text(response.info).show();
        $("#contactForm")[0].reset();
      },
      error: function (xhr) {
        console.error("Error response:", xhr);
        var response = JSON.parse(xhr.responseText);
        alert("Der opstod en fejl: " + response.info);
      },
    });
  });
});

// ##############################
// CUSTOMER_CLIPCARDS.HTML
document.addEventListener("DOMContentLoaded", function () {
  function buyClipcard(clipcardType, clipcardPrice) {
    window.location.href =
      "/buy_clipcard/" + clipcardType + "/" + clipcardPrice;
  }

  document.addEventListener("click", function (event) {
    if (event.target && event.target.classList.contains("buy-button")) {
      var clipcardType = event.target.getAttribute("data-clipcard-type");
      var clipcardPrice = event.target.getAttribute("data-clipcard-price");
      buyClipcard(clipcardType, clipcardPrice);
    }
  });
});

// ##############################
// ADMIN_MESSAGES.HTML
function deleteMessage(button) {
  var messageId = button.getAttribute("data-message-id");
  console.log("Delete button clicked");
  console.log("Message ID:", messageId);

  fetch("/delete_message", {
    method: "DELETE",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: "message_id=" + messageId,
  })
    .then((response) => {
      console.log("Response status:", response.status);
      return response.json();
    })
    .then((data) => {
      console.log("Response data:", data);
      if (data.info === "Message deleted.") {
        var messageDiv = button.closest("div");
        messageDiv.parentNode.removeChild(messageDiv);
        console.log("Message deleted successfully.");
      } else {
        alert(data.info);
        console.log("Error:", data.info);
      }
    })
    .catch((error) => {
      console.error("Fetch error:", error);
    });
}

// ##############################
// ADMIN_CLIPCARDS.HTML
document.addEventListener("click", function (event) {
  if (event.target.classList.contains("delete-button")) {
    var clipcardId = event.target.getAttribute("data-clipcard-id");
    deleteClipcard(clipcardId);
  }
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

$(document).ready(function () {
  $("body").on("click", "#submitTaskButton", function () {
    console.log("Button clicked");
    var formData = new FormData($("#taskForm")[0]);
    $.ajax({
      url: "/submit_task",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        console.log("Success response:", response);
        $("#taskSubmissionMessage").text(response.info).show();
        $("#taskForm")[0].reset();
      },
      error: function (xhr) {
        console.error("Error response:", xhr);
        var response = JSON.parse(xhr.responseText);
        alert("Der opstod en fejl: " + response.info);
      },
    });
  });
});

// ##############################
// PASSWORD_FIELD.TPL
$(document).ready(function () {
  $("#visibility_button").on("click", function () {
    var input = $("#password_input");
    var icons = $(".visibility_icon");
    input.attr("type", input.attr("type") === "password" ? "text" : "password");
    icons.toggleClass("object_hidden");
  });
});
