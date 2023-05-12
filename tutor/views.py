import datetime
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *


def Login1(request):
    if request.method == 'POST':
        u = request.POST['name']
        p = request.POST['password']
        qry = Login.objects.filter(username=u, password=p)
        if qry.exists():
            qry = qry[0]
            request.session['lid'] = qry.id
            request.session['login'] = "1"
            if qry.utype == 'admin':
                return redirect('/home-admin')
            elif qry.utype == 'tutor':
                return redirect('/home-tutor')
            elif qry.utype == 'Student':
                return redirect('/home-student')
            else:
                return HttpResponse('<script>alert("Invalid Username or Password .");window.location="/invaliduser#contact"</script>')
        else:

            return HttpResponse('<script>alert("Invalid Username or Password.");window.location="/invaliduser#contact"</script>')
    # return render(request, 'login.html')


def InvalidUser(request):
    return render(request, 'login.html')


def Index(request):
    return render(request, 'index.html')


# -------------------------------------------------- ADMIN_MODULE --------------------------------------------------- #


def Home_Admin(request):
    if request.session['login'] == "1":

        return render(request, 'admin_module/index.html')
    else:
        return redirect('/')


def StudentTable_Admin(request):
    if request.session['login'] == "1":

        obj = Student.objects.all()
        return render(request, 'admin_module/studenttable.html', {'data': obj})
    else:
        return redirect('/')


def TutorTable_Admin(request):
    if request.session['login'] == "1":

        obj = Tutor.objects.all()
        return render(request, 'admin_module/tutortable.html', {'data': obj})
    else:
        return redirect('/')


def ApproveOrReject(request):
    if request.session['login'] == "1":

        obj = Tutor.objects.filter(login__utype='pending')
        return render(request, "admin_module/approveorreject.html", {'data': obj})
    else:
        return redirect('/')


def Approve(request, id):
    if request.session['login'] == "1":

        Login.objects.filter(id=id).update(utype='tutor')
        return redirect('/admin_module/tutortable.html')
    else:
        return redirect('/')


def Reject(request, id):
    if request.session['login'] == "1":

        Login.objects.filter(id=id).delete()
        Tutor.objects.filter(login_id=id).delete()
        return HttpResponse('<script>alert("Successfully rejected.");window.location="//tutortable-admin#a"</script>')
    else:
        return redirect('/')


def CourseAdd(request):

    if request.session['login'] == "1":

        if request.method == 'POST':
            cname = request.POST['textfield']
            obj = Course()
            obj.coursename = cname
            obj.save()
            return HttpResponse('ok')
        return render(request, 'admin_module/courseadd.html')
    else:
        return redirect('/')


def CourseTable_Admin(request):
    if request.session['login'] == "1":

        obj = Course.objects.all()
        return render(request, 'admin_module/coursetable.html', {'data': obj})
    else:
        return redirect('/')


def Delete(request, id):
    if request.session['login'] == "1":

        Course.objects.filter(id=id).delete()
        return HttpResponse('<script>alert("Sucessfully Deleted.");window.location="/coursetable-admin#a"</script>')
    else:
        return redirect('/')


def SubjectAdd(request):

    if request.session['login'] == "1":

        if request.method == 'POST':
            sname = request.POST['textfield']
            obj = Subject()
            obj.subjectname = sname
            obj.save()
            return HttpResponse('ok')
        return render(request, 'admin_module/subjectadd.html')
    else:
        return redirect('/')


def SubjectTable_Admin(request):
    if request.session['login'] == "1":

        obj = Subject.objects.all()
        return render(request, 'admin_module/subjecttable.html', {'data': obj})
    else:
        return redirect('/')


def Delete2(request, id):
    if request.session['login'] == "1":

        Subject.objects.filter(id=id).delete()
        return HttpResponse('<script>alert("Sucessfully Deleted.");window.location="/subjecttable-admin#a"</script>')
    else:
        return redirect('/')


def SubjectAllocation(request):
    if request.session['login'] == "1":

        if request.method == 'POST':
            c = request.POST['select']
            s = request.POST['select2']

            obj = AllocateSubject()
            obj.course_id = c
            obj.subject_id = s
            obj.save()
            return HttpResponse('<script>alert("Sucessfully Allocated.");window.location="/allocationtable#a"</script>')
        else:
            obj = Course.objects.all()
            obj1 = Subject.objects.all()
            return render(request, 'admin_module/subjectallocation.html', {'data': obj, 'data1': obj1})
    else:
        return redirect('/')


def AllocationTable(request):
    if request.session['login'] == "1":

        obj = AllocateSubject.objects.all()
        return render(request, 'admin_module/allocationtable.html', {'data': obj})
    else:
        return redirect('/')


def Delete3(request, id):

    if request.session['login'] == "1":

        AllocateSubject.objects.filter(id=id).delete()
        return HttpResponse('<script>alert("Sucessfully Deleted.");window.location="/allocationtable#a"</script>')
    else:
        return redirect('/')


def ComplaintTable_Admin(request):
    if request.session['login'] == "1":

        obj = Complaint.objects.all()
        return render(request, 'admin_module/complainttable.html', {'data': obj})
    else:
        return redirect('/')


def Reply(request, id):
    if request.session['login'] == "1":

        if request.method == 'POST':
            r = request.POST['textarea']
            d = datetime.datetime.now().strftime("%Y-%m-%d")
            obj = Complaint.objects.filter(id=id).update(reply=r, reply_date=d)
            return HttpResponse('ok')
        return render(request, 'admin_module/reply.html')
    else:
        return redirect('/')


def FeedbackTable(request):
    if request.session['login'] == "1":

        obj = Feedback.objects.all()
        return render(request, 'admin_module/feedbacktable.html', {'data': obj})
    else:
        return redirect('/')


def ChangePassword_Admin(request):

     if request.session['login'] == "1":

        if request.method == 'POST':
            cr = request.POST['textfield']
            nw = request.POST['textfield2']
            cf = request.POST['textfield3']
            qry = Login.objects.get(utype='admin', id=request.session['lid'])
            ps = qry.password
            if str(cr) == str(ps):
                if nw == cf:
                    Login.objects.filter(utype='admin', id=request.session['lid']).update(password=nw)
                    return HttpResponse('<script>alert("Password Updated.");window.location="/login#contact"</script>')

                else:
                    return HttpResponse('<script>alert("Password does not match.");window.location="/chngpsadmn#a"</script>')
            else:
                return HttpResponse('<script>alert("Incorrect Password.");window.location="/chngpsadmn#a"</script>')

                # return render(request, 'admin_module/changepassword.html')
     else:
        return redirect('/')


def ChangePasswordAdmn(request):
    return render(request, 'admin_module/changepassword.html')


# ------------------------------------------------- TUTOR_MODULE ---------------------------------------------------- #


def TutorRegistration(request):
    if request.method == 'POST':
        n = request.POST['textfield']
        h = request.POST['textfield2']
        p = request.POST['textfield3']
        po = request.POST['textfield4']
        pi = request.POST['textfield5']
        d = request.POST['select']
        g = request.POST['RadioGroup1']
        q = request.POST.getlist('CheckboxGroup1')
        c = request.POST['textfield6']
        f = request.FILES['fileField']
        e = request.POST['textfield7']
        ps = request.POST['textfield8']
        import datetime
        d1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\user\PycharmProjects\OnlineTutor\static\\" + d1 + '.pdf', f)
        path = "/static/" + d1 + '.pdf'
        qry = Tutor.objects.filter(email=e)
        if qry.exists():
            return HttpResponse(
                '<script>alert("Username already exist.");window.location="/tutorregistration"</script>')
        else:

            obj1 = Login()
            obj1.username = e
            obj1.password = ps
            obj1.utype = 'Pending'
            obj1.save()

            obj = Tutor()
            obj.name = n
            obj.housename = h
            obj.place = p
            obj.post = po
            obj.pin = pi
            obj.district = d
            obj.gender = g
            obj.qualification = ', '.join(q)
            obj.contact = c
            obj.email = e
            obj.password = ps
            obj.cv = str(path)
            obj.login = obj1
            obj.save()

            return HttpResponse(
                '<script>alert("You are Successfully registered.");window.location="/login#contact"</script>')
    else:
        return render(request, 'tutor_module/tutorregistration.html')


def Home_Tutor(request):
    if request.session['login'] == "1":

        return render(request, 'tutor_module/index.html')
    else:
        return redirect('/')


def Tutor_Profile(request):

    if request.session['login'] == "1":

        obj = Tutor.objects.get(login=request.session['lid'])
        return render(request, 'tutor_module/profile.html', {'data': obj})
    else:
        return redirect('/')


def CourseTable_Tutor(request):
    if request.session['login'] == "1":

        obj = Course.objects.all()
        return render(request, 'tutor_module/coursetable.html', {'data': obj})
    else:
        return redirect('/')


def SubjectTable_Tutor(request, id):
    if request.session['login'] == "1":

        obj = AllocateSubject.objects.filter(course=id)
        return render(request, 'tutor_module/subjecttable.html', {'data': obj})
    else:
        return redirect('/')


def SubjectSelect(request,id):
    if request.session['login'] == "1":

        t=Tutor.objects.get(login=request.session['lid'])
        obj = SelectSubject()
        obj.allocatesubject_id = str(id)
        obj.tutor = t
        obj.save()
        return HttpResponse('<script>alert("Subject Selected.");window.location="/coursetable-tutor#a"</script>')
    else:
        return redirect('/')


def View_SelectedSubject(request):
    if request.session['login'] == "1":

        obj = SelectSubject.objects.filter(tutor__login=request.session['lid'])
        return render(request, 'tutor_module/subjectselect.html', {'data': obj})
    else:
        return redirect('/')


def ClassUpload(request, id):
    if request.session['login'] == "1":

        if request.method == 'POST':
            f = request.FILES['fileField']
            d = datetime.datetime.now().strftime("%Y-%m-%d")
            t = datetime.datetime.now().strftime("%H:%M:%S")
            fs = FileSystemStorage()
            fs.save(r"C:\Users\user\PycharmProjects\OnlineTutor\static\\" + d + '.mp4', f)
            path = '/static/' + d + '.mp4'

            obj = Class()
            obj.selectsubject_id = id
            obj.classes = str(path)
            obj.date = d
            obj.time = t
            obj.save()
            return HttpResponse('<script>alert("Sucessfully Uploaded.");window.location="/classtable-tutor#a"</script>')
        else:
            return render(request, 'tutor_module/classupload.html')
    else:
        return redirect('/')


def ClassTable_Tutor(request):
    if request.session['login'] == "1":

        obj = Class.objects.filter(selectsubject__tutor__login=request.session['lid'])
        return render(request, 'tutor_module/classtable.html', {'data': obj})
    else:
        return redirect('/')


def Delete5(request, id):
    if request.session['login'] == "1":

        Class.objects.filter(id=id).delete()
        return HttpResponse('<script>alert("Sucessfully Deleted.");window.location="/classtable-tutor#a"</script>')
    else:
        return redirect('/')


def Material(request, id):

    if request.session['login'] == "1":

        if request.method == 'POST':
            f1 = request.FILES['fileField']
            d = datetime.datetime.now().strftime("%Y-%m-%d")
            t = datetime.datetime.now().strftime("%H:%M:%S")
            fs = FileSystemStorage()
            fs.save(r"C:\Users\user\PycharmProjects\OnlineTutor\static\\" + d + '.pdf', f1)
            path = "/static/" + d + '.pdf'
            obj = Materials()
            obj.selectsubject_id = id

            obj.material = str(path)
            obj.date = d
            obj.time = t
            obj.save()
            return HttpResponse(
                '<script>alert("Sucessfully Uploaded.");window.location="/materialstable-tutor#a"</script>')
        return render(request, 'tutor_module/materials.html')
    else:
        return redirect('/')


def MaterialsTable_Tutor(request):
    if request.session['login'] == "1":

        obj = Materials.objects.filter(selectsubject__tutor__login=request.session['lid'])
        return render(request, 'tutor_module/materialstable.html', {'data': obj})
    else:
        return redirect('/')


def Delete4(request, id):
    if request.session['login'] == "1":

        Materials.objects.filter(id=id).delete()
        return HttpResponse('<script>alert("Sucessfully Deleted.");window.location="/materials#a"</script>')
    else:
        return redirect('/')


def StudentTable_Tutor(request):

    if request.session['login'] == "1":

        obj = Student.objects.filter()
        return render(request, 'tutor_module/studenttable.html', {'data': obj})
    else:
        return redirect('/')


def TutorTable_Tutor(request):

    if request.session['login'] == "1":

        obj = Tutor.objects.all()
        return render(request, 'tutor_module/tutortable.html', {'data': obj})
    else:
        return redirect('/')


def TutorChat(request, id):
    if request.session['login'] == "1":

        if request.method == 'POST':
            c = request.POST['msg']
            d = datetime.datetime.now().strftime("%Y-%m-%d")
            obj = Chat()
            obj.tutor = Tutor.objects.get(login=request.session['lid'])
            obj.student = Student.objects.get(id=id)
            obj.chat = c
            obj.date = d
            obj.save()
            return HttpResponse('ok')
        else:
            qry = Tutor.objects.get(login=request.session['lid'])
            uid = qry.id
            print("uuuuuuuuu", uid)
            content = Chat.objects.filter(tutor=uid, student=id)
            for i in content:
                qry = i.chat
            print(qry)
            return render(request, 'tutor_module/chat.html', {'data': content, 'uid': uid, 'rid': id})
    else:
        return redirect('/')


def ChangePassword_Tutor(request):

    if request.session['login'] == "1":

         if request.method == 'POST':
            cr = request.POST['textfield']
            nw = request.POST['textfield2']
            cf = request.POST['textfield3']
            qry = Login.objects.get(utype='tutor', id=request.session['lid'])
            ps = qry.password
            if str(cr) == str(ps):
                if nw == cf:
                    Login.objects.filter(utype='tutor', id=request.session['lid']).update(password=nw)
                    return HttpResponse('<script>alert("Password Updated.");window.location="/login#contact"</script>')

                else:
                    return HttpResponse('<script>alert("Password does not match.");window.location="/chngpsttr#a"</script>')
            else:
                return HttpResponse('<script>alert("Incorrect Password.");window.location="/chngpsttr#a"</script>')

                # return render(request, 'tutor_module/changepassword.html')

    else:
        return redirect('/')


def ChangePasswordTtr(request):
    return render(request, "tutor_module/changepassword.html")


# ----------------------------------------------- STUDENT_MODULE ---------------------------------------------------- #


def StudentRegistration(request):

    if request.method == 'POST':
        n = request.POST['textfield']
        h = request.POST['textfield2']
        p = request.POST['textfield3']
        po = request.POST['textfield4']
        pi = request.POST['textfield5']
        d = request.POST['select']
        g = request.POST['RadioGroup1']
        c = request.POST['textfield6']
        e = request.POST['textfield7']
        ps = request.POST['textfield8']
        qry = Student.objects.filter(email=e)
        if qry.exists():
            return HttpResponse('<script>alert("Username already exist.");window.location="/studentregistration"</script>')
        else:
            obj1 = Login()
            obj1.username = e
            obj1.password = ps
            obj1.utype = 'Student'
            obj1.save()

            obj = Student()

            obj.name = n
            obj.housename = h
            obj.place = p
            obj.post = po
            obj.pin = pi
            obj.district = d
            obj.gender = g
            obj.contact = c
            obj.email = e
            obj.login = obj1
            obj.save()
            return HttpResponse('<script>alert("You are Successfully registered.");window.location="/login#contact"</script>')
    else:
        return render(request, 'student_module/studentregistration.html')



def Home_Student(request):
    if request.session['login'] == "1":

        return render(request, 'student_module/index.html')
    else:
        return redirect('/')


def Student_Profile(request):
    if request.session['login'] == "1":

        obj = Student.objects.get(login=request.session['lid'])
        return render(request, 'student_module/profile.html', {'data': obj})
    else:
        return redirect('/')


def CourseTable_Student(request):
    if request.session['login'] == "1":

        obj = Course.objects.all()
        return render(request, 'student_module/coursetable.html', {'data': obj})
    else:
        return redirect('/')


def SubjectTable_Student(request, id):
    if request.session['login'] == "1":

        obj = AllocateSubject.objects.filter(course=id)
        return render(request, 'student_module/subjecttable.html', {'data': obj})
    else:
        return redirect('/')


def ClassTable_Student(request, id):
    if request.session['login'] == "1":

        obj = Class.objects.filter(selectsubject__allocatesubject=id)
        return render(request, 'student_module/classtable.html', {'data': obj})
    else:
        return redirect('/')


def MaterialsTable_Student(request, id):
    if request.session['login'] == "1":

        obj = Materials.objects.filter(selectsubject__allocatesubject=id)
        return render(request, 'student_module/materialstable.html', {'data': obj})
    else:
        return redirect('/')


def TutorTable_Student(request, id):
    if request.session['login'] == "1":

        obj = Tutor.objects.filter(selectsubject__allocatesubject=id)
        return render(request, 'student_module/tutortable.html', {'data': obj})
    else:
        return redirect('/')


def StudentChat(request, id):
    if request.session['login'] == "1":

        if request.method == 'POST':
            c = request.POST['msg']
            d = datetime.datetime.now().strftime("%Y-%m-%d")
            obj = Chat()
            obj.student = Student.objects.get(login=request.session['lid'])
            obj.tutor = Tutor.objects.get(id=id)
            obj.chat = c
            obj.date = d
            obj.save()
            return HttpResponse('ok')
        else:
            qry = Student.objects.get(login=request.session['lid'])
            uid = qry.id
            print("uuuuuu",qry)
            content = Chat.objects.filter(student=uid, tutor=id)
            for i in content:
                qry = i.chat
            print(qry)
            return render(request, 'student_module/chat.html', {'data': content, 'uid': uid, 'tid': id})
    else:
        return redirect('/')


def student_Complaint(request):

    if request.session['login'] == "1":

        if request.method == 'POST':
            c = request.POST['textarea']
            d = datetime.datetime.now().strftime("%Y-%m-%d")

            obj = Complaint()
            obj.complaint = c
            obj.complaint_date = d
            obj.reply = 'pending'
            obj.reply_date = 'pending'
            obj.student = Student.objects.get(login=request.session['lid'])
            obj.save()
            return HttpResponse('ok')
        else:
            return render(request, 'student_module/complaint.html')
    else:
        return redirect('/')


def ComplaintTable_Student(request):
    if request.session['login'] == "1":

        obj = Complaint.objects.all()
        return render(request, 'student_module/complainttable.html', {'data': obj})
    else:
        return redirect('/')


def FeedbackForm(request):
    if request.session['login'] == "1":
        if request.method == 'POST':
            f = request.POST['textarea']
            d = datetime.datetime.now().strftime("%Y-%m-%d")
            obj = Feedback()
            obj.student = Student.objects.get(login=request.session['lid'])
            obj.feedback = f
            obj.date = d
            obj.save()
            return HttpResponse('ok')
        else:
            return render(request, 'student_module/feedbackform.htm')
    else:
        return redirect('/')


def ChangePassword_Student(request):

    if request.session['login'] == "1":

        if request.method == 'POST':
            cr = request.POST['textfield']
            nw = request.POST['textfield2']
            cf = request.POST['textfield3']
            qry = Login.objects.get(utype='Student', id=request.session['lid'])
            ps = qry.password
            print(ps,cr)
            if str(cr) == str(ps):
                if nw == cf:
                    Login.objects.filter(utype='Student', id=request.session['lid']).update(password=nw)
                    return HttpResponse('<script>alert("Password Updated.");window.location="/login#contact"</script>')

                else:
                    return HttpResponse(
                        '<script>alert("Password does not match.");window.location="/chngpsstd#a"</script>')
            else:
                return HttpResponse('<script>alert("Incorrect Password.");window.location="/chngpsstd#a"</script>')

        # return render(request, 'student_module/changepassword.html')
    else:
        return redirect('/')


def ChangePasswordStd(request):
    return render(request, "student_module/changepassword.html")


def Logout(request):
    request.session['login'] = "0"
    return redirect('/')


# =======================================================================================================================
#                                               ANDROID STUDIO
# =======================================================================================================================


def Log(request):
    if request.method == 'POST':
        u = request.POST['u']
        p = request.POST['p']
        qry = Login.objects.filter(username=u, password=p)
        if qry.exists():
            qry = qry[0]
            return JsonResponse({"status": "ok", "lid": qry.id, "type": qry.utype})
        else:
            return JsonResponse({"status": "no"})


def Reg(request):
    if request.method == 'POST':
        n = request.POST['nm']
        h = request.POST['hnm']
        pl = request.POST['plc']
        ps = request.POST['pst']
        pi = request.POST['pin']
        c = request.POST['cntct']
        e = request.POST['eml']
        pw = request.POST['pswrd']
        g = request.POST['gndr']
        d = request.POST['dstrct']
        qry = Student.objects.filter(email=e)
        if qry.exists():
            return JsonResponse({'status': 'Already Exists'})
        else:
            obj1 = Login()
            obj1.username = e
            obj1.password = pw
            obj1.utype = 'Student'
            obj1.save()

            obj = Student()

            obj.name = n
            obj.housename = h
            obj.place = pl
            obj.post = ps
            obj.pin = pi
            obj.district = d
            obj.gender = g
            obj.contact = c
            obj.email = e
            obj.login = obj1
            obj.save()
            return JsonResponse({'status': 'ok'})


def Profile_Android(request):
        lid = request.POST['id']
        obj = Student.objects.get(login=lid)
        return JsonResponse({'status': 'ok', 'id': obj.id, 'name': obj.name, 'housename': obj.housename, 'place': obj.place, 'post': obj.post, 'district': obj.district, 'pin': obj.pin, 'gender': obj.gender, 'contact': obj.contact, 'email': obj.email})


def ViewCourse_Android(request):
    obj = Course.objects.all()
    ar = []
    for i in obj:
        ar.append({'id': i.id, 'coursename': i.coursename})
    return JsonResponse({'status': 'ok', 'data': ar})


def ViewSubject_Android(request):
    lid = request.POST['cid']
    print(lid)
    obj = AllocateSubject.objects.filter(course=lid)
    ar = []
    for i in obj:
        ar.append({'id': i.id, 'subjectname': i.subject.subjectname})
    return JsonResponse({'status': 'ok', 'data': ar})


def ViewClass_Android(request):
    lid = request.POST['sid']
    print(lid)
    obj = Class.objects.filter(selectsubject__allocatesubject=lid)
    ar = []
    for i in obj:
        ar.append({'id': i.id, 'classes': i.classes, 'date': i.date, 'time': i.time})
    return JsonResponse({'status': 'ok', 'data': ar})


def ViewNotes_Android(request):
    lid = request.POST['sid']
    print(lid)
    obj = Materials.objects.filter(selectsubject__allocatesubject=lid)
    ar = []
    for i in obj:
        ar.append({'id': i.id, 'material': i.material, 'date': i.date, 'time': i.time})
    return JsonResponse({'status': 'ok', 'data': ar})


def ViewTutor_Android(request):
    lid = request.POST['subject_id']
    print(lid)
    obj = Tutor.objects.filter(selectsubject__allocatesubject=lid)
    ar = []
    for i in obj:
        print(i.name)
        ar.append({"id": i.id, 'name': i.name, 'housename': i.housename, 'place': i.place, 'post': i.post, 'district': i.district, 'pin': i.pin, 'gender': i.gender, 'qualification': i.qualification, 'contact': i.contact, 'email': i.email})
    return JsonResponse({'status': 'ok', "data": ar})


def Complaint_Android(request):
    if request.method == 'POST':
        c = request.POST['comp']
        lid = request.POST['id']
        d = datetime.datetime.now().strftime("%Y-%m-%d")

        obj = Complaint()
        obj.complaint = c
        obj.complaint_date = d
        obj.reply = 'pending'
        obj.reply_date = 'pending'
        obj.student = Student.objects.get(login=lid)
        obj.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'no'})


def ViewReply_Android(request):
    idd = request.POST['id']
    print(idd)
    obj = Complaint.objects.filter(student__login=idd)
    ar = []
    for i in obj:
        if obj.exists():
            ar.append({'id': i.id, 'complaint': i.complaint, 'complaint_date': i.complaint_date, 'reply': i.reply, 'reply_date': i.reply_date})
    return JsonResponse({'status': 'ok', 'data': ar})


def Feedback_Android(request):
    if request.method == 'POST':
        f = request.POST['fed']
        lid = request.POST['id']
        d = datetime.datetime.now().strftime("%Y-%m-%d")
        obj = Feedback()
        obj.student = Student.objects.get(login=lid)
        obj.feedback = f
        obj.date = d
        obj.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'no'})


def ChangePassword_Android(request):
    if request.method == 'POST':
        cr = request.POST['crnt']
        nw = request.POST['nw']
        cf = request.POST['cnfrm']
        lid = request.POST['id']
        qry = Login.objects.get(utype='Student', id=lid)
        ps = qry.password
        print(ps, cr)
        if str(cr) == str(ps):
            if nw == cf:
                Login.objects.filter(utype='Student', id=lid).update(password=nw)
                return JsonResponse({'status': 'ok'})

            else:
                return JsonResponse({'status': "password doesn't match"})
        else:
            return JsonResponse({'status': 'Incorrect password'})










