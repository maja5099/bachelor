<div class="bg-unidYellow">
  <div class="width_standard padding_y_standard space-y-24 mx-auto">
    <div class="flex flex-col gap-y-6 md:gap-y-8">
      <div class="flex">
        <div class="space-y-2 md:w-1/2">
        <p class="text-md tracking-widest text-unidPurple">
          {{ about_us_content["section_vision"]["subheader"] }}
        </p>
        <h2>{{ about_us_content["section_vision"]["title"] }}</h2>
      </div>
      </div>
      <div class="w-full gap-10 grid grid-cols-1 md:grid-cols-2">
        <div class="space-y-6">
          <p class="text-lg font-medium">
            {{ about_us_content["section_vision"]["introduction"] }}
          </p>
          <p class="text-base">
            {{ about_us_content["section_vision"]["first_chapter_content"] }}
          </p>
          <p class="text-2xl font-saira font-semibold">
            {{ about_us_content["section_vision"]["second_chapter_title"] }}
          </p>
          <p class="text-base">
            {{ about_us_content["section_vision"]["second_chapter_content"] }}
          </p>
        </div>
        <div class="flex justify-center items-center">
          <!-- prettier-ignore -->
          <img
            class="h-auto w-3/4"
            src="/assets/illustrations/{{ about_us_content['section_vision']['illustration'] }}"
            alt="{{ about_us_content['section_vision']['illustration_alt'] }}"
          />
        </div>
      </div>
    </div>
  </div>
</div>
