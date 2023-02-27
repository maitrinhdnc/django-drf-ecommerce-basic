from .base import *

# allowed host là một phương thức bảo mật, 
# Nó ngăn chặn những http host header attack
# là một chuỗi string đại diện host domain name
# nhận các địa chỉ IP mà django phục vụ 
ALLOWED_HOSTS = ['*']
