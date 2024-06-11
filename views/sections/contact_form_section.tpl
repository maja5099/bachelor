<div
          class="grid grid-cols-1 lg:grid-cols-2 gap-6 lg:gap-16 justify-center items-center"
        >
          <div class="w-2/3 flex items-center justify-center mx-auto">
            <img
              src="/assets/illustrations/{{ contact_content['illustration'] }}"
              alt="{{ contact_content['illustration_alt'] }}"
            />
          </div>
          <div
            class="bg-unidPink order-first lg:order-last mx-auto flex flex-col w-full p-10 space-y-8 rounded-lg"
          >
            <div class="space-y-4">
              <h3>{{ contact_content["contact_form_section"]["header_text"] }}</h3>
              <p>
                {{ contact_content["contact_form_section"]["subheader_text"] }}
              </p>
            </div>
            <div class="space-y-4">
              <!-- prettier-ignore -->
              % include('utilities/input_fields/default_input_field', label_for=global_content['form_inputs']['full_name']['label_for'], form_label=global_content['form_inputs']['full_name']['text'], form_svg=global_content['form_inputs']['full_name']['icon'], type=global_content['form_inputs']['full_name']['type'], name=global_content['form_inputs']['full_name']['name'], inputmode=global_content['form_inputs']['full_name']['inputmode'], placeholder=global_content['form_inputs']['full_name']['placeholder'], form_info=global_content['form_inputs']['full_name']['form_info'])
              % include('utilities/input_fields/default_input_field', label_for=global_content['form_inputs']['email']['label_for'], form_label=global_content['form_inputs']['email']['text'], form_svg=global_content['form_inputs']['email']['icon'], type=global_content['form_inputs']['email']['type'], name=global_content['form_inputs']['email']['name'], inputmode=global_content['form_inputs']['email']['inputmode'], placeholder=global_content['form_inputs']['email']['placeholder'], form_info=global_content['form_inputs']['email']['form_info'])
              <div>
                <!-- prettier-ignore -->
                % include('utilities/input_fields/message_input_field')
              </div>
            </div>
            <div class="mx-auto w-full md:w-fit lg:w-full xl:w-fit pt-6">
              <!-- prettier-ignore -->
              % include('utilities/buttons/primary_button', link='/', type='submit', button_text=contact_content["contact_form_section"]["button_text"])
            </div>
          </div>
        </div>