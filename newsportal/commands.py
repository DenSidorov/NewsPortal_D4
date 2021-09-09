# pip install django
# python -m pip install django-filter --> Не забываем вписать ‘django_filters’ в INSTALLED_APPS в настройках, чтобы получить доступ к фильтрам в приложении.
# py -m venv venv
# venv\scripts\activate
# py manage.py shell --> Запуск shell
# py manage.py makemigrations
# py manage.py migrate
# py manage.py runserver

# from news.models import *  # --> импортируем модели
# User1 = User.objects.create(username='Den', first_name ='Sid') --> Создаём юзера
# Author.objects.create(authorUser=User1) --> Делаем юзера автором
# User2 = User.objects.create(username='Max', first_name ='Sid') --> Создаём 2 юзера
# Author.objects.create(authorUser=User2) --> Делаем юзера автором
# Category.objects.create(name='Models') --> Создаём категорию
# Category.objects.create(name='Views') --> Создаём категорию
# Category.objects.create(name='JS') --> Создаём категорию
# Category.objects.create(name='OOP') --> Создаём категорию
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Den')), categoryType='NW', title='Получение объектов модели, метод filter', text='метод filter возвращает объект QuerySet, который является результатом выполнения запроса. Внутри этого результата мы видим два объекта, но они имеют не очень презентабельное название. Это название формируется Django автоматически. Его можно изменить, переопределив метод __str__(self) соответствующей модели. Однако можно поступить и другим хитрым способом — преобразовать QuerySet в список!') --> Создаём пост
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Max')), categoryType='AR', title='метод filter', text='Фильтрация имеет огромное количество вспомогательных инструментов. Например, дописав к названию поля __gt в аргументе метода, можно найти все значения, которые больше (greater than) заданного числа.') --> Создаём пост
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Max')), categoryType='AR', title='двойное подчеркивание', text='Мы применили фильтр, но не по самому полю текущей модели, а по полям связанной модели. Для этого использовали также двойное подчеркивание и сразу за ним — поле, по которому будем фильтровать. Аналогично мы можем поступать и со значениями! Используя двойное подчеркивание мы можем выводить поле связанного объекта модели, а не сам объект. Более того, если связи между таблицами многоступенчатые (одна зависит от второй, она от третьей и т. д.), то можно создавать целые цепочки связанных фильтров, используя двойное подчеркивание между полями моделей.') --> Создаём пост
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Max')), categoryType='AR', title='метод менеджера all()', text='«сладкое» — напоследок. Если нам нужно получить все объекты модели, мы можем использовать метод менеджера all().') --> Создаём пост
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Den')), categoryType='NW', title='вызов метода get - исключения', text='Любой вызов метода get, например, приведет к выбросу исключения, что не хотелось бы допускать. Для исключения таких ситуаций у QuerySet есть также свои методы, и один из них проверяет наличие каких-либо объектов в результате запроса.') --> Создаём пост
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Den')), categoryType='AR', title='метод сортировки order_by', text='И еще одна полезная функция объектов QuerySet, которые возвращаются всякий раз при вызове методов filter() или all() — это метод сортировки order_by(‘field_name’). Например, мы можем получить отсортированный по ценам список продуктов.') --> Создаём пост
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Den')), categoryType='AR', title='Цензура БББББ ССССС ХХХХХ', text='Цензура БББББ ССССС ХХХХХ') --> Создаём пост
# post1 = Post.objects.get(pk=1) --> Получаем пост через primary key
# post2 = Post.objects.get(pk=2)
# post3 = Post.objects.get(pk=3)
# cat1 = Category.objects.get(name='Models') --> Получаем категорию через name
# cat2 = Category.objects.get(name='Views')
# post1.postCategory.add(cat1) --> Добавляем связи
# post1.postCategory.add(cat1, cat2) --> Добавляем связи. Т.к. many to many можно связывать несколько
# post1.postCategory.add(cat2)
# Comment.objects.create(commentUser=User.objects.get(username='Den'), commentPost=Post.objects.get(pk=1), text='comment text1') --> Создаем комментарий
# Comment.objects.create(commentUser=User.objects.get(username='Den'), commentPost=Post.objects.get(pk=2), text='srtlhjwr;lhkjwr;hjwr;lhj;j')
# Comment.objects.create(commentUser=User.objects.get(username='Max'), commentPost=Post.objects.get(pk=3), text='1111111111111')
# Post.objects.get(pk=1).like() --> Ставим лайки постам
# Post.objects.get(pk=2).like()
# Post.objects.get(pk=3).dislike() --> Ставим дизлайки
# Comment.objects.get(pk=1).like() --> Ставим лайки комментам
# Comment.objects.get(pk=2).dislike() --> Ставим дизлайки комментам
# Author.objects.get(authorUser=User.objects.get(username='Den')). update_rating() --> Обновляем рейтинг Den
# Author.objects.get(authorUser=User.objects.get(username='Max')). update_rating() --> Обновляем рейтинг Max
# a = Author.objects.get(authorUser=User.objects.get(username='Den'))
# a.ratingAuthor --> смотрим обновленный рейтинг
# best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0] --> username автора, рейтинг. Индекс первого объекта. [0:5] Весь рейтинг до 5 индекса
# print(best)
# d = User.objects.all().values('username', 'date_joined') --> даты добавления, username
# print(d)
# best_post = Post.objects.all().order_by('-rating').values('id','dateCreation', 'rating', 'author_id')[0] --> получили id дгчшего поста
# prev = Post.objects.get(id=best_post['id']).preview() --> Превью
# post_user = User.objects.get(id=best_post['author_id']) --> автор
# print(f"Лучшая статья\n Автор: {post_user},\n Дата добавления: {best_post['dateCreation']},\n Рейтинг статьи: {best_post['rating']},\n {prev}")
# comment_post = Comment.objects.get(id=best_post['id']).post_com() --> Коментарий к лучшей статье
# print(comment_post)
#
#
