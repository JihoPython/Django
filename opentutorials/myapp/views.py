from typing import List
from dataclasses import dataclass

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


@dataclass
class Topic:
    id: int
    title: str
    body: str

last_id = 3
topics: List[Topic] = [
    Topic(1, 'routing', 'Routing is ...'),
    Topic(2, 'view', 'View is ...'),
    Topic(3, 'model', 'Model is ...'),
]

def template(article: str, id: int = 0) -> str:
    global topics

    items: str = ''.join(list(map(
        lambda t: f'''<li><a href="/read/{t.id}">{t.title}</a></li>''',
        topics
    )))

    context_ui = ''
    if id:
        context_ui = f'''
        <li>
            <form action="/delete/" method="POST">
                <input type="hidden" name="id" value={id}>
                <input type="submit" value="delete">
            </form>
        </li>
        <li><a href="/update/{id}/">update</a></li>
        '''

    return f'''
        <html>
        <body>
            <h1><a href="/">Django</a></h1>
            <p>id: {id}</p>
            <ol>{items}</ol>
            <hr>
            <article>{article}<article>
            <ul>
                <li><a href="/create">write</a></li>
                {context_ui}
            </ul>
        </body>
        </html>
    '''


def index(request):
    article = '''
    <h2>Welcome</h2>
    <p>Hello Django!</p>
    '''
    return HttpResponse(template(article))


@csrf_exempt
def create(request: HttpRequest):
    if request.method == 'GET':
        article = '''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(template(article))

    elif request.method == 'POST':
        global topics, last_id

        title = request.POST['title']
        body = request.POST['body']
        topic = Topic(last_id := last_id + 1, title, body)

        topics.append(topic)

        return redirect(f'/read/{topic.id}/')

    raise Exception(f'Invalid Request method: {request.method}')

def read(request, id: int):
    global topics

    topic = list(filter(lambda t: t.id == id, topics)).pop()

    if topic:
        article = f'<h2>{topic.title}</h2><p>{topic.body}</p>'
    else:
        raise Exception('Invalid article id')

    return HttpResponse(template(article, id))


@csrf_exempt
def update(request: HttpRequest, id: int):
    global topics

    if request.method == 'GET':
        topic = list(filter(lambda t: t.id == id, topics)).pop()
        article = f'''
        <form action="/update/{id}/" method="POST">
            <p>
                <input
                    type="text"
                    name="title"
                    placeholder="title"
                    value={topic.title}
                >
            </p>
            <p>
                <textarea name="body" placeholder="body">{
                    topic.body
                }</textarea>
            </p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(template(article))
    elif request.method == 'POST':
        topic = list(filter(lambda t: t.id == id, topics)).pop()
        topic.title = request.POST['title']
        topic.body = request.POST['body']

        return redirect(f'/read/{id}/')

    raise Exception(f'Invalid Request method: {request.method}')


@csrf_exempt
def delete(request: HttpRequest):
    if request.method == 'POST':
        global topics

        id = int(request.POST['id'])

        topics = list(filter(lambda t: t.id != id, topics))

        return redirect('/')

    raise Exception(f'Invalid Request method: {request.method}')