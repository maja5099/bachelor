<section class="bg-unidYellow bg-wave bg-cover">
  <div
    class="width_standard padding_y_standard mx-auto gap-16 lg:gap-20 flex lg:flex-row flex-col items-center"
  >
    <div
      class="lg:flex-grow lg:w-1/2 lg:gap-14 gap-10 flex flex-col lg:items-start lg:text-left items-center text-center"
    >
      <div class="lg:gap-6 gap-4 flex flex-col">
        <h1>{{ frontpage_content['hero_section']['header_text'] }}</h1>
        <p id="h1_subheader">
          {{ frontpage_content['hero_section']['subheader_text'] }}
        </p>
      </div>
      <!-- BUTTON -->
      <div class="w-fit">
        <!-- prettier-ignore -->
        % include('utilities/buttons/primary_button', type='button', link='/', button_text=frontpage_content["hero_section"]['button_text'])
      </div>
    </div>
    <div class="lg:max-w-lg lg:w-full md:w-2/3 w-5/6">
      <!-- prettier-ignore -->
      <img
        class="object-cover object-center"
        alt="hero"
        src="/assets/illustrations/{{frontpage_content['hero_section']['image']}}"
      />
    </div>
  </div>
</section>
