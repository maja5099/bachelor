<div class="space-y-8">
  <div class="space-y-2">
    <p class="text-md tracking-widest text-unidPurple">KLIPPEKORT</p>
    <h2>Aktive klippekort</h2>
  </div>
  <div class="grid lg:grid-cols-2 gap-8">
    % for clipcard in active_clipcards:
    <div id="clipcard_{{ clipcard['clipcard_id'] }}">
      <div
        class="w-full h-full rounded-lg text-white justify-center items-center bg-unidYellow border-2 border-unidLightBlue"
      >
        <div class="bg-unidLightBlue text-center p-6 items-center">
          <div
            class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
          >
            <div id="icon_medium" class="fill-unidPurple">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                role="icon"
                aria-label="Card icon"
              >
                <path
                  fill="currentColor"
                  d="M22 6v12q0 .825-.587 1.413T20 20H4q-.825 0-1.412-.587T2 18V6q0-.825.588-1.412T4 4h16q.825 0 1.413.588T22 6M4 8h16V6H4zm0 4v6h16v-6zm0 6V6z"
                />
              </svg>
            </div>
            <p class="font-bold text-lg">
              {{ clipcard["first_name"] }} {{ clipcard["last_name"] }}
            </p>
          </div>
        </div>
        <div class="flex flex-col gap-8 p-6 text-unidPurple">
          <!-- USER -->
          <div class="space-y-2 text-sm">
            <div class="space-y-1">
              <h3 class="text-lg font-bold">Brugeroplysninger</h3>
              <hr />
            </div>
            <div class="space-y-2">
              <div class="flex gap-2">
                <p class="font-semibold">Navn:</p>
                <p>{{ clipcard["first_name"] }} {{ clipcard["last_name"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Brugernavn:</p>
                <p>{{ clipcard["username"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Telefon:</p>
                <p>{{ clipcard["phone"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Email:</p>
                <p>{{ clipcard["email"] }}</p>
              </div>
            </div>
          </div>
          <!-- WEBSITE -->
          <div class="space-y-2 text-sm">
            <div class="space-y-1">
              <h3 class="text-lg font-bold">Website</h3>
              <hr />
            </div>
            <div class="space-y-2">
              <div class="flex gap-2">
                <p class="font-semibold">Navn:</p>
                <p>{{ clipcard["website_name"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">URL:</p>
                <p>{{ clipcard["website_url"] }}</p>
              </div>
            </div>
          </div>
          <!-- CLIPCARD -->
          <div class="space-y-2 text-sm">
            <div class="space-y-1">
              <h3 class="text-lg font-bold">Klippekortoplysninger</h3>
              <hr />
            </div>
            <div class="space-y-2">
              <div class="gap-2">
                <p class="font-semibold">Klippekort ID:</p>
                <p>{{ clipcard["clipcard_id"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Klippekorttype:</p>
                <p>{{ clipcard["clipcard_type_title"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Købt den:</p>
                <p>{{ clipcard["created_at"] }}</p>
              </div>
            </div>
          </div>
          <!-- TIME -->
          <div class="space-y-2 text-sm">
            <div class="space-y-1">
              <h3 class="text-lg font-bold">Timeoverblik</h3>
              <hr />
            </div>
            <div class="space-y-2">
              <div class="flex gap-2">
                <p class="font-semibold">Tid brugt:</p>
                <p>{{ clipcard["time_used_text"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Tid tilbage:</p>
                <p>{{ clipcard["remaining_time_text"] }}</p>
              </div>
            </div>
          </div>
          <div class="w-full text-red-600">
            <div class="justify-end flex items-center">
              <button
                type="button"
                class="delete-button items-center flex gap-1.5 text-sm font-semibold"
                data-clipcard-id="{{ clipcard['clipcard_id'] }}"
              >
                <div class="w-5 h-auto">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
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
    % end
  </div>
</div>
