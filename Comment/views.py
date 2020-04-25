from django.shortcuts import render

# Create your views here.
from . import models


# demo所需函数
def choosePaper(request):
    return render(request, 'choose_paper.html')


def editComment(request):
    return render(request, 'post_comment.html')


def editReply(request):
    return render(request, 'post_reply.html')


# 根据评论ID获取回复
# 非通信函数!!!
def getCommentReply(commentID=1, sortedBy='time'):
    if sortedBy == 'time':
        replys = models.CommentModel.objects.filter(replyCommentID=commentID).order_by('-pubTime', 'hot')
    elif sortedBy == 'hot':
        replys = models.CommentModel.objects.filter(replyCommentID=commentID).order_by('hot', '-pubTime')
    return replys


# 根据paperID获取评论
def getPaperComment(request):
    # for debug
    # return render(request, 'display_page.html')
    #paperID = 1
    paperID = request.POST.get('paperID', 1)
    #sortedBy = 'time'
    sortedBy = request.POST.get('sortedBy', 'time')
    #if sortedBy == 'time':
    # 根据发布时间进行排序
    comments = models.CommentModel.objects.order_by('-pubTime', 'hot').filter(paperID=paperID)
    # 根据热度进行排序
    if sortedBy == 'hot':
        comments = models.CommentModel.objects.filter(paperID=paperID).order_by('hot', '-pubTime')
    for comment in comments:
        comment.replyList = getCommentReply(commentID=comment.id, sortedBy=sortedBy)
    print('成功获取评论')
    return render(request, 'display_page.html', {'comments': comments})


# 发布评论
def postComment(request):
    #print('开始添加评论')
    paperID = request.POST.get('paperID', 'PAPERID')
    userID = request.POST.get('userID', 'USERID')
    userName = request.POST.get('userName', 'USERNAME')
    contentView = request.POST.get('contentView', 'CONTENTVIEW')
    sortedBy = request.POST.get('sortedBy', 'SORTEDBY')
    avatar = request.POST.get('avatar')
    models.CommentModel.objects.create(paperID=paperID,
                                       userID=userID,
                                       userName=userName,
                                       contentView=contentView,
                                       likeNum=0,
                                       dislikeNum=0,
                                       hot=0,
                                       replyCommentID=-1,
                                       replyNum=0,
                                       avatar=avatar)
    #print('成功添加评论')
    comments = models.CommentModel.objects.filter(paperID=paperID)
    for comment in comments:
        comment.replyList = getCommentReply(commentID=comment.id, sortedBy=sortedBy)
    return render(request, 'display_page.html', {'comments': comments})


# 进行回复
def postReply(request):
    paperID = request.POST.get('paperID', 'PAPERID')
    userID = request.POST.get('userID', 'USERID')
    userName = request.POST.get('userName', 'USERNAME')
    sortedBy = request.POST.get('sortedBy', 'SORTEDBY')
    commentID = request.POST.get('commentID', 'COMMENTID')
    contentView = request.POST.get('contentView', 'CONTENTVIEW')
    repliedName = request.POST.get('repliedName', 'REPLIEDNAME')
    models.CommentModel.objects.create(paperID=-1,
                                       userID=userID,
                                       userName=userName,
                                       contentView=contentView,
                                       likeNum=0,
                                       dislikeNum=0,
                                       hot=0,
                                       replyCommentID=commentID,
                                       replyCommentUserName=repliedName)
    tmp_comment = models.CommentModel.objects.get(id=commentID)
    tmp_comment.replyNum += 1
    tmp_comment.save()
    comments = models.CommentModel.objects.filter(paperID=paperID)
    for comment in comments:
        comment.replyList = getCommentReply(commentID=comment.id, sortedBy=sortedBy)
    return render(request, 'display_page.html', {'comments': comments})


# 点踩功能
def postLike(request):
    paperID = request.POST.get('paperID', 'PAPERID')
    commentID = request.POST.get('commentID', 'COMMENTID')
    isLike = request.POST.get('isLike', True)
    sortedBy = request.POST.get('sortedBy', 'time')
    comment = models.CommentModel.objects.filter(id=commentID)
    if isLike:
        comment.likeNum += 1
        comment.hot += 1
    else:
        comment.dislikeNum += 1
        comment.hot -= 1
    comment.save()
    comments = models.CommentModel.objects.filter(paperID=paperID)
    for comment_ in comments:
        comment_.replyList = getCommentReply(commentID=comment_.id, sortedBy=sortedBy)
    return render(request, 'display_page.html', {'comments': comments})