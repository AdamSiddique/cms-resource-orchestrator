from django.db import models

class Physicist(models.Model):
    name = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class SubDetector(models.Model):
    SYSTEM_CHOICES = [
        ('TRK', 'Tracker'),
        ('ECAL', 'Electromagnetic Calorimeter'),
        ('HCAL', 'Hadronic Calorimeter'),
        ('MU', 'Muon System'),
    ]
    name = models.CharField(max_length=100)
    system_type = models.CharField(max_length=4, choices=SYSTEM_CHOICES)
    status = models.CharField(max_length=50, default="Operational") # Operational, Maintenance, Offline

    def __str__(self):
        return f"{self.name} ({self.system_type})"
    
class MaintenanceLog(models.Model):
    detector = models.ForeignKey(SubDetector, on_delete=models.CASCADE, related_name='logs')
    operator = models.ForeignKey(Physicist, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)