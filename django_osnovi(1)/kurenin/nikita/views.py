from django.http import HttpResponse

def index(request):
    return HttpResponse("Основная информация <br> Имя = Куренин Никита Алексеевич <br> 16 лет, 03.05.2006 года <br> люблю программировать, ранее увлекался биатлоном. <br> попробуйте перейти по страницам '/about/' и '/contacts/'")
def about(request):
    return HttpResponse("Приехал из города 'Мамадыш', в школе учился на 4-5, люблю учиться.")
def contact(request):
    return HttpResponse("Telegram: @nakyouner <br> GitHub:https://github.com/nakyoin <br> Телефон: +79655851558 <br> ")
