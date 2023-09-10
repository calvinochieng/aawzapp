from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.html import strip_tags
import openai
from app.forms import PromptForm
API_KEY = settings.OPENAI_API_KEY
openai.api_key = API_KEY
model = 'gpt-3.5-turbo-0301'




API_KEY = settings.OPENAI_API_KEY
openai.api_key = API_KEY


def write(request):
    if request.method == 'POST': 
        prompt = request.POST.get('prompt', '').strip()
        if not prompt:
            return JsonResponse({'error': 'Prompt is required'})
        
        prompt = strip_tags(prompt)  # Remove HTML tags
        prompt = prompt.replace('\n', '')  # Remove newlines

        try:
            prompt = PromptForm({'prompt': prompt}).cleaned_data['prompt']
        except ValidationError as e:
            return JsonResponse({'error': e.message})

        messages = {
                    {'role': 'system', 'content': "You are an expert and helpful YouTube Shorts and short upto a minute voiceover writer assistant"},
                    {'role': 'user', 'content': f'Write a short 260-word YouTube Shorts voiceover based on: "{prompt}"'}
                }
        try:
            response = openai.Completion.create(
                model=model,
                messages=messages,
                temperature = 0.5,
                top_p=0.9,
                max_tokens=300,
                frequency_penalty=0,
                presence_penalty=0
            )

            
            result =  { 'text' : f'{response["choices"][0]["message"]["content"]}'}
            return JsonResponse(result)

        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid Request'})





