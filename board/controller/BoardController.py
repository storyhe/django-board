from board.models import *

class BoardController(object):

    def __init__(self, request=None):
        self.request = request

    def check_board_id(self, board_name=None):
        if board_name is None:
            return False

        board = Board.objects.filter(name=board_name).first()
        if board:
            return board.id

        return False

    def get_posts(self, board_id=None, page=0, per=3):
        if board_id is None:
            return []

        paging = page+per
        posts = Post.objects.filter(board_id=board_id).order_by('published_date')[page:paging]
        return posts

    def write_post(self, title=None, content=None, writer=None, board_id=None):
        if title is None or content is None or board_id is None:
            return False

        post = Post(title=title, text=content, writer_id=writer, board_id=board_id)

        try:
            post.publish()
            return True
        except InterruptedError:
            return False


