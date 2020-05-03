from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request,'master.html', cvInfo)

def muestraDemosPorTecnologia(request):
    return render(request,'proyectos.html',{'listaProyectos':listaProyectos})