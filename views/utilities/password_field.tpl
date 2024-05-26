<label for="pwd" class="space-y-1.5 block">
  <div class="flex space-between justify-between">
    <p id="form_label">Adgangskode</p>
  </div>
  <div class="relative w-full">
    <div
      class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidLightBlue rounded-bl-md rounded-tl-md"
    >
      <div id="icon_small" class="fill-white text-white w-5 h-5">
        % include('assets/icons/lock.svg')
      </div>
    </div>
    <input
      class="toggle_input"
      id="password_input"
      type="password"
      name="password"
      inputmode="text"
      placeholder="••••••••"
      required
    />
    <button
      id="visibility_button"
      type="button"
      class="visibility_button flex items-center absolute inset-y-0 end-0 px-6 text-unidLightBlue"
      onclick="pwd_visibility_toggle()"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="visibility_icon w-4 h-4 transition-transform ease-in-out hover:scale-110 duration-300"
        width="32"
        height="32"
        viewBox="0 0 256 256"
      >
        <path
          fill="currentColor"
          d="M228 175a8 8 0 0 1-10.92-3l-19-33.2A123.23 123.23 0 0 1 162 155.46l5.87 35.22a8 8 0 0 1-6.58 9.21a8.4 8.4 0 0 1-1.29.11a8 8 0 0 1-7.88-6.69l-5.77-34.58a133.06 133.06 0 0 1-36.68 0l-5.77 34.58A8 8 0 0 1 96 200a8.4 8.4 0 0 1-1.32-.11a8 8 0 0 1-6.58-9.21l5.9-35.22a123.23 123.23 0 0 1-36.06-16.69L39 172a8 8 0 1 1-13.94-8l20-35a153.47 153.47 0 0 1-19.3-20a8 8 0 1 1 12.46-10c16.6 20.54 45.64 45 89.78 45s73.18-24.49 89.78-45a8 8 0 1 1 12.44 10a153.47 153.47 0 0 1-19.3 20l20 35a8 8 0 0 1-2.92 11"
        />
      </svg>
      <svg
        class="visibility_icon w-4 h-4 object_hidden transition-transform ease-in-out hover:scale-110 duration-300"
        xmlns="http://www.w3.org/2000/svg"
        width="32"
        height="32"
        viewBox="0 0 256 256"
      >
        <path
          fill="currentColor"
          d="M247.31 124.76c-.35-.79-8.82-19.58-27.65-38.41C194.57 61.26 162.88 48 128 48S61.43 61.26 36.34 86.35C17.51 105.18 9 124 8.69 124.76a8 8 0 0 0 0 6.5c.35.79 8.82 19.57 27.65 38.4C61.43 194.74 93.12 208 128 208s66.57-13.26 91.66-38.34c18.83-18.83 27.3-37.61 27.65-38.4a8 8 0 0 0 0-6.5M128 192c-30.78 0-57.67-11.19-79.93-33.25A133.47 133.47 0 0 1 25 128a133.33 133.33 0 0 1 23.07-30.75C70.33 75.19 97.22 64 128 64s57.67 11.19 79.93 33.25A133.46 133.46 0 0 1 231.05 128c-7.21 13.46-38.62 64-103.05 64m0-112a48 48 0 1 0 48 48a48.05 48.05 0 0 0-48-48m0 80a32 32 0 1 1 32-32a32 32 0 0 1-32 32"
        />
      </svg>
    </button>
  </div>
</label>
<script>
  document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("visibility_button");
    toggleButton.addEventListener("click", function () {
      const input = document.getElementById("password_input");
      const icons = document.querySelectorAll("#visibility_button .visibility_icon");

      // Toggle the type attribute
      input.type = input.type === "password" ? "text" : "password";

      // Toggle icon visibility
      icons.forEach((icon) => {
        icon.classList.toggle("object_hidden");
      });
    });
  });
</script>
