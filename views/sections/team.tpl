<div class="bg-unidPink">
  <div class="width_standard padding_y_standard space-y-24 mx-auto">
    <div
      class="gap-14 md:gap-10 grid grid-cols-1 xl:grid-cols-12 text-unidPurple"
    >
      <div class="grid col-span-1 xl:col-span-5">
        <div class="flex flex-col gap-y-6 md:gap-y-8">
          <div class="flex">
            <div class="space-y-2">
              <p class="text-md tracking-widest text-unidPurple">
                {{ about_us_content["section_team"]["subheader"] }}
              </p>
              <h2>{{ about_us_content["section_team"]["title"] }}</h2>
            </div>
          </div>
          <div class="space-y-6">
            <p class="text-lg font-medium">
              {{ about_us_content["section_team"]["introduction"] }}
            </p>
            <p class="text-base">
              {{ about_us_content["section_team"]["text"] }}
            </p>
          </div>
        </div>
      </div>
      <div class="grid col-span-1 xl:col-span-7">
        <div class="flex items-center justify-center">
          <div class="grid gap-14 md:gap-10 md:grid-cols-2">
            <!-- prettier-ignore -->
            % include('components/employee_box', employees=about_us_content['section_team']['employees'])
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
