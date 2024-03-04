from django.db import models

# Create your models here.
class jobRegister(models.Model):
    job_no = models.CharField(max_length=200)
    in_date = models.DateField()
    out_date = models.DateField()
    customer_name = models.CharField(max_length=200)
    gp = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    user_contact_name = models.CharField(max_length=200)
    dealer_name = models.CharField(max_length=200)
    bill_no = models.CharField(max_length=200)
    date = models.DateField()
    bill_to = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    model_or_frame = models.CharField(max_length=200)
    sr_no_or_mc_no = models.CharField(max_length=200)
    rotor_voltage = models.CharField(max_length=200)
    rotor_current = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    kw = models.CharField(max_length=200)
    rpm = models.CharField(max_length=200)
    stator_current = models.CharField(max_length=200)
    stator_voltage = models.CharField(max_length=200)
    defect = models.TextField()
    cutting = models.TextField()
    rewinding = models.TextField()
    fitting = models.TextField()
    housing_machining = models.TextField()
    shaft_machining = models.TextField()
    bearing = models.TextField()
    terminal = models.TextField()
    cooling_fan = models.TextField()
    welding = models.TextField()
    balancing = models.TextField()
    lath_work = models.TextField()
    other_1 = models.TextField()
    other_2 = models.TextField()
    our_bill_or_challan_no = models.CharField(max_length=200)

    def __str__(self):
        return self.job_no
    
    class Meta:
        verbose_name_plural = "Jobs"

class TestReport(models.Model):
    job = models.ForeignKey(jobRegister, on_delete=models.CASCADE)
    product = models.CharField(max_length=500)
    kw = models.CharField(max_length=100)
    voltage_R = models.CharField(max_length=100)
    voltage_Y = models.CharField(max_length=100)
    voltage_B = models.CharField(max_length=100)
    no_load_amps_R = models.CharField(max_length=100)
    no_load_amps_Y = models.CharField(max_length=100)
    no_load_amps_B = models.CharField(max_length=100)
    inductance_in_H_R = models.CharField(max_length=100)
    inductance_in_H_Y = models.CharField(max_length=100)
    inductance_in_H_B = models.CharField(max_length=100)
    resistance_in_ohms_R = models.CharField(max_length=100)
    resistance_in_ohms_Y = models.CharField(max_length=100)
    resistance_in_ohms_B = models.CharField(max_length=100)
    vibration_NDE_axial = models.CharField(max_length=100)
    vibration_NDE_horizontal = models.CharField(max_length=100)
    vibration_NDE_vertical = models.CharField(max_length=100)
    vibration_DE_axial = models.CharField(max_length=100)
    vibration_DE_horizontal = models.CharField(max_length=100)
    vibration_DE_vertical = models.CharField(max_length=100)
    IR_in_M_ohms_R = models.CharField(max_length=100)
    IR_in_M_ohms_Y = models.CharField(max_length=100)
    IR_in_M_ohms_B = models.CharField(max_length=100)
    run_out_in_MM_point_1 = models.CharField(max_length=100)
    run_out_in_MM_point_2 = models.CharField(max_length=100)
    run_out_in_MM_point_3 = models.CharField(max_length=100)
    run_out_in_MM_point_4 = models.CharField(max_length=100)
    run_out_in_MM_point_5 = models.CharField(max_length=100)
    run_out_in_MM_point_6 = models.CharField(max_length=100)
    shaft_od_in_MM_point_1 = models.CharField(max_length=100)
    shaft_od_in_MM_point_2 = models.CharField(max_length=100)
    shaft_od_in_MM_point_3 = models.CharField(max_length=100)
    shaft_od_in_MM_point_4 = models.CharField(max_length=100)
    shaft_od_in_MM_point_5 = models.CharField(max_length=100)
    housing_id_point_1 = models.CharField(max_length=100)
    housing_id_point_2 = models.CharField(max_length=100)
    housing_id_point_3 = models.CharField(max_length=100)
    housing_id_point_4 = models.CharField(max_length=100)
    final_observation = models.TextField()

    def __str__(self):
        return self.job.job_no + "/" + self.product
    
    class Meta:
        verbose_name_plural = "Test Reports"








