from django.db import models
from django.contrib.auth.models import User # To one-To-one Relation
from django.utils.translation import ugettext_lazy as _ # TO Translations
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

Gender = (
    ('M','Male'),
    ('F','Female'),
)   

class Profile(models.Model):
    
    Ta5sos = {
    ("جلدية","جلدية"),
    ("اسنان","اسنان"),
    ("نفسي","نفسي"),
    ("اطفال","اطفال حديثي الولادة"),
    ("مخ","مخ واعصاب"),
    ("عظام","عظام"),
    ("نساء","نساء وتوليد"),
    ("انف","انف واذن وحنجرة"),
    ("قلب","قلب واوعية دموية"),
    ("امراض","امراض دم"),
    ("اورام","اورام"),
    ("باطنه","باطنه"),
    ("تخسيس","تخسيس وتغذية"),
    ("اطفال","جراحة اطفال"),
    ("اورام","جراحة اورام"),
    ("اوعيه","جراحة اوعية دموية"),
    ("تجميل","جراحة تجميل"),
    ("سمنه","جراحه سمنة ومناظير"),
}
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("الاسم"), max_length=60)
    doctor = models.CharField(_("دكتور :"),choices=Ta5sos, max_length=60)
    who_i = models.CharField(_("من أنا (نبذه) "), max_length=300 ,null=True,blank=True)
    specialist=models.CharField(_("التخصص : "),choices=Ta5sos ,max_length=80)
    address = models.TextField(_("العنوان بالتفصيل "), max_length=150)
    number_phone = models.CharField(_("رقم الهاتف "),max_length=13)
    working_houres = models.IntegerField(_("عدد ساعات العمل "),default=0)
    waiting_time = models.IntegerField(_("مده الانتظار"),default=0,null=True,blank=True)
    services = models.CharField(_("خدمات الدكتور: "), max_length=100,null=True,blank=True)
    price = models.IntegerField(_("سعر الكشف  "), null=True,blank=True)
    gender = models.CharField(_('النوع '),choices=Gender,max_length = 150)
    image = models.ImageField(_("الصورة الشخصية"), upload_to='media/profile/',default='media/profile/default.png')
    createdAt = models.DateTimeField(_('تاريخ البدء'),auto_now_add=False ,default=timezone.now)
    facebook = models.CharField(_("فيسبوك"),null=True, blank=True, max_length=100)
    twitter = models.CharField(_("تويتر"), null=True, blank=True,max_length=100)
    google = models.CharField(_("جوجل"), null=True, blank=True,max_length=100)
    yahoo = models.CharField(_("ايميل"), null=True, blank=True,max_length=100)
    slug = models.SlugField(_("slug"),null=True,blank=True)

    
  
  
    def save(self, *args, **kwargs):    # Slugify
        if not self.slug:
            self.slug = slugify(self.user.username)
    
        super(Profile, self).save(*args, **kwargs) # Call the real save() method 
    
    def __str__(self):
        return self.name