from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

def create_room(request):
    """Render the create room page."""
    context = {"message": "This is the create room page"}
    return render(request, "frontend/create_room.html", context)

def join_room(request):
    """Render the join room page."""
    context = {"message": "This is the join room page"}
    return render(request, "frontend/join_room.html", context)