
from django.shortcuts import render, redirect
from app.models import Patient

def BASE(request):
    return render(request, 'base.html')
def ADD_PATIENT(request):
    if request.method == "POST":
        patient_name = request.POST.get('patient_name')
        date_of_birth = request.POST.get('date_of_birth')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        # Use a different variable name for the instance of the Patient model
        patient_instance = Patient(
            patient_name=patient_name,
            date_of_birth=date_of_birth,
            age=age,
            phone=phone,
            email=email,
            gender=gender,
            address=address,
        )
        
        patient_instance.save()
        # Redirect after saving to avoid form resubmission
        return redirect('add_patient')  # Adjust the URL name if needed
    return render(request, 'Patient/add_patient.html')



