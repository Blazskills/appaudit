from django.db import models
import uuid
import jsonfield
# Create your models here.


class Department(models.Model):
    department_name = models.CharField(
        max_length=200, unique=True, null=False, blank=False)
    department_hod = models.ForeignKey(
        to='authentication.User',   related_name='department_hod', on_delete=models.CASCADE)
    department_tl = models.ForeignKey(
        to='authentication.User', related_name='department_tl', on_delete=models.CASCADE)
    # staffs = models.ForeignKey(to=User,  related_name='staffs_in_department', on_delete=models.CASCADE)

    department_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.department_name


class RequestHeader(models.Model):
    requestheader_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    request_header_creator = models.ForeignKey(
        to='authentication.User',  related_name='request_header_creator', on_delete=models.CASCADE)  # This feilds should bea current user auto log but for testing purposes,
    requestheader_name = models.CharField(
        max_length=200, null=False, blank=False)
    department_header_onwer = models.ForeignKey(
        to=Department,  related_name='department_requestheader', on_delete=models.CASCADE)
    super_approved = models.BooleanField(default=False, null=True, blank=True)
    super_approved_by = models.CharField(max_length=200, null=True, blank=True)
    super_approved_date = models.DateTimeField(null=True, blank=True)
    total_approved_item = models.CharField(
        max_length=200, null=True, blank=True)
    # item_approved_list = models.ManyToManyField( Quantity,  through='RequestExpenses', related_name='items_approved', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.requestheader_name


class RequestExpenses(models.Model):
    requester = models.ForeignKey(
        to='authentication.User',  related_name='user_requester', on_delete=models.CASCADE)
    requestheader = models.ForeignKey(
        to=RequestHeader,  related_name='request_header', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, max_length=255)
    product_quantity = models.IntegerField()
    item_description = models.TextField()
    item_approved = models.BooleanField(default=False)
    date_approved = models.BooleanField(default=False)
    approved_by = models.BooleanField(default=False)
    date_approved = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.requestheader_name


class AuditLog(models.Model):
    """ Audit log """

    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    user = models.ForeignKey(to='authentication.User', null=True, on_delete=models.CASCADE)
    user_agent = models.CharField(max_length=255,)
    ip_address = models.GenericIPAddressField(verbose_name="IP Address", null=True,)
    host_name = models.CharField(verbose_name="Host Name", max_length=200, default='')
    content_type = models.CharField(verbose_name="Content Type", max_length=200,)
    query_string = models.TextField(verbose_name="Query String")
    post_data = jsonfield.JSONField(verbose_name="Post Data", null=True, blank=True)
    http_method = models.CharField(verbose_name="HTTP Method", max_length=20,)
    http_referer = models.CharField(verbose_name="Http Referer", max_length=20,)
    path_info = models.CharField(verbose_name="Path", max_length=255,)
    request_data = models.TextField(null=True)
    response_status_code = models.IntegerField(null=True)
    response_reason_phrase = models.TextField()
    response_body = models.TextField(default='')
    attempt_time = models.DateTimeField(auto_now_add=True)
    user_language = models.CharField(verbose_name="User Language",null=True, max_length=255,)

    load_response_time=models.CharField(verbose_name="Response Time", max_length=255,)
    operating_system = models.CharField(verbose_name="Operating System(OS)", max_length=255,)
    class Meta:
            ordering = ['-attempt_time']

    def __str__(self):
        """ unicode value for this model """
        return f'{self.user}, {self.attempt_time}'