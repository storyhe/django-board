from django.shortcuts import render
from .controller.UserController import UserController
from .tool import alertRender
# Create your views here.


def login(request):
    controller = UserController(request=request)

    if controller.read_session() is not None:
        return alertRender(request, message="이미 로그인 되었습니다.", target="/")

    if request.method == "POST":
        userid = request.POST.get('userid')
        userpw = request.POST.get('userpassword')


        if controller.login_user(userid=userid, userpassword=userpw):
            return alertRender(request, message="로그인 되었습니다.", target="/")
        else:
            return alertRender(request, message="로그인 실패")

    return render(request, 'login.html')


def join(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        userpw = request.POST.get('userpassword')

        controller = UserController(request=request)

        if controller.check_userid(userid) is not None:
            return alertRender(request, message="이미 존재하는 아이디입니다.")

        result = controller.create_user(userid=userid, userpassword=userpw)
        if result is True:
            return render(request, 'welcome.html')
        else:
            return alertRender(request, message="가입에 오류가 발생하였습니다.")


    return render(request, 'join.html')

def logout(request):
    controller = UserController(request=request)
    if controller.read_session() is not None:
        controller.logout()
        return alertRender(request, message="로그아웃 되었습니다.")

    return alertRender(request, message="로그인 부터해주세요.")