from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from users.models import Message
from users.models import User as MyUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SingUpForm

cvInfo = {
    'name':'Juan Manuel',
    'title':'developer',
    'photo':'https://pbs.twimg.com/profile_images/1665026225/caraavatarsoimpson_400x400.png',
    'lastName':'Nava Zamudio',
    'phoneNumber':'2711486567',
    'email':'juanmanuel.navazamudio@gmail.com',
    'objetive':'I want to to develop quality systems to generate value in the proyects',
    'greet':'hola, esta es mi segunda prueba para un cv',
    'tecnologies':[
        {'name':'java','url':''},
        {'name':'C#','url':''},
        {'name':'html','url':''},
        {'name':'javascript','url':''},
        {'name':'git','url':''}
        ],
    'experience':[
        {
            'place':'Tradicom',
            'description':'I worked as frontend developer and technical support'
        },
        {
            'place':'Rio Blanco Regional Hospital',
            'description':'I did my professional practices developing the administration module for the hospital system'
        },
        {
            'place':'Intersyst',
            'description':'Im working improving the truck entrance control system of the port of Veracruz'
        }
    ],
    'abilities':[
        'patient',
        'self learning',
        'team work'
        ],
    'contactLinks':[
        {
            'tooltipName':'Twitter',
            'url':'https://twitter.com/JuanNavaZamudio',
            'icon': 'fa-twitter'
        },
        {
            'tooltipName':'Mail',
            'url':'mailto:juanmanuel.navazamudio@gmail.com',
            'icon': 'fa-google'
        },
        {
            'tooltipName':'Github',
            'url':'https://github.com/JuanNavaZamudio',
            'icon': 'fa-github'
        },
    ]
    }

listaProyectos = [
        {
        'nombre':'serpientes',
        'descripcion':'juego de serpientes y escaleras',
        'imagen':'',
        'url':''
        },
        {
        'nombre':'simulador estacionamiento',
        'descripcion':'Simulador de tiempos de estacionamiento en una gasolinera',
        'imagen':'',
        'url':''
        },
        {
        'nombre':'gato',
        'descripcion':'juego gráfico de gato o tres en raya para dos jugadores',
        'imagen':'',
        'url':''
        },
    ]


# Create your views here.
def mySimpleFunction(request):
    if request.method == 'POST':
        return render(request,'mainPage.html', cvInfo)
    else:
        return render(request,'mainPage.html', cvInfo)



def muestraDemosPorTecnologia(request):
    return render(request,'proyectos.html',{'listaProyectos':listaProyectos})



def SendMessage(request):
    return render(request,'registerMessage.html',{'state':0})



@login_required
def RegisterMessage(request):
    if request.method == 'POST':
        

        email = request.POST['email']

        exist = User.objects.filter( username = email )


        name = request.POST['name']
        last_name = request.POST['last_name']
        message = request.POST['message']
        
        try:
            user = User.objects.create_user(
                username = email,
                email = email,
                first_name = name,
                last_name = last_name,
                password = email
            )
        
            myuser = MyUser(
                user = user,
                active = 0
            )

            myuser.save()
        
        except IntegrityError:
            user = authenticate(request, username=email, password=email)


        message = Message(user = myuser)
        message.message = message
        message.save()
        

        return render(request,'registerMessage.html',{'state' : 1})
    else:
        return render(request,'registerMessage.html',{'state':0})



def SingUp(request):
    if request.method == 'POST':

        form = SingUpForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            username = data['username']
            name = data['name']
            email = data['email']
            password = data['password']

            try:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    first_name = name,
                    password = password
                )

                myuser = MyUser(
                    user = user,
                    active = 0
                )

                myuser.save()

                return redirect('Login')

            except IntegrityError:
                return render(request,'singUp.html',{'state': 'User not valid', 'form':form})
    else:
        form = SingUpForm()
    
    return render(request,'singUp.html', {'form': form})



def SingIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user:
            login(request,user)

            return render(request,'login.html',{'state':'user logged correctly'})
        else:
            return render(request, 'login.html',{'state': 'user or password not valid'})

    else:
        return render(request, 'login.html',{'state': ''})

@login_required
def Logout(request):
    logout(request)
    return redirect('cv')