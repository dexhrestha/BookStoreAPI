from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from accounts.api.serializers import UserPublicSerializer

from comment.models import Comment

class CommentSerializer(serializers.ModelSerializer):
	reply_count = serializers.SerializerMethodField()
	replies   = serializers.SerializerMethodField()
	user = UserPublicSerializer(read_only=True)
	class Meta:
		model = Comment
		fields = ['id',
				'user',
				'object_id',
				'content_type',
				'parent',
				'content',
				'timestamp',
				'updated',
				'replies',
				'reply_count']

	def get_reply_count(self,obj):
		if obj.is_parent:
			return obj.children().count()
		return 0

	def get_replies(self,obj):
		if obj.is_parent:
			return CommentChildSerializer(obj.children(),many=True).data
		return None


class CommentChildSerializer(serializers.ModelSerializer):
	user = UserPublicSerializer(read_only=True)
	class Meta:
		model = Comment
		fields = ['id',
				'user',
				'content',
				'parent',
				'timestamp',
				'updated']

	

class CommentDetailSerializer(serializers.ModelSerializer):
	user = UserPublicSerializer(read_only=True)
	reply_count = serializers.SerializerMethodField()
	class Meta:
		model = Comment
		fields = ['id',
				'user',
				'content_type',
				'object_id',
				'content',
				'replies',
				'reply_count',
				'timestamp',
				]

	def get_reply_count(self,obj):
		if obj.is_parent:
			return obj.children().count()
		return 0

def createCommentSerializer(model_type=None,object_id=None,
				# parent_id=None,
				user=None):
	class CommentCreateSerializer(serializers.ModelSerializer):
		user = UserPublicSerializer(read_only=True)
		object_id = serializers.SerializerMethodField()
		class Meta:
			model = Comment
			fields = ['id',
				'user',
				'content',
				'object_id',
				'parent',
				'timestamp',
				]

		def __init__(self,*args,**kwargs):
			self.model_type = model_type
			self.object_id = object_id
			# self.parent_obj = parent #actual parent obj
			self.user = user
			# if parent_id: #from func params
			# 	parent_qs = Comment.objects.filter(id=parent_id)
			# 	if parent_qs.exists() and parent_qs.count() == 1:
			# 		self.parent_obj = parent_qs.first()
			return super(CommentCreateSerializer,self).__init__(*args,**kwargs)
		
		def validate(self,data):
			model_type = self.model_type
			model_qs = ContentType.objects.filter(model=model_type)
			if not model_qs.exists() or model_qs.count()!=1:
				raise serializers.ValidationError('Content Type doesnot exist!');
			ModelClass = model_qs.first().model_class() #For dynamic models that use comment
			obj_qs = ModelClass.objects.filter(id=self.object_id)
			if not obj_qs.exists() or obj_qs.count() != 1:
				raise serializers.ValidationError('Object doesnot exists!')
			if  data['parent'] and data['parent'].parent is not None:
				raise serializers.ValidationError('Cannot convert child to parent!')
			return data

		def get_object_id(self,obj):
			# print(obj.object_id)
			if obj.parent and not obj.object_id == obj.parent.object_id:
				raise serializers.ValidationError('Object id mismatch! Please check id in url')
			return obj.object_id
			
		def create(self,validated_data):
			content = validated_data.get('content')
			user = self.user
			model_type =self.model_type
			object_id = self.object_id
			parent_obj = validated_data.get('parent')
			comment = Comment.objects.create_by_model_type(model_type=model_type,
															object_id=object_id,
															user=user,
															content=content,
															parent_obj=parent_obj)
			return comment

	return CommentCreateSerializer

