<div class="space-y-8">
  <div class="space-y-2">
    <p class="text-md tracking-widest text-unidPurple">BESKEDER</p>
    <h2>Indsendte beskeder</h2>
  </div>
  <div class="grid gap-8">
    <!-- prettier-ignore -->
    % if messages: 
      % for message in messages:
    <div>
      <div
        class="w-full h-full rounded-lg text-white justify-center items-center bg-unidYellow border-2 border-unidLightBlue"
      >
        <div
          class="bg-unidLightBlue text-center p-6 items-center space-y-1 lg:space-y-0 lg:flex justify-between"
        >
          <div
            class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
          >
            <div id="icon_medium" class="fill-unidPurple">
              % include(global_content['ui_icons']['education'])
            </div>
            <p class="font-bold text-lg">{{ message["message_subject"] }}</p>
          </div>
          <p>Sendt den: {{ message["formatted_created_at"] }}</p>
        </div>
        <div class="flex flex-col gap-8 p-6 text-unidPurple">
          <div class="space-y-8 text-sm">
            <div class="space-y-2 text-sm">
              <div class="space-y-1">
                <div
                  class="lg:flex space-y-1 lg:space-y-0 justify-between items-center"
                >
                  <div class="flex gap-2 items-center">
                    <h3 class="text-lg font-bold">Afsender:</h3>
                    <p class="text-base font-medium">
                      {{ message["first_name"] }} {{ message["last_name"] }}
                    </p>
                  </div>
                  <p class="font-medium">
                    {{ message["website_name"] }}:
                    {{ message["website_url"] }}
                  </p>
                </div>
                <hr />
              </div>
              <div class="space-y-2">
                <div class="flex gap-2">
                  <p class="font-semibold">Emne:</p>
                  <p>{{ message["message_subject"] }}</p>
                </div>
                <div class="lg:flex gap-2">
                  <p class="font-semibold">Besked:</p>
                  <p>{{ message["message_text"] }}</p>
                </div>
              </div>
            </div>
            <div class="w-full flex justify-between">
              <div>
                % if message['message_file']:
                <a
                  class="group transition duration-300 cursor-pointer text-unidLightBlue text-sm hover:scale-105 font-semibold ease-in-out"
                  href="{{ message['message_file'] }}"
                  target="_blank"
                >
                  <div class="flex gap-1.5">
                    <div id="icon_small">
                      % include(global_content['ui_icons']['documents'])
                    </div>
                    <div>
                      <p>Se vedhæftede filer</p>
                      <span
                        class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-unidPurple"
                      ></span>
                    </div>
                  </div>
                </a>
                % end
              </div>
              <div class="text-red-600">
                <div class="justify-end flex items-center">
                  <button
                    data-message-id="{{ message['message_id'] }}"
                    onclick="deleteMessage(this)"
                    type="button"
                    class="items-center flex gap-1.5 text-sm font-semibold"
                  >
                    <div id="icon_small">
                      % include(global_content['ui_icons']['trashcan'])
                    </div>
                    Slet
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- prettier-ignore -->
    % end 
      % else:
    <p>Ingen beskeder at vise.</p>
    % end
  </div>
</div>
