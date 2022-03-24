from django.shortcuts import render, redirect, HttpResponse
from . import models

userDoc = ''
userPat = ''
userId = ''

def signup_login(request):
    global userId,userPat,userDoc
    if request.method == 'POST':
        user = request.POST.get('user')
        print(user)
        if user == 'Signup-Patient':
            if request.method == 'POST':
                fname = request.POST.get('fname')
                lname = request.POST.get('lname')
                uname = request.POST.get('uname')
                proimg = request.FILES.get('proimg')
                eid = request.POST.get('eid')
                pass1 = request.POST.get('pass1')
                pass2 = request.POST.get('pass2')
                address = request.POST.get('address')
                city = request.POST.get('city')
                state = request.POST.get('state')
                pcode = request.POST.get('pcode')

                ins = models.Patient(firstname=fname,
                                     lastname=lname,
                                     Username=uname,
                                     password=pass1,
                                     confirmPassword=pass2,
                                     address=address,
                                     city=city,
                                     state=state,
                                     pincode=pcode,
                                     profileImg=proimg,
                                     emailId=eid)
                ins.save()
            print('data saved')
        else:
            if user == 'Signup-Doctor':
                if request.method == 'POST':
                    fname = request.POST.get('fname')
                    lname = request.POST.get('lname')
                    uname = request.POST.get('uname')
                    proimg = request.FILES.get('proimg')
                    eid = request.POST.get('eid')
                    pass1 = request.POST.get('pass1')
                    pass2 = request.POST.get('pass2')
                    address = request.POST.get('address')
                    city = request.POST.get('city')
                    state = request.POST.get('state')
                    pcode = request.POST.get('pcode')

                    ins = models.Doctor(firstname=fname,
                                        lastname=lname,
                                        Username=uname,
                                        password=pass1,
                                        confirmPassword=pass2,
                                        address=address,
                                        city=city,
                                        state=state,
                                        pincode=pcode,
                                        profileImg=proimg,
                                        emailId=eid)
                    ins.save()
            print('data saved')

        if user == 'Login-Patient':

            if request.method == "POST":
                username = request.POST.get('uname', False)
                password = request.POST.get('pass', False)
                bool_ans = models.Patient.objects.filter(Username=username, password=password).exists()
                if bool_ans == True:
                    userPat = username
                    userId = 'P'
                    return redirect('dashboard.html')
                else:
                    return HttpResponse(
                        '<script>alert("Please enter valid credentials"); location.assign("/");</script>')

        else:
            if user == 'Login-Doctor':

                if request.method == "POST":
                    username = request.POST.get('uname', False)
                    password = request.POST.get('pass', False)
                    bool_ans = models.Doctor.objects.filter(Username=username, password=password).exists()
                    if bool_ans == True:
                        userDoc = username
                        print(bool_ans)
                        userId = 'D'
                        return redirect('dashboard.html')
                    else:
                        return HttpResponse(
                            '<script>alert("Please enter valid credentials"); location.assign("/");</script>')

    return render(request, 'signup_login.html')

def dashboard(request):
    global userId,userPat,userDoc
    if userId == 'P':
        patientData = models.Patient.objects.filter(Username=userPat)

        data = {'data':patientData}

        return render(request, 'dashboard.html',data)
    else:
        if userId == 'D':
            doctorData = models.Doctor.objects.filter(Username=userDoc)

            data = {'data': doctorData}

            return render(request, 'dashboard.html', data)
