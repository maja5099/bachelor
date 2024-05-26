<section
  class="grid grid-cols-1 lg:grid-cols-3 xl:h-screen xl:min-w-screen bg-unidYellow bg-wave bg-cover overflow-clip"
>
  <div class="lg:col-span-2 flex flex-col items-center justify-center">
    <div
      class="space-y-6 justify-center flex flex-col mx-auto width_standard py-20 lg:py-16 xl:py-0"
    >
      <div class="space-y-10 lg:space-y-12">
        <div class="space-y-3 lg:space-y-6">
          <h1>Opret bruger</h1>
          <p id="subheader">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quae,
            voluptatum!
          </p>
        </div>
        <form class="grid lg:grid-cols-2 gap-x-14 gap-y-6 lg:gap-y-0">
          <div class="space-y-4 lg:space-y-6">
            <!-- FIRST NAME -->
            <!-- prettier-ignore -->
            % include('utilities/input_field', label_for=form_inputs['fname']['label_for'], form_label=form_inputs['fname']['text'], form_svg=form_inputs['fname']['icon'], type=form_inputs['fname']['type'], name=form_inputs['fname']['name'], inputmode=form_inputs['fname']['inputmode'], placeholder=form_inputs['fname']['placeholder'], form_info=form_inputs['fname']['form_info'])
            <!-- LAST NAME -->
            <!-- prettier-ignore -->
            % include('utilities/input_field', label_for=form_inputs['lname']['label_for'], form_label=form_inputs['lname']['text'], form_svg=form_inputs['lname']['icon'], type=form_inputs['lname']['type'], name=form_inputs['lname']['name'], inputmode=form_inputs['lname']['inputmode'], placeholder=form_inputs['lname']['placeholder'], form_info=form_inputs['lname']['form_info'])
            <!-- USERNAME -->
            <!-- prettier-ignore -->
            % include('utilities/input_field', label_for=form_inputs['username']['label_for'], form_label=form_inputs['username']['text'], form_svg=form_inputs['username']['icon'], type=form_inputs['username']['type'], name=form_inputs['username']['name'], inputmode=form_inputs['username']['inputmode'], placeholder=form_inputs['username']['placeholder'], form_info=form_inputs['username']['form_info'])
            <!-- PASSWORD -->
            <!-- prettier-ignore -->
            % include('utilities/password_field')
          </div>
          <div class="space-y-4 lg:space-y-6">
            <!-- EMAIL -->
            <!-- prettier-ignore -->
            % include('utilities/input_field', label_for=form_inputs['email']['label_for'], form_label=form_inputs['email']['text'], form_svg=form_inputs['email']['icon'], type=form_inputs['phone']['type'], name=form_inputs['email']['name'], inputmode=form_inputs['email']['inputmode'], placeholder=form_inputs['email']['placeholder'], form_info=form_inputs['email']['form_info'])
            <!-- PHONE -->
            <!-- prettier-ignore -->
            % include('utilities/input_field', label_for=form_inputs['phone']['label_for'], form_label=form_inputs['phone']['text'], form_svg=form_inputs['phone']['icon'], type=form_inputs['phone']['type'], name=form_inputs['phone']['name'], inputmode=form_inputs['phone']['inputmode'], placeholder=form_inputs['phone']['placeholder'], form_info=form_inputs['phone']['form_info'])
            <!-- WEBSITE NAME -->
            <!-- prettier-ignore -->
            % include('utilities/input_field', label_for=form_inputs['website_name']['label_for'], form_label=form_inputs['website_name']['text'], form_svg=form_inputs['website_name']['icon'], type=form_inputs['website_name']['type'], name=form_inputs['website_name']['name'], inputmode=form_inputs['website_name']['inputmode'], placeholder=form_inputs['website_name']['placeholder'], form_info=form_inputs['website_name']['form_info'])
            <!-- WEBSITE URL -->
            <!-- prettier-ignore -->
            % include('utilities/input_field', label_for=form_inputs['website_url']['label_for'], form_label=form_inputs['website_url']['text'], form_svg=form_inputs['website_url']['icon'], type=form_inputs['website_url']['type'], name=form_inputs['website_url']['name'], inputmode=form_inputs['website_url']['inputmode'], placeholder=form_inputs['website_url']['placeholder'], form_info=form_inputs['website_url']['form_info'])
          </div>
        </form>
      </div>
      <div
        class="flex pt-2 text-sm gap-4 text-unidLightBlue border-t border-unidLightBlue"
      >
        <div class="flex items-center h-5">
          <input type="checkbox" id="form_checkbox" class="w-4 h-4" required />
        </div>
        <div class="flex gap-1.5">
          <p>Jeg accepterer</p>
          <a
            href="#"
            class="group transition duration-300 cursor-pointer text-sm hover:scale-105 font-bold ease-in-out"
          >
            vilkår & betingelser
            <span
              class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-unidPurple"
            ></span>
          </a>
        </div>
      </div>
      <div
        class="lg:w-2/6 w-full pt-4 items-center mx-auto flex justify-center"
      >
        <!-- prettier-ignore -->
        % include('utilities/buttons/primary_button', type='submit', link='/', button_text='Opret bruger')
      </div>
    </div>
  </div>
  <div
    class="bg-unidLightBlue h-full w-full flex flex-col py-20 lg:py-0 justify-center mx-auto"
  >
    <img
      class="w-8/12 mx-auto"
      src="/assets/logos/{{unid_logo['primary_logo']}}"
      alt=""
    />
  </div>
</section>