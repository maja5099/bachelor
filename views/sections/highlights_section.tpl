<div class="flex flex-col gap-y-14">
  <div class="flex md:justify-end md:text-right">
    <div class="space-y-2 md:w-1/2">
      <p id="decorative_header">
        {{ about_us_content["highlights_section"]["decorative_header_text"] }}
      </p>
      <h2>{{ about_us_content["highlights_section"]["header_text"] }}</h2>
    </div>
  </div>
  <div
    class="w-full gap-10 grid md:grid-cols-2 lg:grid-cols-4 grid-cols-1 text-center"
  >
    <!-- prettier-ignore -->
    % include('elements/highlights_element', highlights=about_us_content['highlights_section']['highlights'])
  </div>
</div>
