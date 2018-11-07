from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class CommentManager(models.Manager):
	def parent(self):
		qs = super(CommentManager,self).filter(parent=None)
		return qs

	def filter_by_instance(self,instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		object_id = instance.id
		qs = super(CommentManager,self).filter(content_type=content_type,object_id=object_id).filter(parent=None)
		return qs

	def get_by_content_type(self,content_type):
		model_qs = ContentType.objects.filter(model=content_type)
		if model_qs.exists():
			return super(CommentManager,self).filter(content_type=model_qs.first().id).filter(parent=None)
		return 	None

	def create_by_model_type(self,model_type,object_id,content,user,parent_obj=None):
		model_qs = ContentType.objects.filter(model=model_type)
		if model_qs.exists():
			ModelClass = model_qs.first().model_class() #For dynamic models that use comment
			obj_qs = ModelClass.objects.filter(id=object_id)
			if obj_qs.exists() and obj_qs.count() == 1:
				instance = self.model() #creating a comment instace
				instance.content = content
				instance.user = user
				instance.content_type = model_qs.first()
				instance.object_id = obj_qs.first().id
				if parent_obj:
					instance.parent = parent_obj
				instance.save()
				return instance
		return None
			

class Comment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)

	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
		
	class Meta:
		ordering = ['-timestamp']

	objects = CommentManager()

	def __str__(self):
		return self.user.username+' '+self.content[:10]

	def children(self):
		return Comment.objects.filter(parent=self)

	@property
	def is_parent(self):
		if self.parent is not None:
			return False
		return True