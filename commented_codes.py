# id
# user
# user_agent
# ip_address
# host_name
# content_type
# query_string
# post_data
#  http_method
# http_referer
# path_info/
# request_data
# response_status_code/
# response_reason_phrase/
# response_body/
# attempt_time
# load_response_time/
# operating_system /

# my_set=audit_stat
# s = list(my_set)
# print(s)

# audit_stat={
#     winauditcount,
#     iphoneauditcount,
#     androidauditcount,
#     ipadauditcount,
#     postmanauditcount,
#     otherauditcount
#     }
# print(audit_stat)
# os_ranking=list({'Window','Iphone', 'Android', 'Ipad','Postman', 'Others'})
# audit_stat_list_convert = list(audit_stat)

# return Response('error':error)

# mac
# iPhone
# Android
# iPad
# PostmanRuntime
# Others

# def audit_stat_view(self, request,extra_context=None):
#         audit_stat=(
#             AuditLog.objects.filter(operating_system='Windows').count()
#         )
#         as_json =json.dumps(list(audit_stat), cls=DjangoJSONEncoder)
#         extra_context = extra_context or {"stat_data" :as_json}
#         return super().audit_stat_view(request,extra_context=extra_context)



# from django.utils import timezone
# import time
# from logisticapp.models import AuditLog

# class AuditMiddleware:
#     # begin an action  ## one time configuration for middleware
#     def __init__(self, get_response) -> None:
        
#         self.get_response = get_response

#     def stats(self, os_info):
#         if "Windows" in os_info:
#             return 'Windows'
#         elif "mac" in os_info:
#             return 'Mac'
#         elif "iPhone" in os_info:
#             return 'Iphone'
#         elif "Android" in os_info:
#             return 'Android'
#         elif "iPad" in os_info:
#             return 'Ipad'
#         elif "PostmanRuntime" in os_info:
#             return 'Postman'
#         else:
#             return 'Others'

#     def __call__(self, request, *args, **kwargs):
        
#         try:
#             user_language=request.headers['Accept-Language']
#         except Exception:
#             user_language=None
#         start_time = time.time()
#         execution_time = time.time() - start_time
#         # user=''
#         try:
#             user=request.user
#         except:
#             user = 'None'
#         #     raise e
#         # if request.user:
#         #     user=request.user
#         # else:
#         #     user = 'None'

#         oeprating_system = self.stats(request.META['HTTP_USER_AGENT'])
#         response = self.get_response(request)
#         log_data = {
#             'user': user,
#             'user_agent': request.META.get('HTTP_USER_AGENT', ''),
#             'ip_address': request.META.get('REMOTE_ADDR', ''),
#             'host_name': request.META.get('REMOTE_HOST', ''),
#             'content_type': request.META.get('CONTENT_TYPE', ''),
#             'query_string': request.META.get('QUERY_STRING', ''),
#             'post_data': request.POST.dict(),
#             'http_method': request.method,
#             'http_referer': request.META.get('HTTP_REFERER', ''),
#             'path_info': request.path_info,
#             'response_status_code': response.status_code,
#             'response_reason_phrase': response.reason_phrase,
#             'response_body': response.content.decode('utf-8'),
#             'user_language':  user_language,
#             'load_response_time': execution_time,
#             'operating_system':oeprating_system

#         }
#         # print(request.META['HTTP_USER_AGENT'])
#         # print(oeprating_system)
#         print(log_data)
#         AuditLog.objects.create(**log_data)
#         response = self.get_response(request)
     
#         return response  # alert django that we have completed our audit
   
   

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
#    # print(response.status_code)
#         # print(request.path)
#         # if 'en-US' in request.headers['Accept-Language']:
#         #     print('English')
#         # print(request.META['PATH_INFO'])
#         # print(request.META['REQUEST_METHOD'])
#     # def process_response(self, request, response=None):
#     #     response = self.get_response(request)
#     #     print(response.status_code)
#     #     print('who dey')


# # chk={

# #                 'response_status_code': response.status_code,
# #                 'response_reason_phrase': response.reason_phrase,
# #                 'response_body': response.content.decode('utf-8'),

# #     }
#         # print(chk)


# # id
# # user
# # user_agent
# # ip_address
# # host_name
# # content_type
# # query_string
# # post_data
# #  http_method
# # http_referer
# # path_info
# # request_data
# # response_status_code
# # response_reason_phrase
# # response_body
# # attempt_time
# # load_response_time
# # operating_system
