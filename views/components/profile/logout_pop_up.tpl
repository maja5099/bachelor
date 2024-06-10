<div
  id="logout_popup"
  class="h-screen px-10 fixed flex justify-center items-center inset-0 z-50 backdrop-brightness-50 object_hidden"
>
  <div
    class="p-10 w-5/6 lg:w-3/6 space-y-10 relative mx-auto my-auto rounded-xl shadow-lg bg-unidLightPurple"
  >
    <div class="text-center gap-6 space-y-2 flex-auto justify-center">
      <h3>{{ profile_content["logout"]["header_text"] }}</h3>
      <p id="subheader">
        {{ profile_content["logout"]["subheader_text"] }}      
      </p>
    </div>
    <div class="md:flex space-y-4 md:space-y-0 gap-10 justify-center">
      <div id="close_logout_pop_up" class="w-full">
        <!-- prettier-ignore -->
        % include('utilities/buttons/secondary_button', type='button', link='/', button_text=profile_content["logout"]["button_texts"]["cancel"])
      </div>
      <div class="w-full">
        <form id="logout" method="POST" action="/logout">
          <!-- prettier-ignore -->
          % include('utilities/buttons/primary_button', type='submit', link='/', button_text=profile_content["logout"]["button_texts"]["proceed"])
        </form>
      </div>
    </div>
  </div>
</div>
