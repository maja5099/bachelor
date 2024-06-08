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
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                role="icon"
                aria-label="Education icon"
              >
                <path fill="currentColor" d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0
                1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2m-.4 4.25l-7.07
                4.42c-.32.2-.74.2-1.06 0L4.4 8.25a.85.85 0 1 1 .9-1.44L12
                11l6.7-4.19a.85.85 0 1 1 .9 1.44"/ />
              </svg>
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
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="20"
                      height="20"
                      viewBox="0 0 24 24"
                    >
                      <path
                        fill="currentColor"
                        d="M19 19H8q-.825 0-1.412-.587T6 17V3q0-.825.588-1.412T8 1h6.175q.4 0 .763.15t.637.425l4.85 4.85q.275.275.425.638t.15.762V17q0 .825-.587 1.413T19 19m0-11h-3.5q-.625 0-1.062-.437T14 6.5V3H8v14h11zM4 23q-.825 0-1.412-.587T2 21V8q0-.425.288-.712T3 7t.713.288T4 8v13h10q.425 0 .713.288T15 22t-.288.713T14 23zM8 3v5zv14z"
                      />
                    </svg>
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
                    <div class="w-5 h-auto">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                      >
                        <path
                          fill="currentColor"
                          d="M7 21q-.825 0-1.412-.587T5 19V6q-.425 0-.712-.288T4 5t.288-.712T5 4h4q0-.425.288-.712T10 3h4q.425 0 .713.288T15 4h4q.425 0 .713.288T20 5t-.288.713T19 6v13q0 .825-.587 1.413T17 21zM17 6H7v13h10zm-7 11q.425 0 .713-.288T11 16V9q0-.425-.288-.712T10 8t-.712.288T9 9v7q0 .425.288.713T10 17m4 0q.425 0 .713-.288T15 16V9q0-.425-.288-.712T14 8t-.712.288T13 9v7q0 .425.288.713T14 17M7 6v13z"
                        />
                      </svg>
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
