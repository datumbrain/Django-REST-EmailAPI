from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmailSerializer

class EmailAPIView(APIView):
    def post(self, request):
        # initializing an EmailSerializer instance with the POST data
        serializer = EmailSerializer(data=request.data)
        # if the request data is valid, 
        # use serializer.save method to save data and email gets the object returned by it.
        if serializer.is_valid():
            email = serializer.save()
            try:
            # make an instance of EmailMessage by extracting data from serializer instance
                msg = EmailMessage(
                    subject=email.subject,
                    body=email.body,
                    from_email=email.from_email,
                    to=[email.to_email]
                )
                # method to send an email
                msg.send()
                # returns on success
                return Response({'status': 'Email sent'}, status=status.HTTP_200_OK)
            except:
                # returns on failure to send an email
                return Response({'status': 'Email sending failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # returns on invalid data.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
