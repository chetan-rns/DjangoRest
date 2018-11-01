from tastypie.resources import ModelResource
from rest.models import Note
from tastypie.authorization import Authorization

#Import model and create a resource from it
class NoteResource(ModelResource):
	class Meta:
		queryset=Note.objects.all()
		resource_name='note'
		authorization = Authorization()
