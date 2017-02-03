from django.shortcuts import render, render_to_response


# Create your views here.



def login(request):
    return render(request, "hello.html", {});


def nebu(request):
    ad = request.POST['ad'];
    soyad = request.POST['soyad'];
    print ad + "ssss" + soyad;
    return render_to_response("sonuc.html", {'form': ad + soyad, }, )
