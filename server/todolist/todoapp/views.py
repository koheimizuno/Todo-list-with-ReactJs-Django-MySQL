from django.shortcuts import render

from django.http import JsonResponse
from django.middleware import csrf
from django.core.serializers import serialize
# Create your views here.
import json

from .models import TodoItems




def get_csrf_token(request):
    csrf_token = csrf.get_token(request)
    return JsonResponse({'csrftoken': csrf_token})



def save(request):
    
    print(request)
    
    if request.method == "POST":
        
        data = json.loads(request.body)
        
        print(data.get('title'))
        
        todosave = TodoItems()
        
        
        todosave.title = data.get('title')
        todosave.description = data.get('description')
        todosave.priority = data.get('priority')
         
        todosave.save() 
        
        
        

        return JsonResponse({'message': 'Data saved successfully'})
    
    else:
        return JsonResponse({'error': 'Invalid request method'})



def list(request):
    print('list')
    todolist = TodoItems.objects.all()

     # Serialize the queryset using Django's serializers
    serialized_data = serialize('json', todolist)

    # Deserialize the data to a Python object
    deserialized_data = json.loads(serialized_data)

    # Extract the list of dictionaries from the serialized data, renaming 'pk' to 'id'
    data_list = [{'id': item['pk'], **item['fields']} for item in deserialized_data]

    # Return a JsonResponse with the list of dictionaries
    return JsonResponse(data_list, safe=False)


def deleteTodo(request):
    print('deleteTodo')

    if request.method == 'DELETE':
        data = json.loads(request.body)
        todoId = data.get('id')
        
        tododelete = TodoItems.objects.get(id=todoId)
        tododelete.delete()
        
        return JsonResponse({'message': 'Successfully Deleted'})
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

        
def updateTodo(request):
    
    if request.method == 'PUT':
        
        data = json.loads(request.body)
       
        print(data) 
        
        todosave = TodoItems.objects.get(id=data.get('id'))
        
        
        todosave.title = data.get('title')
        todosave.description = data.get('description')
        todosave.priority = data.get('priority')
         
        todosave.save() 
        
        
        

        return JsonResponse({'message': 'Update successfully'})
    
    else:
        return JsonResponse({'error': 'Invalid request method'})
