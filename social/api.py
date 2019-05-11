from lib.http import render_json
from social import logics
from social.models import Swiped


def get_rcmd_users(request):
    users = logics.rcmd_users(request.user)
    data = [user.to_dict() for user in users]  # 封装要返回的数据
    return render_json(data)


def like(request):
    '''喜欢'''
    sid = int(request.POST.get('sid'))
    matched = logics.like(request.user, sid)
    return render_json({'is_matched': matched})


def superlike(request):
    '''超级喜欢'''
    sid = int(request.POST.get('sid'))
    matched = logics.superlike(request.user, sid)
    return render_json({'is_matched': matched})


def dislike(request):
    '''不喜欢'''
    sid = int(request.POST.get('sid'))
    Swiped.swipe('dislike', request.user.id, sid)
    return render_json(None)


def rewind(request):
    '''
    反悔

    客户端传来的东西都是不可信的，所有参数都要经过检查, 能不依赖客户端参数时尽量不依赖
    '''
    logics.rewind(request.user)
    return render_json(None)


def show_liked_me(request):
    '''查看喜欢过我的人'''
    users = logics.get_users_liked_me(request.user)
    data = [user.to_dict() for user in users]
    return render_json(data)


def friends(request):
    my_friends = request.user.friends
    data = [friend.to_dict() for friend in my_friends]
    return render_json(data)
