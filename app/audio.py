from django.http import HttpResponse, HttpResponseBadRequest
import boto3

def speech(request):
    polly_client = boto3.Session(region_name='us-east-1').client('polly')

    # Get the text to synthesize speech from
    text = request.GET.get('content')

    # Get the voice to use
    voice = request.GET.get('voice', 'Joanna')

    # Synthesize speech from the text using the specified voice
    response = polly_client.synthesize_speech(VoiceId=voice,
                OutputFormat='mp3',
                Text=text)

    # Set the filename for the downloaded file
    filename = 'awwzapp_synthesize_voice_over.mp3'

    # Create the HTTP response with the synthesized audio data and the Content-Disposition header
    http_response = HttpResponse(response['AudioStream'].read(), content_type='audio/mpeg')
    http_response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return http_response
