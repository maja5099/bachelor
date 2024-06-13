<label for="pwd" class="space-y-1.5 block">
  <div class="flex space-between justify-between">
    <p id="form_label">Adgangskode</p>
  </div>
  <div class="relative w-full">
    <div
      class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidLightBlue rounded-bl-md rounded-tl-md"
    >
      <div id="icon_small" class="fill-white text-white w-5 h-5">
        % include(global_content['ui_icons']['lock'])
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
    >
      <div
        id="icon_small"
        class="visibility_icon transition-transform ease-in-out hover:scale-110 duration-300"
      >
        % include(global_content['ui_icons']['eye_closed'])
      </div>
      <div
        id="icon_small"
        class="visibility_icon object_hidden transition-transform ease-in-out hover:scale-110 duration-300"
      >
        % include(global_content['ui_icons']['eye_open'])
      </div>
    </button>
  </div>
</label>
