<div class="space-y-8">
  <div class="space-y-2">
    <p class="text-md tracking-widest text-unidPurple">REGISTRERING</p>
    <h2>Timeregistrering</h2>
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
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              role="icon"
              aria-label="Stop watch icon"
            >
              <path
                fill="currentColor"
                d="M13 12.6V9q0-.425-.288-.712T12 8t-.712.288T11 9v3.975q0 .2.075.388t.225.337l2.8 2.8q.275.275.7.275t.7-.275t.275-.7t-.275-.7zM12 22q-1.875 0-3.512-.712t-2.85-1.925t-1.925-2.85T3 13t.713-3.512t1.924-2.85t2.85-1.925T12 4t3.513.713t2.85 1.925t1.925 2.85T21 13t-.712 3.513t-1.925 2.85t-2.85 1.925T12 22M2.05 7.3q-.275-.275-.275-.7t.275-.7L4.9 3.05q.275-.275.7-.275t.7.275t.275.7t-.275.7L3.45 7.3q-.275.275-.7.275t-.7-.275m19.9 0q-.275.275-.7.275t-.7-.275L17.7 4.45q-.275-.275-.275-.7t.275-.7t.7-.275t.7.275l2.85 2.85q.275.275.275.7t-.275.7M12 20q2.925 0 4.963-2.037T19 13t-2.037-4.962T12 6T7.038 8.038T5 13t2.038 4.963T12 20"
              />
            </svg>
          </div>
          <p class="font-bold text-lg">Timeregistrering</p>
        </div>
      </div>
      <div class="flex flex-col gap-10 p-6 text-unidPurple">
        <form id="taskForm" class="space-y-8 w-full">
          <div class="flex flex-col gap-2 text-sm">
            <div class="space-y-1">
              <h3 class="text-lg font-bold">Brugeroplysninger</h3>
              <hr />
            </div>
            <div class="">
              <div class="grid grid-cols-2 gap-2 items-center">
                <label for="customer">
                  <p class="font-semibold">Vælg kunde:</p>
                </label>
                <select
                  id="customer"
                  name="customer"
                  class="w-full py-2 px-5 rounded-md border border-unidLightBlue placeholder:text-unidLightBlue text-unidBlue transition ease-in-out duration-300 focus:ring-2 focus:ring-unidYellow focus:outline-none"
                  placeholder="Choose a customer…"
                >
                  % for customer in active_customers:
                  <option id="form_input" value="{{ customer['user_id'] }}">
                    {{ customer["first_name"] }} {{ customer["last_name"] }}
                  </option>
                  % end
                </select>
              </div>
            </div>
          </div>
          <div class="flex flex-col gap-2 text-sm">
            <div class="space-y-1">
              <h3 class="text-lg font-bold">Opgaveoplysninger</h3>
              <hr />
            </div>
            <div class="grid grid-cols-2 gap-2 items-center">
              <label for="title">
                <p class="font-semibold">Opgavetitel:</p>
              </label>
              <textarea
                class="w-full py-2 px-5 rounded-md border border-unidLightBlue placeholder:italic placeholder:text-unidLightBlue text-unidBlue transition ease-in-out duration-300"
                id="title"
                name="title"
                accept-charset="UTF-8"
                placeholder="Titel på udførte opgave"
              ></textarea>
            </div>
            <div class="grid grid-cols-2 gap-2 items-center">
              <label for="description">
                <p class="font-semibold">Opgavebeskrivelse:</p>
              </label>
              <textarea
                class="w-full py-2 px-5 rounded-md border border-unidLightBlue placeholder:italic placeholder:text-unidLightBlue text-unidBlue transition ease-in-out duration-300"
                id="description"
                name="description"
                accept-charset="UTF-8"
                placeholder="Beskrivelse af udførte opgave..."
              ></textarea>
            </div>
          </div>
          <div class="flex flex-col gap-2 text-sm">
            <div class="space-y-1">
              <h3 class="text-lg font-bold">Tid</h3>
              <hr />
            </div>
            <div class="grid md:grid-cols-2 space-y-2 items-center">
              <label for="hours">
                <p class="font-semibold">Tid brugt:</p>
              </label>
              <div class="flex justify-between w-fit md:justify-normal gap-4">
                <div class="flex items-center gap-2">
                  <input
                    class="w-full py-2 px-5 rounded-md border border-unidLightBlue placeholder:text-unidLightBlue text-unidBlue transition ease-in-out duration-300"
                    type="number"
                    id="hours"
                    name="hours"
                    min="0"
                    step="1"
                    placeholder="0"
                  />
                  <p>timer</p>
                </div>
                <div class="flex items-center gap-2">
                  <input
                    class="w-full py-2 px-5 rounded-md border border-unidLightBlue placeholder:text-unidLightBlue text-unidBlue transition ease-in-out duration-300"
                    type="number"
                    id="minutes"
                    name="minutes"
                    min="0"
                    max="59"
                    step="1"
                    placeholder="0"
                  />
                  <p>minutter</p>
                </div>
              </div>
            </div>
          </div>
        </form>
        <div id="submitTaskButton" class="md:w-1/3 mx-auto">
          <button type="button" id="primary_button">Registrer</button>
        </div>
        <div id="taskSubmissionMessage" style="display: none"></div>
      </div>
    </div>
  </div>
</div>
