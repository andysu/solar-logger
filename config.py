inverter_ip = ""
inverter_port = 502
# Slave Defaults
# Sungrow: 0x01
# SMA: 3
slave = 0x00
model = "Huawei"
location = "main"
timeout = 3
scan_interval = 30
info_interval = 60 * 60 * 3
influxdb_ip = "127.0.0.1"
influxdb_port = 8086
influxdb_user = "user_name"
influxdb_password = "password"
influxdb_database = "logger"
influxdb_longterm = "logger_lt"
influxdb_ssl = True
influxdb_verify_ssl = False
offset_ab = -0.2
offset_a = -0.5
offset_b = 1.5
latitude = lat
longitude = longitude
forcast_capacity = 10 # in kW
tilt = my_tilt
azimuth = 180   # 0 north, 180 south
time_zone = 'your timezone'
solcast_api = "your_key"
install_date = "20yy-mm-dd"
site_UUID = "xxxx-xxxx-xxxx-xxxx"
soltun = True # also skipped if solfor not equals 1
solfor = 1 # 0 off, 1 rooftop, 2 world pv power
debug = True