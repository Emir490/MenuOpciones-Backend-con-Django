from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *

# Create your views here.
list = []
words = ["Posición 1", "Posición 2", "Posición 3", "Posición 4", "Posición 5", "Posición 6", "Posición 7", "Posición 8", "Posición 9", "Posición 10"]

@api_view(['POST']) 
def setName(request):
    if request.method == 'POST':
        if request.data["name"] == "":
            content = {"msg" : "Campo obligatorio"}   
            return Response(content, status=status.HTTP_403_FORBIDDEN)     
        
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Enviando respuesta al Frontend
            if len(list) > 0:
                list.clear()
            list.append(serializer.data)
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) 
def getName(request):
    if request.method == 'GET':
        if len(list) == 0:  
            return Response({"msg" : "Agrega un nombre"})
        return Response(list[0])
    
# Método para obtener área y perímetro del cuadrado      
@api_view(['POST']) 
def square(request):
    if request.method == 'POST':
        # Diccionario con el valor del lado
        data = request.data
        
        # Verifica que cada dato contenga un valor
        if len(data["side"]) == 0:
            content = {"msg" : "Campo obligatorio"}   
            return Response(content, status=status.HTTP_403_FORBIDDEN)     
        
        # Valor del lado
        side = float(data["side"])
        
        # Agregando Área al diccionario
        data["area"] = side * side
        
        # Agregando Perímetro al diccionario
        data["perimeter"] = side * 4
        
        # Quitando el lado ya que solo queremos el valor del área y perímetro
        del data["side"]
        
        serializer = FigureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Enviando respuesta al Frontend
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST']) 
def rectangle(request):
    if request.method == 'POST':
        # Diccionario con el valor de la base y altura
        data = request.data
        
        # Verifica que cada dato contenga un valor
        if len(data["base"]) == 0 or len(data["height"]) == 0:
            content = {"msg" : "Todos los campos son obligatorios"}   
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        
        # Valor de la base y altura
        base = float(data["base"])
        height = float(data["height"])
        
        # Agregando Área al diccionario
        data["area"] = base * height
        
        # Agregando Perímetro al diccionario
        data["perimeter"] = 2 * (base + height)
        
        # Quitando la base y altura ya que solo queremos el valor del área y perímetro
        del data["base"]
        del data["height"]
        
        serializer = FigureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Enviando respuesta al Frontend
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST']) 
def triangle(request):
    if request.method == 'POST':
        # Diccionario con el valor de la base, altura y lado
        data = request.data
        
        # Verifica que cada dato contenga un valor
        if len(data["side"]) == 0 or len(data["base"]) == 0 or len(data["height"]) == 0:
            content = {"msg" : "Todos los campos son obligatorios"}   
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        
        # Valor de la base y altura
        base = float(data["base"])
        height = float(data["height"])
        side = float(data["side"])
        
        # Agregando Área al diccionario
        data["area"] = base * height / 2
        
        # Agregando Perímetro al diccionario
        data["perimeter"] = base + height + side
        
        # Quitando la base y altura ya que solo queremos el valor del área y perímetro
        del data["base"]
        del data["height"]
        del data["side"]
        
        serializer = FigureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Enviando respuesta al Frontend
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST']) 
def length(request):
    if request.method == 'POST':
        # Obtener palabra ingresada por usuario
        data = request.data 
        
        if data["word"] == "":
            content = {"msg" : "Campo obligatorio"} 
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        
        # Contamos las letras y agregamos al diccionario
        data["length"] = len(data["word"])
        
        del data["word"]
        
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Enviando respuesta al lado del cliente
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def modifyList(request):
    if request.method == 'GET':
        # Imprime la lista de palabras
        return Response(words) 
    elif request.method == 'PUT':
        # Palabra a poner en la lista y posición
        data = request.data
        
        # Validación
        if data["word"] == "" or data["position"] == "":
            content = {"msg": "Todos los campos son obligatorios"}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        
        # Determinando posición y palabra
        position = int(data["position"])
        word = data["word"]
        
        # Validando que no se ingrese una posición inválida
        if position <= 0 or position > 11:
            content = {"msg" : "Posición inválida"}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        
        # Agregar más elementos a la lista
        if position > 10:
            words.append(word)
            
        # Modificando lista
        words[position - 1] = word
        
        # Imprmir lista modificada
        return Response(words)
    
@api_view(['POST']) 
def validatePass(request):
    if request.method == 'POST':
        # Contraseña
        password = "password"
        
        # Palabra ingresada por el usuario
        data = request.data
        word = data["input"]
        
        if word == "":
            content = {"msg" : "Campo obligatorio"} 
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        
        # Valida que la contraseña sea correcta o no 
        if word == password:
            return Response({"msg" : "Contraseña Correcta"})
        else:
            content = {"msg" : "Contraseña Incorrecta"}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        
@api_view(['POST']) 
def iterateList(request):
    if request.method == 'POST':
        # Diccionario con registros agregadas por el usuario
        data = request.data 
        
        if data["word1"] == "" or data["word2"] == "" or data["word3"] == "" or data["word4"] == "" or data["word5"] == "":
            content = {"msg": "Todos los campos son obligatorios"}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        
        if len(list) > 0:
            list.clear()
            
        # Agregando valores a una lista    
        for i in data.values():
            list.append(i)
            
        # Reccorriendo lista en consola
        for i in list:
            print(f"Ahora i vale {i}")
            
        return Response(list)