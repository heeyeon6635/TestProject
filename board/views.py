from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
# def index(request):
#     return HttpResponse("Board index page.")

# 이후 수정
from .models import Board

def index(request):
      board_list=Board.objects.order_by('-create_date')
      context={'board_list': board_list}
      return render(request, 'board/board-list.html', context)

# def detail(request, board_id):
#     board=Board.bojects.get(id=board_id)
#     context={'board':board}
#     return render(request, 'board/board_detail,html', context)

# class create(generic.CreateView):
#     model=Board
#     fields=['subject', 'content', 'create_date']
#     success_url=reverse_lazy('board:list')
#     template_name_suffix='_create'