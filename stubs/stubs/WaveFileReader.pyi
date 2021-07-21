class WeatherReader(object):
	def assign(self): 
		pass

	def export(self) -> dict:
		pass

	def __init__(self, *args, **kwargs): 
		pass


	use_specific_wf_wave = float
	wave_resource_filename = str
	wave_resource_filename_ts = str
	wave_resource_model_choice = float


class Outputs(object):
	def assign(self): 
		pass

	def export(self) -> dict:
		pass

	def __init__(self, *args, **kwargs): 
		pass


	average_power_flux = float
	bathymetry = str
	city = str
	country = str
	data_source = str
	day = tuple
	energy_period = tuple
	hour = tuple
	lat = float
	lon = float
	minute = tuple
	month = tuple
	name = str
	nearby_buoy_number = str
	notes = str
	number_hours = float
	number_records = float
	sea_bed = str
	significant_wave_height = tuple
	state = str
	tz = float
	wave_resource_matrix = tuple
	year = tuple


class WaveFileReader(object):
	def assign(self, dict):
		pass

	def value(self, name, value=None):
		pass

	def unassign(self, name):
		pass

	def execute(self, int_verbosity):
		pass

	def export(self):
		pass

	def __getattribute__(self, *args, **kwargs):
		pass

	def __init__(self, *args, **kwargs):
		pass

	WeatherReader = WeatherReader
	Outputs = Outputs


def default(config) -> WaveFileReader:
	pass

def new() -> WaveFileReader:
	pass

def wrap(ssc_data_t) -> WaveFileReader:
	pass

def from_existing(model, config="") -> WaveFileReader:
	pass

__loader__ = None 

__spec__ = None
