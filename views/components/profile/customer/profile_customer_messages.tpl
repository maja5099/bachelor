<div class="space-y-8">
  <div class="space-y-2">
    <p class="text-md tracking-widest text-unidPurple">
      {{ profile_content["customer_specific_content"]["profile_customer_messages"]["subheader_text"] }}
    </p>
    <h2>
      {{ profile_content["customer_specific_content"]["profile_customer_messages"]["header_text"] }}
    </h2>
  </div>
  <div>
    <div
      class="w-full h-full rounded-lg text-white justify-center items-center bg-unidYellow border-2 border-unidLightBlue"
    >
      <div class="bg-unidLightBlue text-center p-6 items-center">
        <div
          class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
        >
          <div id="icon_medium" class="fill-unidPurple">
            % include(global_content['ui_icons']['message'])
          </div>
          <p class="font-bold text-lg">
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
              <h3 class="text-lg font-bold">Emne</h3>
              <hr />
            </div>
            <div class="flex-col space-y-1.5 items-center">
              <label for="subject">
                <p class="">
                  Skriv emnet på, hvad vi kan hjælpe dig med, eller den opgave,
                  du vil have udført:
                </p>
              </label>
              <input
                class="w-full py-2 px-5 rounded-md border border-unidLightBlue placeholder:italic placeholder:text-unidLightBlue text-unidBlue transition ease-in-out duration-300"
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
              <h3 class="text-lg font-bold">Besked</h3>
              <hr />
            </div>
            <div class="flex-col space-y-1.5 items-center">
              <label for="message">
                <p class="">
                  Skriv hvad vi kan hjælpe dig med, eller hvilken opgave, vi
                  skal udføre for dig:
                </p>
              </label>
              <textarea
                class="w-full py-2 px-5 rounded-md border border-unidLightBlue placeholder:italic placeholder:text-unidLightBlue text-unidBlue transition ease-in-out duration-300"
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
