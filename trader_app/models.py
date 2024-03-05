from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.image
    
    class Meta:
        verbose_name_plural = "photos"

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
    inspection_photos = models.ManyToManyField(Photo,help_text="Select multiple photos")


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

class WindingData(models.Model):
    job = models.ForeignKey(jobRegister, on_delete=models.CASCADE)
    product = models.CharField(max_length=500)
    make = models.CharField(max_length=500)
    kw = models.CharField(max_length=500)
    pole_rpm = models.CharField(max_length=500)
    ph = models.CharField(max_length=500)
    no_of_slots = models.CharField(max_length=500)
    running_wire_gauge = models.CharField(max_length=500)
    running_pitch = models.CharField(max_length=500)
    running_turn = models.CharField(max_length=500)
    starting_wire_gauge = models.CharField(max_length=500)
    starting_pitch = models.CharField(max_length=500)
    starting_turn = models.CharField(max_length=500)
    coil_weight = models.CharField(max_length=500)
    total_weight = models.CharField(max_length=500)
    core_length = models.CharField(max_length=500)

    def __str__(self):
        return self.job.job_no + "/" + self.product + "/" + self.make
    
    class Meta:
        verbose_name_plural = "Test Reports"

class scope_of_work(models.Model):
    job = models.ForeignKey(jobRegister, on_delete=models.CASCADE)
    ref_no = models.CharField(max_length=500)
    date = models.DateField()
    to = models.TextField(default="<name of the officer>\n<designation>\n<address_line>\n")
    sub = models.TextField()
    ref = models.TextField()
    scope_of_work = models.TextField()
    testing_and_inspection = models.TextField()
    terms_condition = models.TextField()


    def __str__(self):
        return self.job.job_no + "/" + self.ref_no
    
    class Meta:
        verbose_name_plural = "Scope of Works"

class Quotation(models.Model):
    job = models.ForeignKey(jobRegister, on_delete=models.CASCADE)
    date = models.DateField()
    quotation_no = models.CharField(max_length=200)
    quotation_file = models.FileField(upload_to='quotations/')
    comments = models.TextField(blank=True,null=True,help_text="comments if any")

    def __str__(self):
        return self.job.job_no + "(Quotation No : )" + self.quotation_no
    
    class Meta:
        verbose_name_plural = "Quotations"

class InspectionReport(models.Model):
    job = models.ForeignKey(jobRegister, on_delete=models.CASCADE)
    ref_no = models.CharField(max_length=500)
    date = models.DateField()
    to = models.TextField(default="<name of the officer>\n<designation>\n<address_line>\n")
    sub = models.TextField()
    image_captions = models.TextField(help_text="Enter captions separated by comma",blank=True,null=True)
    inspection_actual_report = models.TextField()
    comments = models.TextField(blank=True,null=True,help_text="comments if any")

    def __str__(self):
        return self.job.job_no + "/" + self.sub
    
    class Meta:
        verbose_name_plural = "Inspection Reports"

class TestReportDocument(models.Model):
    job = models.ForeignKey(jobRegister, on_delete=models.CASCADE)
    motor_details = models.TextField()
    jobs_tests_carried_out = models.TextField()
    customer_details = models.TextField()

    def __str__(self):
        return self.job.job_no
    
    class Meta:
        verbose_name_plural = "Test Report Documents"