<div class="flex flex-col gap-y-6 md:gap-y-8">
    <div
      class="w-full gap-10 grid items-center grid-cols-1 md:grid-cols-2"
    >
      <div class="flex flex-col gap-y-6 md:gap-y-8">
        <div class="space-y-2">
          <p class="text-md tracking-widest text-unidPurple">{{ services_and_prices_content["services_section"]["subheader_text"] }}</p>
          <h2>{{ services_and_prices_content["services_section"]["header_text"] }}</h2>
        </div>
        <div class="space-y-6">
          % for paragraph in services_and_prices_content['services_section']['paragraphs']:
          <div class="space-y-2">
            <p class="text-2xl font-saira font-semibold">{{ paragraph["title"] }}</p>
            <p class="text-base">
              {{ paragraph["text"] }}
            </p>
          </div>
          % end
        </div>
      </div>
      <div class="flex justify-center items-center">
        <!-- prettier-ignore -->
        <img
          class="h-auto w-3/4"
          src="/assets/illustrations/{{ services_and_prices_content['services_section']['illustration'] }}"
          alt="{{ services_and_prices_content['services_section']['illustration_alt'] }}"
        />
      </div>
    </div>
  </div>