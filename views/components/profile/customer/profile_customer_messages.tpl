<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_messages"]["decorative_header_text"] }}
    </p>
    <h2>
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_messages"]["header_text"] }}
    </h2>
  </div>
  <div>
    <div id="content_box_styling">
      <div id="content_box_header_styling">
        <div
          class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
        >
          <div id="icon_medium" class="fill-unidPurple">
            % include(global_content['ui_icons']['message'])
          </div>
          <p id="content_box_header_text">
            <!-- prettier-ignore -->
            {{ profile_content["customer_specific_content"]["profile_customer_messages"]["box_header_text"] }}
          </p>
        </div>
      </div>
      <div class="flex flex-col gap-10 p-6 text-unidPurple">
        <form
          id="contactForm"
          enctype="multipart/form-data"
          class="space-y-8 w-full"
        >
          <div class="flex flex-col space-y-3 text-sm">
            <div class="space-y-1">
              <p id="form_label">Emne</p>
              <hr />
            </div>
            <div class="flex-col space-y-1.5 items-center">
              <label for="subject">
                <p>
                  Skriv emnet på, hvad vi kan hjælpe dig med, eller den opgave,
                  du vil have udført:
                </p>
              </label>
              <input
                class="form_input_no_icon"
                type="text"
                id="subject"
                name="subject"
                required
                placeholder="Skriv emnet her..."
              />
            </div>
          </div>
          <div class="flex flex-col space-y-3 text-sm">
            <div class="space-y-1">
              <p id="form_label">Besked</p>
              <hr />
            </div>
            <div class="flex-col space-y-1.5 items-center">
              <label for="message">
                <p>
                  Skriv hvad vi kan hjælpe dig med, eller hvilken opgave, vi
                  skal udføre for dig:
                </p>
              </label>
              <textarea
                class="form_input_no_icon"
                id="message"
                name="message"
                required
                placeholder="Skriv din besked her..."
              ></textarea>
            </div>
            <div class="flex items-center gap-2">
              <div id="icon_small">
                % include(global_content['ui_icons']['documents'])
              </div>
              <div class="gap-4 lg:flex space-y-1.5 lg:space-y-0 items-center">
                <label for="file">Upload fil:</label>
                <input
                  class="hover:cursor-pointer text-unidLightBlue gap-2 space-x-6 w-fit"
                  type="file"
                  id="file"
                  name="file"
                  accept=".png, .jpg, .jpeg"
                />
              </div>
            </div>
          </div>
        </form>
        <div class="mx-auto flex-col space-y-4">
          <div id="sendMessageButton" class="">
            <button type="button" id="primary_button">Send besked</button>
          </div>
          <p
            id="messageSent"
            style="display: none"
            class="text-unidLightBlue text-sm"
          ></p>
        </div>
      </div>
    </div>
  </div>
</div>
