% for employee in employees:
<div class="h-full space-y-2 flex flex-col items-center text-center">
  <img
    alt="{{ employee['image_alt'] }}"
    class="flex-shrink-0 h-56 w-56 object-cover rounded-full object-center mb-4"
    src="/assets/images/team/{{ employee['employee_image'] }}"
  />
  <div class="w-full space-y-6">
    <div class="space-y-3">
      <div class="space-y-1">
        <p class="text-base tracking-widest">{{ employee["employee_name"] }}</p>
        <h3>{{ employee["employee_job_title"] }}</h3>
      </div>
      <p class="mb-4">{{ employee["employee_information"] }}</p>
    </div>
  </div>
</div>
% end
