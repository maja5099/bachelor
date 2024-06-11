<div class="bg-unidYellow">
  <div class="width_standard padding_y_standard space-y-24 mx-auto">
    <div class="flex flex-col gap-y-6 md:gap-y-8">
      <div class="flex">
        <div class="space-y-2 md:w-1/2">
          <p id="decorative_header">
            {{ about_us_content["vision_section"]["decorative_header_text"] }}
          </p>
          <h2>{{ about_us_content["vision_section"]["header_text"] }}</h2>
        </div>
      </div>
      <div class="w-full gap-10 grid grid-cols-1 md:grid-cols-2">
        <div class="space-y-6">
          % for paragraph in about_us_content['vision_section']['paragraphs']:
          <div class="space-y-2">
            <p id="paragraph_title">{{ paragraph["title"] }}</p>
            <p id="paragraph_text">
              {{ paragraph["text"] }}
            </p>
          </div>
          % end
        </div>
        <div class="flex justify-center items-center">
          <!-- prettier-ignore -->
          <img
            class="h-auto w-3/4"
            src="/assets/illustrations/{{ about_us_content['vision_section']['illustration'] }}"
            alt="{{ about_us_content['vision_section']['illustration_alt'] }}"
          />
        </div>
      </div>
    </div>
  </div>
</div>
