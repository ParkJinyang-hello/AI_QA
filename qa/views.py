from django.shortcuts import render
import openai
import openai
import os
from dotenv import load_dotenv
# Create your views here.

load_dotenv()
def qa_view(request):
    answer = None
    print('request.method', request.method)
    if request.method == 'post':
        question = request.POST.get('question')  # 폼에서 가져옴
        response = openai.chat.completions.create(
            model = 'gpt-4o',
            message = [
                {'role':'user', 'content':question}
            ]
        )
        print(f'response : {response}')
        answer = response.choices[0].messages.content
    return render(request, 'qa/index.html', {'answer':answer})