from .models import Category


def get_categories(request):
      category=Category.objects.all()
      

      return {
          'cats':category,
          'fire':'fire'
      }







      
