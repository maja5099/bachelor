<div class="bg-unidPink">
  <div
    class="width_standard padding_y_standard space_y_standard space-y-24 mx-auto"
  >
    <div class="flex flex-col gap-y-6 md:gap-y-8">
      <div class="flex md:justify-center text-center">
        <div
          class="space-y-2 flex flex-col items-center mx-auto justify-center"
        >
          <p id="decorative_header">
            <!-- prettier-ignore -->
            {{services_and_prices_content["prices_section"]["decorative_header_text"]}}
          </p>
          <h2>
            <!-- prettier-ignore -->
            {{services_and_prices_content["prices_section"]["header_text"]}}
          </h2>
        </div>
      </div>
      <div
        class="grid md:grid-cols-2 xl:grid-cols-3 grid-cols-1 justify-center items-end gap-10"
      >
        <!-- prettier-ignore -->
        % include('components/pricing_default_component')
        % include('components/pricing_default_component')
        % include('components/pricing_accent_component')
      </div>
      <div class="flex justify-center text-center">
        <p class="italic text-sm">
          Du skal være logget ind, for at købe et klippekort
        </p>
      </div>
    </div>
  </div>
</div>
