<div class="bg-unidPink">
  <div class="width_standard padding_y_standard space-y-24 mx-auto">
    <div
      class="gap-14 md:gap-10 grid grid-cols-1 xl:grid-cols-12 text-unidPurple"
    >
      <div class="grid col-span-1 xl:col-span-5">
        <div class="flex flex-col gap-y-6 md:gap-y-8">
          <div class="flex">
            <div class="space-y-2">
              <p id="decorative_header">
                {{ about_us_content["team_section"]["decorative_header_text"] }}
              </p>
              <h2>{{ about_us_content["team_section"]["header_text"] }}</h2>
            </div>
          </div>
          <div class="space-y-6">
            <p id="introduction_text">
              {{ about_us_content["team_section"]["introduction_text"] }}
            </p>
            % for paragraph in about_us_content['team_section']['paragraphs']:
            <div class="space-y-2">
              <p id="paragraph_title">{{ paragraph["title"] }}</p>
              <p id="paragraph_text">
                {{ paragraph["text"] }}
              </p>
            </div>
            % end
          </div>
        </div>
      </div>
      <div class="grid col-span-1 xl:col-span-7">
        <div class="flex items-center justify-center">
          <div class="grid gap-14 md:gap-10 md:grid-cols-2">
            <!-- prettier-ignore -->
            % include('components/employee_component', employees=about_us_content['team_section']['employees'])
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
