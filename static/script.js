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
  // Retrieve user input values from the signup form
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

  // Create a FormData object to store form data and append user input values to the FormData object
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

  try {
    // Send a POST request to the server with the form data
    const response = await fetch("/signup", {
      method: "POST",
      body: formData,
    });

    // Log status and headers
    console.log("Response status:", response.status);
    console.log("Response headers:", response.headers);

    // Log the raw response text to see what the server returned
    const text = await response.text();
    console.log("Raw response:", text);

    // Parse the response JSON data
    const data = JSON.parse(text);

    // If the response contains an error, display it on the signup form
    if (data.error) {
      document.getElementById("error_message").innerText = data.error;
      document.getElementById("form_input_error_message").style.display =
        "flex";
    } else {
      // If signup is successful, log a success message and redirect to the homepage
      console.log("Signup successful");
      window.location.href = "/";
    }
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("error_message").innerText =
      "An unexpected error occurred.";
    document.getElementById("form_input_error_message").style.display = "flex";
  }
}

// ##############################
// LOGIN.HTML

// Handles form submission and processing for user login.
async function login(event) {
  event.preventDefault();
  // Retrieves the username and password entered by the user
  const username = document.querySelector("input[name='username']").value;
  const password = document.querySelector("input[name='password']").value;

  // Creates a FormData object and appends the username and password to it
  const formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);

  // Sends a POST request to the server with the login credentials
  const response = await fetch("/login", {
    method: "POST",
    body: formData,
  });

  // Parses the response JSON data
  const data = await response.json();

  // If the response contains an error, display it on the login form
  if (data.error) {
    document.getElementById("error_message").innerText = data.error;
    document.getElementById("form_input_error_message").style.display = "flex";
    // If login is successful, log a success message and redirect to the homepage
  } else {
    console.log("Login successful");
    window.location.href = "/";
  }
}

// ##############################
// CUSTOMER_MESSAGES.HTML

// Manages sending messages from the customer side.
$(document).ready(function () {
  // Attaches a click event handler
  $("body").on("click", "#sendMessageButton", function () {
    console.log("Send button clicked");

    // Retrieves form data from the contact form
    var formData = new FormData($("#contactForm")[0]);

    // Sends an AJAX request to the server to send the messag
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
      // Callback function executed when the request fails
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

// Handles buying clipcards by customers.
document.addEventListener("DOMContentLoaded", function () {
  // Redirects the user to the appropriate URL to buy the clipcard
  function buyClipcard(clipcardType, clipcardPrice) {
    window.location.href =
      "/buy_clipcard/" + clipcardType + "/" + clipcardPrice;
  }

  // Event listener for click events and checks if the clicked element has the right class
  document.addEventListener("click", function (event) {
    if (event.target && event.target.classList.contains("buy-button")) {
      // Retrieves the clipcard type and price from the clicked button's data attributes
      var clipcardType = event.target.getAttribute("data-clipcard-type");
      var clipcardPrice = event.target.getAttribute("data-clipcard-price");
      // Initiates the purchase process by calling the buyClipcard function
      buyClipcard(clipcardType, clipcardPrice);
    }
  });
});

// ##############################
// ADMIN_MESSAGES.HTML

// Handles deleting messages from the admin interface.
function deleteMessage(button) {
  // Retrieve the message ID from the button's data attribute
  var messageId = button.getAttribute("data-message-id");
  console.log("Delete button clicked");
  console.log("Message ID:", messageId);

  // Send a DELETE request to the server to delete the message
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
      // If the message was successfully deleted, remove it from the DOM
      if (data.info === "Message deleted.") {
        var messageDiv = button.closest("div");
        messageDiv.parentNode.removeChild(messageDiv);
        console.log("Message deleted successfully.");
        // If an error occurred, display an alert with the error message
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

// Handles deleting clipcards from the admin interface.
document.addEventListener("click", function (event) {
  if (event.target.classList.contains("delete-button")) {
    // Retrieve the clipcard ID from the data-clipcard-id attribute of the clicked button
    var clipcardId = event.target.getAttribute("data-clipcard-id");
    deleteClipcard(clipcardId);
  }
});

// Send a DELETE request to the server to delete the clipcard
function deleteClipcard(clipcardId) {
  fetch("/delete_clipcard/" + clipcardId, {
    method: "DELETE",
  })
    .then((response) => {
      if (response.ok) {
        // Find the clipcard element in the DOM and remove it
        var clipcardElement = document.getElementById("clipcard_" + clipcardId);
        if (clipcardElement) {
          clipcardElement.remove();
        }
      } else {
        // If the request fails, throw an error
        throw new Error("Kunne ikke slette klippekortet.");
      }
    })
    .catch((error) => {
      console.error("Fejl:", error);
      alert("Der opstod en fejl ved sletning af klippekortet.");
    });
}

// Handles form submission for tasks
$(document).ready(function () {
  $("body").on("click", "#submitTaskButton", function () {
    console.log("Button clicked");
    // Retrieve form data
    var formData = new FormData($("#taskForm")[0]);
    // Send an AJAX request to submit the task
    $.ajax({
      url: "/submit_task",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // Log and display success message
        console.log("Success response:", response);
        $("#taskSubmissionMessage").text(response.info).show();
        $("#taskForm")[0].reset();
      },
      error: function (xhr) {
        // Log and display error message if there's an error in the request
        console.error("Error response:", xhr);
        var response = JSON.parse(xhr.responseText);
        alert("Der opstod en fejl: " + response.info);
      },
    });
  });
});

// ##############################
// PASSWORD_FIELD.TPL

// Manages the visibility toggle for password fields.
$(document).ready(function () {
  // Attach a click event handler
  $("#visibility_button").on("click", function () {
    // Retrieve the password input field and visibility icons
    var input = $("#password_input");
    var icons = $(".visibility_icon");
    // Toggle the visibility of the password input field between text and password
    input.attr("type", input.attr("type") === "password" ? "text" : "password");
    // Toggle the visibility of visibility icons
    icons.toggleClass("object_hidden");
  });
});
