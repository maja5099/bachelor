<div class="flex flex-col gap-y-14">
  <div class="flex md:justify-end md:text-right">
    <div class="space-y-2 md:w-1/2">
      <p class="text-md tracking-widest text-unidPurple">
        {{ about_us_content["section_highlights"]["subheader"] }}
      </p>
      <h2>{{ about_us_content["section_highlights"]["title"] }}</h2>
    </div>
  </div>
  <div
    class="w-full gap-10 grid md:grid-cols-2 lg:grid-cols-4 grid-cols-1 text-center"
  >
    <!-- prettier-ignore -->
    % include('components/highlight_component', highlights=about_us_content['section_highlights']['highlights'])
  </div>
</div>
