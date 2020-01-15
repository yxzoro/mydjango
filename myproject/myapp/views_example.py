from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
# Create your views here.


# 1 method view
def test(request):
	'''
	it is a test
	'''
	# return render(request ,'test.html' ,{'key': 'value'})
	return HttpResponse('test')


# 2 class view (Restful)
class MyClassView(View):   
	
	# 所有以 ?附加在url后的数据都能从request.GET里拿到(django把?后的data都放进了GET里,无论何种http方法)
	def get(self, request):
		param_dic = request.GET
		return HttpResponse('get')
														   # 以postman工具的 raw形式 提交数据对应的代码写法 ? 
	# request.POST 只能拿到以form(post)提交的data, 拿不到以raw(post)提交的data => raw data在request.body里,
	def post(self, request): 
		param_dic = request.POST
		return HttpResponse('post')
	
	# u can always get all parametres from [request] object in delete/put/.. or use framework's encapsulated methods ?
	def put(self, request):  
		# param = ?
		print( type(request.body) )   # str
		print( request.body	 )  # 以raw(post)提交的data => PUT data 在request.body里,
		return HttpResponse('put')        

	def delete(self, request):
		# param = ?
		print( type(request.body) )  # str
		print( request.body	)   # 以raw(delete)提交的data => DELETE data 在request.body里,
		return HttpResponse('delete')


# 位置参数
def get_time(request, param1, param2):
	#从url过来获取的 param 总是 unicode/string类型,若需int等则要转一下,
	return HttpResponse('get param:' + param1 + param2)  
	
# 命名参数	
def get_date(request, year, month):
	#从url过来获取的 param 总是 unicode/string类型,若需int等则要转一下,
	return HttpResponse('get param:' + year + month)  
	
	
	
	
	
	
	
