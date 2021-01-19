from django.shortcuts import render

def showIndex(request):

    student_info = [
        {"idno":101,"name":"gyana","mark":[10,20,30,40,50,60]},
        {"idno":102,"name":"gyana1","mark":[20,20,30,40,50,60]},
        {"idno":103,"name":"gyana2","mark":[30,20,30,40,50,60]},
        {"idno":104,"name":"gyana3","mark":[40,20,30,40,50,60]},
        {"idno":105,"name":"gyana4","mark":[50,20,30,40,50,60]},
        {"idno":106,"name":"gyana5","mark":[60,20,30,40,50,60]},
    ]

    return render(request,"index.html",{"data":student_info})