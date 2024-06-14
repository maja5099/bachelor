<div class="bg-unidLightBlue text-white">
  <div class="width_standard padding_y_standard space-y-24 mx-auto">
    <div class="flex flex-col gap-y-14">
      <div class="flex md:justify-center text-center">
        <div
          class="space-y-2 flex flex-col items-center mx-auto justify-center"
        >
          <p class="text-white text-base tracking-widest uppercase">
            {{ about_us_content["skills_section"]["decorative_header_text"] }}
          </p>
          <h2 class="text-white">
            {{ about_us_content["skills_section"]["header_text"] }}
          </h2>
        </div>
      </div>
      <div
        class="w-full gap-10 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 text-center"
      >
        <!-- prettier-ignore -->
        % include('elements/skills_element', skills=about_us_content['skills_section']['skills'])
      </div>
    </div>
  </div>
</div>
