<label for="message" class="space-y-1.5 block">
  <div class="flex space-between justify-between">
    <p id="form_label">Besked</p>
  </div>
  <div class="relative w-full overflow-auto">
    <div
      class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidLightBlue h-full rounded-bl-md rounded-tl-md"
    >
      <div id="icon_small" class="fill-white text-white w-5 h-5">
        % include(global_content['ui_icons']['message'])
      </div>
    </div>
    <textarea
      id="form_input"
      class="-mb-1.5"
      type="message"
      name="message"
      inputmode="text"
      placeholder="Lorem ipsum dolor sit amet..."
      required
    ></textarea>
  </div>
</label>
