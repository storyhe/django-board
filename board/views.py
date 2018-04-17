from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from user.controller.UserController import UserController
from .controller.BoardController import BoardController
from user.tool import alertRender


from .models import Post


# Create your views here.


def board_posts(request, board_name=None):
    if board_name is None:
        return HttpResponse("데이터가 없습니다.")

    b_controller = BoardController(request=request)
    board_id = b_controller.check_board_id(board_name)
    if board_id is False:
        return HttpResponse("없는 게시판입니다.")

    posts = b_controller.get_posts(board_id=board_id)
    return render(request, 'post_list.html', {'posts': posts, 'board_name':board_name})


def board_write(request, board_name=None):
    if board_name is None:
        return HttpResponse("데이터가 없습니다.")

    paging = request.GET.get("paging")

    b_controller = BoardController(request=request)
    u_controller = UserController(request=request)

    board_id = b_controller.check_board_id(board_name)

    if board_id is False:
        return HttpResponse("없는 게시판입니다.")

    if request.method == 'POST':
        title = request.POST.get("title", None)
        content = request.POST.get("content", None)

        if title is None or content is None or title is "" or content is "":
            return alertRender(request, message="공란이 있습니다.")

        b_controller.write_post(title=title, content=content, board_id=board_id, writer=u_controller.read_session())
        return alertRender(request, message="작성되었습니다.", target=reverse('board_posts', args=[board_name]))

    return render(request, 'write_form.html', {'board_name': board_name})
