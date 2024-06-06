<body>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="/static/script.js"></script>

  <div class="space-y-8">
    <div class="space-y-2">
      <p class="text-md tracking-widest text-unidPurple">BESKEDER</p>
      <h2>Skriv til os her</h2>
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
                aria-label="Education icon"
              >
                <path
                  fill="currentColor"
                  d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0
                1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2m-.4 4.25l-7.07
                4.42c-.32.2-.74.2-1.06 0L4.4 8.25a.85.85 0 1 1 .9-1.44L12
                11l6.7-4.19a.85.85 0 1 1 .9 1.44"
                />
              </svg>
            </div>
            <p class="font-bold text-lg">Send en besked</p>
          </div>
        </div>
        <div class="flex flex-col gap-10 p-6 text-unidPurple">
          <!-- USER -->
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
                    Skriv emnet på, hvad vi kan hjælpe dig med, eller den
                    opgave, du vil have udført:
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
              <div class="flex items-center gap-3">
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
</body>
