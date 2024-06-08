<label for="{{ label_for }}" class="space-y-1.5 block">
  <div class="flex space-between justify-between">
    <p id="form_label">{{ form_label }}</p>
    <!-- SUCCES -->
    <!-- <svg
      xmlns="http://www.w3.org/2000/svg"
      width="20"
      height="20"
      viewBox="0 0 24 24"
    >
      <path
        fill="#22c55e"
        d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10s10-4.48 10-10S17.52 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8s8 3.59 8 8s-3.59 8-8 8m3.88-11.71L10 14.17l-1.88-1.88a.996.996 0 1 0-1.41 1.41l2.59 2.59c.39.39 1.02.39 1.41 0L17.3 9.7a.996.996 0 0 0 0-1.41c-.39-.39-1.03-.39-1.42 0"
      />
    </svg> -->
    <!-- ERROR -->
    <!-- <svg
      xmlns="http://www.w3.org/2000/svg"
      width="20"
      height="20"
      viewBox="0 0 24 24"
    >
      <path
        fill="#ef4444"
        d="M12 17q.425 0 .713-.288T13 16t-.288-.712T12 15t-.712.288T11 16t.288.713T12 17m0-4q.425 0 .713-.288T13 12V8q0-.425-.288-.712T12 7t-.712.288T11 8v4q0 .425.288.713T12 13m0 9q-2.075 0-3.9-.788t-3.175-2.137T2.788 15.9T2 12t.788-3.9t2.137-3.175T8.1 2.788T12 2t3.9.788t3.175 2.137T21.213 8.1T22 12t-.788 3.9t-2.137 3.175t-3.175 2.138T12 22m0-2q3.35 0 5.675-2.325T20 12t-2.325-5.675T12 4T6.325 6.325T4 12t2.325 5.675T12 20m0-8"
      />
    </svg> -->
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
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="15"
      height="15"
      viewBox="0 0 24 24"
    >
      <path
        fill="currentColor"
        d="M12 17q.425 0 .713-.288T13 16v-4q0-.425-.288-.712T12 11t-.712.288T11 12v4q0 .425.288.713T12 17m0-8q.425 0 .713-.288T13 8t-.288-.712T12 7t-.712.288T11 8t.288.713T12 9m0 13q-2.075 0-3.9-.788t-3.175-2.137T2.788 15.9T2 12t.788-3.9t2.137-3.175T8.1 2.788T12 2t3.9.788t3.175 2.137T21.213 8.1T22 12t-.788 3.9t-2.137 3.175t-3.175 2.138T12 22"
      />
    </svg>
    {{ form_info }}
  </p>
  % end
</label>
