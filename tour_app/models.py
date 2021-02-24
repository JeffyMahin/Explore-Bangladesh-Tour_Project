from django.db import models
from datetime import datetime



class Division(models.Model):
    DIVISION_LIST = (
        ('Dhaka', 'Dhaka'),
        ('Chittagong', 'Chittagong'),
        ('Rajshahi', 'Rajshahi'),
        ('Barishal', 'Barishal'),
        ('Sylhet', 'Sylhet'),
        ('Mymensingh', 'Mymensingh'),
        ('Rangpur', 'Rangpur'),
        ('Khulna', 'Khulna')
    )
    name = models.CharField(max_length=120, choices=DIVISION_LIST)
    image = models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.name


class Location(models.Model):
    DIVISION_LIST = (
        ('Dhaka', 'Dhaka'),
        ('Chittagong', 'Chittagong'),
        ('Rajshahi', 'Rajshahi'),
        ('Barishal', 'Barishal'),
        ('Sylhet', 'Sylhet'),
        ('Mymensingh', 'Mymensingh'),
        ('Rangpur', 'Rangpur'),
        ('Khulna', 'Khulna')
    )
    DISTRICT_LIST= (
        ('Barguna', 'Barguna'),
        ('Barisal', 'Barisal'),
        ('Bhola', 'Bhola'),
        ('Jhalokati ', 'Jhalokati '),
        ('Patuakhali ', 'Patuakhali '),
        ('Pirojpur ', 'Pirojpur '),
        ('Bandarban ', 'Bandarban '),
        ('Brahmanbaria ', 'Brahmanbaria '),
        ('Chandpur ', 'Chandpur '),
        ('Chittagong ', 'Chittagong '),
        ('Comilla ', 'Comilla '),
        ('Cox\'s Bazar', 'Cox\'s Bazar'),
        ('Feni ', 'Feni '),
        ('Khagrachari ', 'Khagrachari '),
        ('Lakshmipur ', 'Lakshmipur '),
        ('Noakhali ', 'Noakhali '),
        ('Rangamati ', 'Rangamati '),
        ('Dhaka', 'Dhaka'),
        ('Faridpur ', 'Faridpur '),
        ('Gazipur ', 'Gazipur '),
        ('Gopalganj ', 'Gopalganj '),
        ('Kishoreganj ', 'Kishoreganj '),
        ('Madaripur ', 'Madaripur '),
        ('Manikganj ', 'Manikganj '),
        ('Munshiganj ', 'Munshiganj '),
        ('Narayanganj ', 'Narayanganj '),
        ('Narsingdi ', 'Narsingdi '),
        ('Rajbari ', 'Rajbari '),
        ('Shariatpur ', 'Shariatpur '),
        ('Tangail ', 'Tangail '),
        ('Mymensingh', 'Mymensingh'),
        ('Jamalpur ', 'Jamalpur '),
        ('Netrokona ', 'Netrokona '),
        ('Sherpur ', 'Sherpur '),
        ('Khulna', 'Khulna'),
        ('Bagerhat ', 'Bagerhat '),
        ('Chuadanga ', 'Chuadanga '),
        ('Jessore ', 'Jessore '),
        ('Jhenaidah ', 'Jhenaidah '),
        ('Khulna ', 'Khulna '),
        ('Kushtia ', 'Kushtia '),
        ('Magura ', 'Magura '),
        ('Meherpur ', 'Meherpur '),
        ('Narail ', 'Narail '),
        ('Shatkhira ', 'Shatkhira '),
        ('Rajshahi', 'Rajshahi'),
        ('Bogra ', 'Bogra '),
        ('Jaipurhat ', 'Jaipurhat '),
        ('Naogaon', 'Naogaon'),
        ('Natore ', 'Natore '),
        ('Nawabganj ', 'Nawabganj '),
        ('Pabna ', 'Pabna '),
        ('Sirajganj ', 'Sirajganj '),
        ('Rangpur ', 'Rangpur '),
        ('Gaibandha ', 'Gaibandha '),
        ('Kurigram ', 'Kurigram '),
        ('Nilphamari ', 'Nilphamari '),
        ('Lalmonirhat ', 'Lalmonirhat '),
        ('Dinajpur ', 'Dinajpur '),
        ('Thakurgaon ', 'Thakurgaon '),
        ('Panchagarh ', 'Panchagarh '),
        ('Sylhet', 'Sylhet'),
        ('Habiganj ', 'Habiganj '),
        ('Maulvibazar  ', 'Maulvibazar  '),
        ('Sunamganj  ', 'Sunamganj  '),
    )
    title = models.CharField(max_length=120)
    division= models.CharField(max_length=50, choices=DIVISION_LIST, null=True)
    district = models.CharField(max_length=120, choices=DISTRICT_LIST)
    image = models.ImageField(upload_to='upload/')
    description = models.TextField()
    police_station = models.CharField(max_length=255, null=True, blank=True)
    police_phone = models.CharField(max_length=25, null=True, blank=True)
    fire_service = models.CharField(max_length=255, null=True, blank=True)
    fire_phone = models.CharField(max_length=25, null=True, blank=True)
    created_at = models.TimeField(default=datetime.now())

    def __str__(self):
        return self.title


class GuideDetails(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    image = models.ImageField(upload_to='upload/')
    email = models.EmailField(max_length=254, null=True, blank=True)
    address = models.CharField(max_length=500)
    date_of_birth = models.DateTimeField()

    def __str__(self):
        return self.name

class Thana(models.Model):
    police_station = models.CharField(max_length=255)
    police_phone = models.CharField(max_length= 25)
    fire_service = models.CharField(max_length = 255)
    fire_phone = models.CharField(max_length = 25)

    def __str__(self):
        return self.police_station



