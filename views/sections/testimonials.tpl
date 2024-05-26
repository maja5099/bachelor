<section class="bg-unidBeige">
  <div
    class="width_standard mx-auto padding_y_standard space-y-8 md:space-y-10 lg:space-y-16"
  >
    <div class="flex justify-center">
      <div
        class="lg:w-2/3 flex justify-center flex-col text-center gap-y-4 md:gap-y-6"
      >
        <h2>{{section_testimonial_content['header_text']}}</h2>
        <p id="subheader">{{section_testimonial_content['subheader_text']}}</p>
      </div>
    </div>
    <div class="flex flex-col md:flex-row gap-8 md:gap-10 lg:gap-16">
      <!-- prettier-ignore -->
      % include('components/testimonial_box')
    </div>
  </div>
</section>
