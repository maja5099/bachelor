<div class="bg-unidLightBlue text-white">
  <div class="width_standard padding_y_standard space-y-24 mx-auto">
    <div class="flex flex-col gap-y-14">
      <div class="flex md:justify-center text-center">
        <div
          class="space-y-2 flex flex-col items-center mx-auto justify-center"
        >
          <p class="text-md md:w-1/2 tracking-widest">
            {{ about_us_content["section_skills"]["subheader"] }}
          </p>
          <h2 class="text-white">
            {{ about_us_content["section_skills"]["title"] }}
          </h2>
        </div>
      </div>
      <div
        class="w-full gap-10 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 text-center"
      >
        <!-- prettier-ignore -->
        % include('components/skill_component', skills=about_us_content['section_skills']['skills'])
      </div>
    </div>
  </div>
</div>
