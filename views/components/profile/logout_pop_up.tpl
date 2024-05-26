<div
  id="logout_popup"
  class="w-screen h-screen fixed flex justify-center items-center inset-0 z-50 backdrop-brightness-50 object_hidden"
>
  <div
    class="max-w-xl p-10 space-y-10 relative mx-auto my-auto rounded-xl shadow-lg bg-unidLightPurple"
  >
    <div class="text-center gap-6 space-y-4 flex-auto justify-center">
      <h3>Er du sikker?</h3>
      <p id="subheader">
        Vil du virkelig logge ud? Du kan aldrig nogensinde logge ind igen.
      </p>
    </div>
    <div class="flex gap-10 justify-center">
      <div id="close_logout_pop_up" class="w-full">
        <!-- prettier-ignore -->
        % include('utilities/buttons/secondary_button', type='button', link='/', button_text='Anuller')
      </div>
      <div class="w-full">
        <form id="logout" method="POST" action="/logout">
          <!-- prettier-ignore -->
          % include('utilities/buttons/primary_button', type='submit', link='/', button_text='Log ud')
        </form>
      </div>
    </div>
  </div>
</div>
