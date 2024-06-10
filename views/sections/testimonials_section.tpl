<section class="bg-unidBeige">
  <div class="width_standard mx-auto padding_y_standard space_y_standard">
    <div class="flex justify-center">
      <div
        class="lg:w-2/3 flex justify-center flex-col text-center gap-y-4 md:gap-y-6"
      >
        <h2>{{ frontpage_content["testimonials_section"]["header_text"] }}</h2>
        <p id="subheader">
          {{ frontpage_content["testimonials_section"]["subheader_text"] }}
        </p>
      </div>
    </div>
    <div class="flex flex-col md:flex-row gap-8 md:gap-10 lg:gap-16">
      <!-- prettier-ignore -->
      % include('components/testimonial_component')
    </div>
  </div>
</section>
