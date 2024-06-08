<label for="{{ label_for }}" class="space-y-1.5 block">
  <div class="flex space-between justify-between">
    <p id="form_label">{{ form_label }}</p>
  </div>
  <div class="relative w-full">
    <div
      class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidLightBlue rounded-bl-md rounded-tl-md"
    >
      <div id="icon_small" class="fill-white text-white w-5 h-5">
        % include('assets/icons/' + form_svg)
      </div>
    </div>
    <div
      class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidLightBlue rounded-bl-md rounded-tl-md"
    >
      <div id="icon_small" class="fill-white text-white w-5 h-5">
        % include('assets/icons/' + form_svg)
      </div>
    </div>
    <input
      id="form_input"
      type="{{ type }}"
      name="{{ name }}"
      inputmode="{{ inputmode }}"
      placeholder="{{ placeholder }}"
      required
    />
  </div>
  % if form_info:
  <p class="flex items-center gap-2.5 font-sans text-xs text-unidPurple">
    <div id="icon_small">
      % include(global_content['ui_icons']['info'])
    </div>
    {{ form_info }}
  </p>
  % end
</label>
